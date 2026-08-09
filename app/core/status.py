from enum import Enum


class TicketStatus(str, Enum):
    NEW = "New"
    OPEN = "Open"
    ASSIGNED = "Assigned"
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"