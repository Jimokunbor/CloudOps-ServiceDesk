# API Reference

## Introduction

CloudOps ServiceDesk exposes a RESTful API that enables secure communication between client applications and the backend platform. The API follows REST principles and returns JSON responses for all supported operations.

The API has been designed using FastAPI and follows a modular architecture that separates authentication, business logic, artificial intelligence, infrastructure services, background processing, cloud infrastructure and data access into independent layers.

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
- Asynchronous Background Processing
- Artificial Intelligence Service Integration
- Infrastructure as Code (IaC)
- Cloud-Native Architecture

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
| /admin | GET | Endpoint restricted to administrators. |

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

# Artificial Intelligence API

Base Path

```text
/ai
```

Purpose

Provides Artificial Intelligence capabilities for ticket analysis and intelligent assistance within CloudOps ServiceDesk.

Current Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /classify | POST | Classify an IT support ticket using the AI service layer. |
| /summarize | POST | Generate a concise summary of an IT support ticket. |
| /priority | POST | Recommend an appropriate priority level for an IT support ticket. |

Current Capabilities

- AI Provider Abstraction
- Prompt Management
- Ticket Classification
- Ticket Summarization
- Priority Recommendation
- Provider-Independent AI Architecture

Supported AI Providers

- OpenAI
- Azure OpenAI
- Ollama
- AWS Bedrock

---

# Health API

Base Path

```text
/health
```

Purpose

Provides application health and operational status information for developers, administrators, monitoring platforms, container orchestration systems, cloud infrastructure and future Application Load Balancers.

Current Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| / | GET | Returns the application's operational status, environment, version and current timestamp while triggering an asynchronous background notification task. |

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
- Docker Compose
- NGINX Reverse Proxy
- Amazon EC2
- Application Load Balancer (Future)
- Kubernetes Readiness Probes
- Kubernetes Liveness Probes
- Monitoring Systems

---

# Background Processing

Purpose

CloudOps ServiceDesk supports asynchronous task execution using Celery and Redis.

Current Background Tasks

| Task | Description |
|------|-------------|
| send_notification | Executes notification processing asynchronously without blocking API requests. |

Infrastructure

- Redis Message Broker
- Celery Worker
- Docker Container
- Asynchronous Task Queue

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

Authentication Flow

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

Docker Deployment

Swagger UI

```text
http://localhost/docs
```

Local Development

Swagger UI

```text
http://127.0.0.1:8000/docs
```

Health Endpoint

```text
http://localhost/health/
```

---

# Current Enterprise Platform

The current API platform includes:

- RESTful API
- FastAPI
- JWT Authentication
- OAuth2
- Role-Based Access Control (RBAC)
- Ticket Management
- Artificial Intelligence Service Layer
- AI Ticket Classification
- AI Ticket Summarization
- AI Priority Recommendation
- Enterprise Health API
- Docker
- Docker Compose
- Docker Health Checks
- NGINX Reverse Proxy
- Structured Logging
- Environment Separation
- Redis Integration
- Celery Background Processing
- PostgreSQL
- SQLAlchemy
- Alembic
- Terraform
- AWS CLI
- Amazon VPC
- Public Subnets
- Private Subnets
- Internet Gateway
- NAT Gateway
- Public Route Tables
- Private Route Tables
- Security Groups
- Amazon EC2
- Infrastructure as Code (IaC)

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
- Knowledge Base API
- Analytics API

Future cloud integration will include:

- Amazon S3
- Amazon RDS PostgreSQL
- Application Load Balancer
- Auto Scaling
- Route 53
- AWS Certificate Manager
- CloudWatch
- AWS Secrets Manager

---

# Related Documentation

- 05-System-Architecture.md
- 08-Authentication.md
- 09-Ticket-Lifecycle.md
- 10-Database-Design.md
- 16-AI-Integration.md
- 17-Project-Status.md

---

# Revision History

| Version | Description |
|----------|-------------|
| 1.0 | Initial API Reference documentation created. |
| 1.1 | Authentication and Ticket Management APIs documented. |
| 1.2 | Health API documented and enterprise monitoring endpoints added. |
| 1.3 | Added Docker Health Checks, Structured Logging, Environment Separation, Redis Integration and Celery Background Processing. |
| 1.4 | Added the Artificial Intelligence API, AI provider abstraction, ticket classification, ticket summarization and priority recommendation endpoints. |
| 1.5 | Added Terraform Infrastructure as Code foundation and AWS CLI integration to the enterprise platform documentation. |
| 1.6 | Updated the enterprise platform to include Amazon VPC, public and private networking, Internet Gateway, NAT Gateway, route tables, Security Groups and Amazon EC2 deployment through Terraform. |

---

# Document Status

Actively Maintained