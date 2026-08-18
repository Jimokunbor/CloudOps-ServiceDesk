# API Reference

## Introduction

CloudOps ServiceDesk exposes a RESTful API that enables secure communication between client applications and the backend platform. The API follows REST principles and returns JSON responses for all supported operations.

The API has been designed using FastAPI and follows a modular architecture that separates authentication, business logic, infrastructure services, and data access into independent layers.

Interactive API documentation is automatically generated through Swagger UI and OpenAPI.

---

# API Design Principles

The API has been designed according to the following principles:

- RESTful Architecture
- Stateless Communication
- JSON Data Exchange
- JWT Authentication
- Role-Based Access Control (RBAC)
- Input Validation
- Consistent Error Handling
- Modular Endpoint Design
- Enterprise Health Monitoring

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
| /my | GET | Retrieve tickets belonging to the authenticated user. |
| /my/dashboard | GET | Retrieve dashboard summary information. |
| /{ticket_id} | GET | Retrieve a ticket by its unique identifier. |
| /{ticket_id} | PUT | Update an existing ticket. |
| /{ticket_id} | DELETE | Delete a ticket. |
| /{ticket_id}/assign | POST | Assign a ticket to a technician. |
| /{ticket_id}/status | PATCH | Update the status of a ticket. |

Access

- Authenticated User
- Technician
- Administrator

---

# Health API

Base Path

```text
/health
```

Purpose

Provides application health and operational status information for developers, administrators, monitoring platforms, container orchestration systems and load balancers.

Current Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| / | GET | Returns the current operational status of the application, environment, version and timestamp. |

Example Response

```json
{
    "status": "healthy",
    "application": "CloudOps ServiceDesk",
    "version": "1.0.0",
    "environment": "development",
    "timestamp": "2026-08-18T15:40:00Z"
}
```

Supported Consumers

- Docker Health Checks
- Nginx Reverse Proxy
- Kubernetes Readiness Probes
- Kubernetes Liveness Probes
- Monitoring Systems
- Cloud Load Balancers

---

# Request Validation

The API validates all incoming requests using Pydantic models.

Validation includes:

- Required fields
- Data types
- Enumerations
- UUID validation
- Request schema validation
- Automatic request serialization
- Automatic response validation

---

# Authentication

Protected endpoints require a valid JWT Bearer Token.

Authentication flow

```text
User Login
      │
      ▼
JWT Access Token Generated
      │
      ▼
Authorization: Bearer <token>
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

# Interactive API Documentation

Swagger UI

```text
http://localhost/docs
```

FastAPI Swagger (Development)

```text
http://localhost:8000/docs
```

Health Endpoint

```text
http://localhost/health/
```

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
- Artificial Intelligence API
- Knowledge Base API
- Analytics API

---

# Related Documentation

- 05-System-Architecture.md
- 08-Authentication.md
- 09-Ticket-Lifecycle.md
- 10-Database-Design.md
- 17-Project-Status.md

---

# Revision History

| Version | Description |
|----------|-------------|
| 1.0 | Initial API Reference documentation created. |
| 1.1 | Authentication and Ticket Management APIs documented. |
| 1.2 | Health API documented and enterprise monitoring endpoints added. |

---

# Document Status

Actively Maintained