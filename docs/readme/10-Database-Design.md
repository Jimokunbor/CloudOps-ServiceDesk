# Database Design

## Introduction

The CloudOps ServiceDesk database has been designed to provide a reliable, scalable, and maintainable foundation for storing application data. A relational database model has been adopted to ensure data integrity, enforce relationships between entities, and support future expansion as new enterprise features are introduced.

PostgreSQL has been selected as the primary database management system because of its reliability, performance, standards compliance, and widespread adoption within enterprise environments.

---

# Database Objectives

The database has been designed to:

- Maintain data integrity.
- Support secure data storage.
- Enforce relationships between entities.
- Eliminate unnecessary data duplication.
- Support future enterprise expansion.
- Provide reliable transaction management.
- Simplify maintenance through version-controlled migrations.

---

# Database Technology

| Technology | Purpose |
|------------|---------|
| PostgreSQL | Primary relational database |
| SQLAlchemy | Object Relational Mapping (ORM) |
| Alembic | Database schema version control |
| UUID | Primary key generation |

---

# Current Database Structure

The current implementation contains the following primary entities.

## Users

The Users table stores account information for everyone who accesses the platform.

Current information includes:

- Unique Identifier (UUID)
- Full Name
- Email Address
- Password Hash
- Role
- Active Status
- Created Date
- Updated Date

---

## Tickets

The Tickets table stores all support requests submitted through the platform.

Current information includes:

- Unique Identifier (UUID)
- Title
- Description
- Status
- Priority
- Created By
- Assigned To
- Created Date
- Updated Date

---

# Entity Relationships

The current relationships are:

```text
Users
   │
   ├──────────────┐
   │              │
   ▼              ▼
Created By    Assigned To
        │
        ▼
      Tickets
```

A user may create multiple tickets.

A technician may be assigned multiple tickets.

Each ticket is created by one user and may be assigned to one technician.

---

# Database Design Principles

The database follows the following principles:

- Relational database design.
- Normalised data structure.
- UUID primary keys.
- Foreign key relationships.
- Data integrity.
- Transaction consistency.
- Scalable schema design.

---

# Current Implementation

The database currently supports:

- User Management
- Authentication
- Role-Based Access Control (RBAC)
- Ticket Management
- Ticket Assignment
- Ticket Status Tracking

Database schema changes are managed through Alembic migrations to ensure every structural change is version controlled.

---

# Enterprise Roadmap

The database will expand to support additional entities including:

- Departments
- Categories
- Attachments
- Comments
- Notifications
- Audit Logs
- Activity History
- Assets
- Knowledge Base
- Service Requests
- Change Requests

Each new entity will follow the same relational design principles used throughout the existing database.

---

# Future Entity Relationship Model

Future relationships will include:

```text
Users
 │
 ├──────── Tickets
 │              │
 │              ├──────── Comments
 │              ├──────── Attachments
 │              ├──────── Activity Logs
 │              └──────── Notifications
 │
 ├──────── Departments
 │
 └──────── Roles
```

This expanded model will support a more comprehensive enterprise IT Service Management (ITSM) platform while maintaining data consistency and scalability.

---

# Related Documentation

- 05-System-Architecture.md
- 06-Project-Structure.md
- 07-API-Reference.md
- 09-Ticket-Lifecycle.md

---

# Revision History

| Version | Description |
|----------|-------------|
| 1.0 | Initial database design documentation. |

---

# Document Status

Draft