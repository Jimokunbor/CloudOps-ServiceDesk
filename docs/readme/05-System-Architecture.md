# System Architecture

## Introduction

CloudOps ServiceDesk follows a layered architecture designed to promote modularity, maintainability, scalability, and separation of concerns. Each layer has a clearly defined responsibility, allowing the application to evolve without introducing unnecessary coupling between components.

This architectural approach reflects software engineering practices commonly adopted within enterprise environments and supports future expansion as additional features and infrastructure components are introduced.

---

# Architectural Principles

The platform has been designed around the following principles:

- Separation of Concerns
- Modular Design
- Layered Architecture
- RESTful API Design
- Stateless Authentication
- Role-Based Access Control (RBAC)
- Infrastructure as Code (IaC)
- Cloud-Native Design
- Security by Design
- Scalability

---

# High-Level Architecture

The application follows the request flow shown below.

```text
Client Application
        │
        ▼
FastAPI REST API
        │
        ▼
Authentication & Authorization
        │
        ▼
API Endpoints
        │
        ▼
Business Services
        │
        ▼
Database Layer
        │
        ▼
PostgreSQL Database
```

Every incoming request passes through each layer before a response is returned to the client.

---

# Application Layers

## Client Layer

The Client Layer represents any application that communicates with CloudOps ServiceDesk, including Swagger UI, future web applications, mobile applications, and third-party integrations.

Responsibilities include:

- Sending HTTP requests
- Displaying responses
- Providing user interaction

---

## API Layer

The API Layer exposes RESTful endpoints using FastAPI.

Responsibilities include:

- Receiving requests
- Validating request data
- Returning structured responses
- Managing endpoint routing

---

## Authentication Layer

The Authentication Layer verifies user identity and controls access to protected resources.

Responsibilities include:

- User authentication
- JWT validation
- OAuth2 authentication flow
- Role verification

---

## Business Logic Layer

The Business Logic Layer contains the application's core functionality.

Responsibilities include:

- Ticket management
- User management
- Business rules
- Workflow validation
- Dashboard calculations

---

## Data Access Layer

The Data Access Layer communicates with the database through SQLAlchemy.

Responsibilities include:

- Database queries
- Data persistence
- Relationship management
- Transaction handling

---

## Database Layer

PostgreSQL serves as the primary relational database.

Responsibilities include:

- Data storage
- Data integrity
- Relationship enforcement
- Transaction consistency

---

# Current Architecture

The current implementation includes:

- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT Authentication
- RBAC
- Swagger UI

---

# Target Enterprise Architecture

As development progresses, the architecture will expand to include:

```text
Client
      │
      ▼
NGINX
      │
      ▼
FastAPI
      │
      ▼
Business Services
      │
      ▼
PostgreSQL
      │
      ▼
Docker
      │
      ▼
Kubernetes
      │
      ▼
Amazon Web Services
```

Additional enterprise components will include:

- Terraform
- Ansible
- GitHub Actions
- Prometheus
- Grafana
- Loki
- Amazon S3

---

# Architectural Benefits

This architecture provides:

- Clear separation of responsibilities
- Improved maintainability
- Easier testing
- Better scalability
- Enhanced security
- Simplified deployment
- Support for future enterprise expansion