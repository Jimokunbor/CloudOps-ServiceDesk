# API Reference

## Introduction

CloudOps ServiceDesk exposes a RESTful API that enables secure communication between client applications and the backend platform. The API follows REST principles and returns JSON responses for all supported operations.

The API has been designed using FastAPI and follows a modular architecture that separates authentication, business logic, and data access into independent layers.

Interactive API documentation is automatically generated through Swagger UI and OpenAPI.

---

# API Design Principles

The API has been designed according to the following principles:

- RESTful Architecture
- Stateless Communication
- JSON Data Exchange
- Secure Authentication
- Role-Based Access Control (RBAC)
- Input Validation
- Consistent Error Handling
- Modular Endpoint Design

---

# Authentication API

Base Path

```text
/auth
```

Purpose

Provides authentication and identity management services.

Current Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /register | POST | Register a new user account. |
| /login | POST | Authenticate a user and return a JWT access token. |
| /me | GET | Return information about the authenticated user. |
| /admin | GET | Example endpoint restricted to administrators. |

Access

- Guest
- Authenticated User
- Administrator

---

# Ticket API

Base Path

```text
/tickets
```

Purpose

Provides ticket management functionality throughout the application.

Current Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| / | POST | Create a new ticket. |
| / | GET | Retrieve all tickets. |
| /my | GET | Retrieve tickets assigned to the authenticated user. |
| /my/dashboard | GET | Retrieve dashboard summary information. |
| /{ticket_id} | GET | Retrieve a ticket by its unique identifier. |
| /{ticket_id} | PUT | Update an existing ticket. |
| /{ticket_id} | DELETE | Delete a ticket. |
| /{ticket_id}/assign | POST | Assign a ticket to a technician. |
| /{ticket_id}/status | PATCH | Update the status of a ticket. |

---

# Request Validation

The API validates all incoming requests using Pydantic models.

Validation includes:

- Required fields
- Data types
- Enumerations
- UUID validation
- Request schema validation

---

# Authentication

Protected endpoints require a valid JWT Bearer Token.

Authentication flow:

```text
User Login
      │
      ▼
JWT Token Generated
      │
      ▼
Authorization Header
      │
      ▼
Protected Endpoint
```

---

# Response Format

The API returns JSON responses.

Example

```json
{
    "id": "...",
    "title": "Printer not working",
    "status": "Assigned"
}
```

---

# HTTP Status Codes

Common response codes include:

| Code | Meaning |
|------|---------|
| 200 | Request successful |
| 201 | Resource created |
| 400 | Invalid request |
| 401 | Authentication required |
| 403 | Access denied |
| 404 | Resource not found |
| 422 | Validation error |
| 500 | Internal server error |

---

# Future API Expansion

Planned API modules include:

- User Administration API
- Dashboard API
- Reporting API
- Notification API
- File Upload API
- Audit Log API
- Asset Management API

---

# Related Documentation

- 05-System-Architecture.md
- 08-Authentication.md
- 09-Ticket-Lifecycle.md
- 10-Database-Design.md

---

# Revision History

| Version | Description |
|----------|-------------|
| 1.0 | Initial API Reference documentation. |

---

# Document Status

Draft