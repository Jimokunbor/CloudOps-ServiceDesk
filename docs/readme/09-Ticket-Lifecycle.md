# Ticket Lifecycle

## Introduction

The ticket lifecycle defines the journey of every support request submitted through CloudOps ServiceDesk. It provides a structured workflow that ensures incidents are managed consistently, responsibilities are clearly assigned, and progress can be monitored from creation to completion.

The workflow has been designed to reflect enterprise IT Service Management (ITSM) practices while remaining simple enough to evolve as additional functionality is introduced.

---

# Objectives

The ticket lifecycle has been designed to:

- Standardise ticket processing.
- Track ticket progress.
- Improve accountability.
- Support technician workflows.
- Maintain consistent status transitions.
- Prepare the platform for future ITSM capabilities.

---

# Current Ticket Workflow

The current implementation supports the following lifecycle.

```text
New
 │
 ▼
Assigned
 │
 ▼
In Progress
 │
 ▼
Resolved
 │
 ▼
Closed
```

Each status must follow the defined sequence.

Invalid status transitions are rejected by the application.

---

# Status Definitions

## New

A ticket has been created by a user but has not yet been assigned to a technician.

---

## Assigned

An administrator assigns the ticket to a technician who becomes responsible for handling the request.

---

## In Progress

The assigned technician has started investigating or resolving the issue.

---

## Resolved

The technician has completed the required work and marked the ticket as resolved.

---

## Closed

The ticket has been completed and no further action is required.

Closed tickets become read-only unless future functionality allows reopening.

---

# Current Responsibilities

## End User

Can:

- Create tickets
- View personal tickets
- Update eligible tickets

---

## Technician

Can:

- View assigned tickets
- Update ticket status
- Resolve assigned tickets

---

## Administrator

Can:

- View all tickets
- Assign technicians
- Update any ticket
- Delete tickets
- Monitor ticket activity

---

# Workflow Validation

CloudOps ServiceDesk validates every status transition to ensure that tickets follow the defined lifecycle.

The application prevents users from skipping stages or performing invalid transitions that could compromise workflow consistency.

---

# Enterprise Workflow

Future versions of the platform will extend the lifecycle to support additional enterprise ITSM processes.

```text
New
 │
 ▼
Assigned
 │
 ▼
Acknowledged
 │
 ▼
In Progress
 │
 ▼
Pending Customer
 │
 ▼
Pending Vendor
 │
 ▼
Resolved
 │
 ▼
Closed
 ▲
 │
Reopened
```

These additional states will improve operational visibility and more closely align the platform with enterprise service desk workflows.

---

# Future Enhancements

Planned improvements include:

- Service Level Agreement (SLA) tracking
- Automatic ticket escalation
- Priority-based routing
- Assignment history
- Internal technician notes
- Activity timeline
- Email notifications
- Ticket reopening
- Audit logging

---

# Related Documentation

- 03-Features.md
- 07-API-Reference.md
- 08-Authentication.md
- 10-Database-Design.md

---

# Revision History

| Version | Description |
|----------|-------------|
| 1.0 | Initial ticket lifecycle documentation. |

---

# Document Status

Draft