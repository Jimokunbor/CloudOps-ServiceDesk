from enum import Enum


class UserRole(str, Enum):
    USER = "user"
    TECHNICIAN = "technician"
    MANAGER = "manager"
    ADMIN = "admin"