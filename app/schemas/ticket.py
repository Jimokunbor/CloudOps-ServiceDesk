from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.core.status import TicketStatus


class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str = "Medium"


class TicketUpdate(BaseModel):
    title: str
    description: str
    priority: str
    status: TicketStatus


class TicketAssign(BaseModel):
    technician_id: UUID


class TicketStatusUpdate(BaseModel):
    status: TicketStatus


class TicketDashboard(BaseModel):
    assigned: int
    in_progress: int
    resolved: int
    closed: int


class TicketResponse(BaseModel):
    id: UUID
    title: str
    description: str
    status: TicketStatus
    priority: str
    created_by: UUID
    assigned_to: UUID | None
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }