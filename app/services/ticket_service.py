from uuid import UUID

from sqlalchemy.orm import Session

from app.core.status import TicketStatus
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate
from app.schemas.ticket import TicketUpdate


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


def get_all_tickets(db: Session):
    return db.query(Ticket).all()


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
    ticket = get_ticket_by_id(db, ticket_id)

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
    ticket = get_ticket_by_id(db, ticket_id)

    if not ticket:
        return None

    ticket.title = ticket_data.title
    ticket.description = ticket_data.description
    ticket.priority = ticket_data.priority
    ticket.status = ticket_data.status

    db.commit()
    db.refresh(ticket)

    return ticket