# System Architecture

## Introduction

CloudOps ServiceDesk follows a layered architecture designed to promote modularity, maintainability, scalability and separation of concerns. Each layer has a clearly defined responsibility, allowing the application to evolve without introducing unnecessary coupling between components.

This architectural approach reflects software engineering practices commonly adopted within enterprise environments and supports future expansion as additional application features, cloud infrastructure and enterprise services are introduced.

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
- High Availability
- Automation First

---

# High-Level Architecture

The application currently follows the request flow shown below.

```text
                        User / Client
                              │
                              ▼
                    Web Browser / Swagger UI
                              │
                              ▼
                           NGINX
                    (Reverse Proxy)
                              │
                              ▼
                     FastAPI REST API
                              │
                              ▼
             Authentication & Authorization
                    (JWT / OAuth2 / RBAC)
                              │
                              ▼
                     API Endpoints Layer
                              │
                              ▼
                  Business Services Layer
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
       Artificial Intelligence           Celery Worker
           Service Layer              Background Processing
              │                               │
              └───────────────┬───────────────┘
                              ▼
                         Redis Broker
                              │
                              ▼
                    SQLAlchemy ORM Layer
                              │
                              ▼
                    PostgreSQL Database
```

Every incoming request passes through the appropriate application layers before a response is returned to the client.

---

# Application Layers

## Client Layer

The Client Layer represents applications that communicate with CloudOps ServiceDesk, including Swagger UI, future web applications, mobile applications and third-party integrations.

Responsibilities include:

- Sending HTTP requests
- Displaying responses
- User interaction
- API consumption

---

## Reverse Proxy Layer

The Reverse Proxy Layer is implemented using NGINX.

Responsibilities include:

- Routing incoming requests
- Reverse proxy services
- Request forwarding
- Backend service isolation

---

## API Layer

The API Layer exposes RESTful endpoints using FastAPI.

Responsibilities include:

- Receiving requests
- Request validation
- Response serialization
- Endpoint routing
- OpenAPI documentation

---

## Authentication Layer

The Authentication Layer verifies user identity and controls access to protected resources.

Responsibilities include:

- User authentication
- JWT validation
- OAuth2 Password Flow
- Role verification
- Access control

---

## Business Logic Layer

The Business Logic Layer contains the application's core functionality.

Responsibilities include:

- Ticket management
- User management
- Business rules
- Workflow validation
- Dashboard calculations
- Administrative operations

---

## Artificial Intelligence Layer

The Artificial Intelligence Layer provides intelligent support services for ticket processing.

Responsibilities include:

- Ticket classification
- Ticket summarization
- Priority recommendation
- AI service abstraction
- AI provider integration

---

## Background Processing Layer

Redis and Celery provide asynchronous task processing.

Responsibilities include:

- Background jobs
- Task queues
- Asynchronous processing
- Future notification services

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

# Cloud Infrastructure Architecture

CloudOps ServiceDesk provisions its cloud infrastructure using Terraform and Amazon Web Services (AWS).

The current cloud architecture consists of:

```text
                    Amazon Web Services
                            │
                            ▼
                 Virtual Private Cloud (VPC)
                  ┌────────────┴────────────┐
                  ▼                         ▼
          Public Subnets             Private Subnets
                  │                         │
                  ▼                         ▼
          Internet Gateway          NAT Gateway
                  │                         │
                  └────────────┬────────────┘
                               ▼
                        Route Tables
                               │
                               ▼
                       Security Groups
                               │
                               ▼
                    Amazon EC2 Web Server
                               │
                               ▼
                  Apache Web Server (User Data)
```

This infrastructure has been provisioned entirely through Infrastructure as Code (IaC) using Terraform.

---

# Current Architecture

The current implementation includes:

- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT Authentication
- OAuth2
- Role-Based Access Control (RBAC)
- Swagger UI
- Docker
- Docker Compose
- Redis
- Celery
- NGINX Reverse Proxy
- Structured Logging
- Health Monitoring
- Artificial Intelligence Service Layer
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
- Apache Web Server
- Infrastructure as Code (IaC)

---

# Target Enterprise Architecture

As development progresses, the architecture will expand into a fully cloud-native enterprise platform.

```text
                    Users / Internet
                            │
                            ▼
                     Route 53 DNS
                            │
                            ▼
                  AWS Certificate Manager
                            │
                            ▼
                Application Load Balancer
                            │
                ┌───────────┴───────────┐
                ▼                       ▼
          Amazon EC2              Amazon EC2
          Auto Scaling Group      Auto Scaling Group
                │                       │
                └───────────┬───────────┘
                            ▼
                      FastAPI Services
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
        Amazon RDS                    Amazon S3
       PostgreSQL                     Object Storage
                            │
                            ▼
                      CloudWatch
                            │
                            ▼
             Prometheus • Grafana • Loki
```

Additional enterprise components will include:

- Application Load Balancer (ALB)
- Auto Scaling Group
- Amazon RDS PostgreSQL
- Amazon S3
- Route 53
- AWS Certificate Manager (ACM)
- AWS Secrets Manager
- AWS Systems Manager
- VPC Endpoints
- AWS CloudTrail
- AWS WAF
- Ansible
- GitHub Actions
- Kubernetes

---

# Architectural Benefits

This architecture provides:

- Clear separation of responsibilities
- Modular application design
- Infrastructure as Code (IaC)
- Automated cloud provisioning
- Improved maintainability
- Easier testing
- Better scalability
- Enhanced security
- Enterprise networking
- Background task processing
- Artificial Intelligence integration
- Simplified deployment
- Support for high availability
- Foundation for cloud-native deployment
- Support for future enterprise expansion