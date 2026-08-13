from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_db as get_db
from app.api.dependencies import get_current_user
from app.models.user import User
from app.schemas.ticket import (
    TicketAssign,
    TicketCreate,
    TicketResponse,
    TicketStatusUpdate,
    TicketUpdate,
)
from app.services.ticket_service import (
    assign_ticket,
    create_ticket,
    delete_ticket,
    get_all_tickets,
    get_ticket_by_id,
    update_ticket,
    update_ticket_status,
)

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
    dependencies=[Depends(get_current_user)],
)


@router.post("/")
def create_new_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_ticket(
        db=db,
        ticket=ticket,
        created_by=current_user.id,
    )


@router.get("/")
def read_all_tickets(
    db: Session = Depends(get_db),
):
    return get_all_tickets(db)


@router.get("/{ticket_id}")
def read_ticket(
    ticket_id: UUID,
    db: Session = Depends(get_db),
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

    return ticket


@router.put("/{ticket_id}")
def edit_ticket(
    ticket_id: UUID,
    ticket: TicketUpdate,
    db: Session = Depends(get_db),
):
    updated_ticket = update_ticket(
        db,
        ticket_id,
        ticket,
    )

    if not updated_ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found",
        )

    return updated_ticket


@router.post(
    "/{ticket_id}/assign",
    response_model=TicketResponse,
)
def assign_ticket_to_technician(
    ticket_id: UUID,
    assignment: TicketAssign,
    db: Session = Depends(get_db),
):
    return assign_ticket(
        db=db,
        ticket_id=ticket_id,
        assignment=assignment,
    )


@router.patch(
    "/{ticket_id}/status",
    response_model=TicketResponse,
)
def change_ticket_status(
    ticket_id: UUID,
    status_update: TicketStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_ticket_status(
        db=db,
        ticket_id=ticket_id,
        status_update=status_update,
        current_user=current_user,
    )


@router.delete("/{ticket_id}")
def remove_ticket(
    ticket_id: UUID,
    db: Session = Depends(get_db),
):
    ticket = delete_ticket(
        db,
        ticket_id,
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found",
        )

    return {
        "message": "Ticket deleted successfully"
    }