from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.roles import UserRole
from app.core.status import TicketStatus
from app.models.ticket import Ticket
from app.models.user import User
from app.schemas.ticket import (
    TicketAssign,
    TicketCreate,
    TicketDashboard,
    TicketStatusUpdate,
    TicketUpdate,
)


def create_ticket(
    db: Session,
    ticket: TicketCreate,
    created_by: UUID,
):
    db_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        status=TicketStatus.NEW,
        created_by=created_by,
    )

    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)

    return db_ticket


def get_all_tickets(
    db: Session,
):
    return db.query(Ticket).all()


def get_my_tickets(
    db: Session,
    current_user: User,
):
    return (
        db.query(Ticket)
        .filter(
            Ticket.assigned_to == current_user.id
        )
        .all()
    )


def get_ticket_by_id(
    db: Session,
    ticket_id: UUID,
):
    return (
        db.query(Ticket)
        .filter(Ticket.id == ticket_id)
        .first()
    )


def delete_ticket(
    db: Session,
    ticket_id: UUID,
):
    ticket = get_ticket_by_id(
        db,
        ticket_id,
    )

    if not ticket:
        return None

    db.delete(ticket)
    db.commit()

    return ticket


def update_ticket(
    db: Session,
    ticket_id: UUID,
    ticket_data: TicketUpdate,
):
    ticket = get_ticket_by_id(
        db,
        ticket_id,
    )

    if not ticket:
        return None

    ticket.title = ticket_data.title
    ticket.description = ticket_data.description
    ticket.priority = ticket_data.priority
    ticket.status = ticket_data.status

    db.commit()
    db.refresh(ticket)

    return ticket


def assign_ticket(
    db: Session,
    ticket_id: UUID,
    assignment: TicketAssign,
):
    ticket = get_ticket_by_id(
        db,
        ticket_id,
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found",
        )

    technician = (
        db.query(User)
        .filter(User.id == assignment.technician_id)
        .first()
    )

    if not technician:
        raise HTTPException(
            status_code=404,
            detail="Technician not found",
        )

    if technician.role != UserRole.TECHNICIAN:
        raise HTTPException(
            status_code=400,
            detail="User is not a technician",
        )

    ticket.assigned_to = technician.id

    if ticket.status == TicketStatus.NEW:
        ticket.status = TicketStatus.ASSIGNED

    db.commit()
    db.refresh(ticket)

    return ticket


def update_ticket_status(
    db: Session,
    ticket_id: UUID,
    status_update: TicketStatusUpdate,
    current_user: User,
):
    ticket = get_ticket_by_id(
        db,
        ticket_id,
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found",
        )

    if (
        current_user.role != UserRole.ADMIN
        and ticket.assigned_to != current_user.id
    ):
        raise HTTPException(
            status_code=403,
            detail="You are not assigned to this ticket.",
        )

    allowed_transitions = {
        TicketStatus.NEW: [
            TicketStatus.ASSIGNED,
        ],
        TicketStatus.ASSIGNED: [
            TicketStatus.IN_PROGRESS,
        ],
        TicketStatus.IN_PROGRESS: [
            TicketStatus.RESOLVED,
        ],
        TicketStatus.RESOLVED: [
            TicketStatus.CLOSED,
        ],
        TicketStatus.CLOSED: [],
    }

    current_status = ticket.status
    new_status = status_update.status

    if new_status not in allowed_transitions[current_status]:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Cannot change ticket "
                f"from '{current_status.value}' "
                f"to '{new_status.value}'."
            ),
        )

    ticket.status = new_status

    db.commit()
    db.refresh(ticket)

    return ticket


def get_dashboard_summary(
    db: Session,
    current_user: User,
) -> TicketDashboard:
    tickets = (
        db.query(Ticket)
        .filter(
            Ticket.assigned_to == current_user.id
        )
        .all()
    )

    return TicketDashboard(
        assigned=sum(
            ticket.status == TicketStatus.ASSIGNED
            for ticket in tickets
        ),
        in_progress=sum(
            ticket.status == TicketStatus.IN_PROGRESS
            for ticket in tickets
        ),
        resolved=sum(
            ticket.status == TicketStatus.RESOLVED
            for ticket in tickets
        ),
        closed=sum(
            ticket.status == TicketStatus.CLOSED
            for ticket in tickets
        ),
    )