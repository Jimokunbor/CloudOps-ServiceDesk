# Software Requirements Specification (SRS)

# CloudOps ServiceDesk

Version: 1.0.0

Author: Okunbor James Ehigiamusoe

Status: Active Development

---

# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional, non-functional, technical, and business requirements for CloudOps ServiceDesk.

The document serves as the primary reference for the design, implementation, testing, deployment, maintenance, and future enhancement of the platform throughout its software development lifecycle.

It establishes a common understanding of the system's expected behaviour, architecture, quality standards, and long-term objectives while providing a foundation for future development and project maintenance.

---

## 1.2 Project Scope

CloudOps ServiceDesk is an enterprise-style Information Technology Service Management (ITSM) platform developed to simulate the operational environment of a modern enterprise service desk.

The application enables users to submit IT support requests, technicians to manage assigned incidents, and administrators to oversee users, system operations, and platform configuration.

Beyond delivering service management functionality, the project demonstrates enterprise software engineering practices including secure authentication, RESTful API development, relational database management, Infrastructure as Code (IaC), DevOps automation, containerization, orchestration, monitoring, and cloud deployment.

The project also serves as a professional engineering portfolio demonstrating the complete software delivery lifecycle expected within enterprise cloud environments.

---

## 1.3 Intended Audience

This document is intended for:

- Software Developers
- Backend Engineers
- Cloud Engineers
- DevOps Engineers
- Platform Engineers
- Site Reliability Engineers (SREs)
- System Administrators
- Technical Reviewers
- Project Supervisors
- Technical Recruiters
- Future Project Contributors

---

## 1.4 Document Structure

This Software Requirements Specification is organised into the following sections:

- Introduction
- Functional Requirements
- Non-Functional Requirements
- User Roles
- Enterprise Roadmap
- Technology Constraints
- Success Criteria
- Document Maintenance

Each section defines a specific aspect of the platform to ensure development remains aligned with the project's architectural goals, enterprise roadmap, and software engineering standards.

---

## 1.5 Definitions, Acronyms and Abbreviations

| Term | Description |
|------|-------------|
| API | Application Programming Interface |
| CI/CD | Continuous Integration and Continuous Deployment |
| DevOps | Development and Operations |
| IaC | Infrastructure as Code |
| ITSM | Information Technology Service Management |
| JWT | JSON Web Token |
| ORM | Object Relational Mapping |
| RBAC | Role-Based Access Control |
| REST | Representational State Transfer |
| SLA | Service Level Agreement |
| SRE | Site Reliability Engineering |
| VPC | Virtual Private Cloud |

---

## 1.6 References

This specification should be read together with the following project documentation.

- docs/PROJECT_OVERVIEW.md
- docs/readme/
- OpenAPI (Swagger) Documentation
- GitHub Repository
- Project Roadmap

---

# 2. Functional Requirements

This section defines the business functionality provided by CloudOps ServiceDesk. Each requirement has a unique identifier to improve traceability throughout development, testing, deployment, and future maintenance.

---

## 2.1 Authentication

### Purpose

The authentication module provides secure identity verification before allowing access to protected resources within the platform.

### Current Capabilities

**AUTH-001**

The system shall allow new users to register an account.

**AUTH-002**

The system shall securely authenticate registered users.

**AUTH-003**

The system shall hash user passwords before storing them.

**AUTH-004**

The system shall generate JWT access tokens after successful authentication.

**AUTH-005**

The system shall support OAuth2 Password Flow.

**AUTH-006**

The system shall protect secured API endpoints.

**AUTH-007**

The system shall return the authenticated user's profile information.

### Enterprise Roadmap

The authentication module will later support:

- Password Reset
- Refresh Tokens
- Multi-Factor Authentication (MFA)
- Single Sign-On (SSO)
- Password Expiration
- Login History
- Security Audit Logging

---

## 2.2 User Management

### Purpose

The user management module controls user accounts, permissions, and access across the platform.

### Current Capabilities

**USER-001**

The system shall create user accounts.

**USER-002**

The system shall assign application roles.

**USER-003**

The system shall enforce Role-Based Access Control (RBAC).

### Enterprise Roadmap

Future enhancements include:

- User Profiles
- Profile Editing
- Password Change
- User Activation
- User Deactivation
- Department Assignment
- User Search
- Last Login Tracking

---

## 2.3 Ticket Management

### Purpose

Ticket management is the primary business function of CloudOps ServiceDesk. It enables users to submit requests while technicians and administrators manage the complete incident lifecycle.

### Current Capabilities

**TICKET-001**

The system shall create tickets.

**TICKET-002**

The system shall retrieve tickets.

**TICKET-003**

The system shall update tickets.

**TICKET-004**

The system shall delete tickets.

**TICKET-005**

The system shall assign tickets to technicians.

**TICKET-006**

The system shall update ticket status.

**TICKET-007**

The system shall display tickets assigned to the authenticated technician.

**TICKET-008**

The system shall display technician dashboard statistics.

### Enterprise Roadmap

Future functionality will include:

- Ticket Categories
- Priority Levels
- Due Dates
- SLA Management
- Attachments
- Ticket Tags
- Escalation Rules
- Ticket Merge
- Ticket Archive
- Ticket Reopening

---

## 2.4 Ticket Workflow

### Purpose

The workflow module controls how support tickets progress through predefined lifecycle stages.

### Current Workflow

```text
New
↓
Assigned
↓
In Progress
↓
Resolved
↓
Closed
```

### Future Enterprise Workflow

```text
New
↓
Assigned
↓
Acknowledged
↓
In Progress
↓
Pending Customer
↓
Pending Vendor
↓
Resolved
↓
Closed
↑
Reopened
```

### Requirements

**WORKFLOW-001**

The system shall enforce valid workflow transitions.

**WORKFLOW-002**

The system shall reject invalid workflow transitions.

---

## 2.5 Dashboard and Reporting

### Purpose

Dashboards provide operational insight into users, tickets, technicians, and platform activity.

### Current Capabilities

**DASH-001**

The system shall display assigned tickets.

**DASH-002**

The system shall display dashboard statistics.

### Enterprise Roadmap

Future dashboards will include:

Administrator

- User Statistics
- Ticket Statistics
- Critical Incidents
- Resolution Metrics

Technician

- Assigned Tickets
- Due Today
- Pending Work
- Daily Performance

End User

- My Open Tickets
- My Closed Tickets
- Recent Activity

---

## 2.6 Search and Reporting

### Purpose

Search and reporting features improve operational visibility and data analysis.

### Future Requirements

**REPORT-001**

Search tickets by title.

**REPORT-002**

Search tickets by status.

**REPORT-003**

Search tickets by priority.

**REPORT-004**

Generate technician reports.

**REPORT-005**

Generate SLA reports.

**REPORT-006**

Generate management reports.

---

# 3. Non-Functional Requirements

## Security

The platform shall:

- Protect user credentials using secure password hashing.
- Authenticate users using JWT.
- Enforce Role-Based Access Control.
- Protect sensitive configuration using environment variables.
- Follow the Principle of Least Privilege.

---

## Performance

The application shall provide responsive API performance under normal operating conditions.

---

## Scalability

The application shall support horizontal scaling through containerized deployment.

---

## Reliability

The platform shall provide reliable operation with consistent database integrity.

---

## Availability

The application shall support highly available deployment within a cloud environment.

---

## Maintainability

The source code shall follow modular architecture, clean coding principles, version control best practices, and comprehensive documentation.

---

## Observability

The application shall support:

- Logging
- Monitoring
- Metrics Collection
- Health Checks
- Alerting

---

# 4. User Roles

## Guest

- Register
- Login

---

## End User

- Create Tickets
- View Own Tickets
- Update Own Tickets
- Close Own Tickets

---

## Technician

- View Assigned Tickets
- Update Ticket Status
- Resolve Tickets

---

## IT Manager

- Assign Tickets
- Reassign Tickets
- View Operational Reports

---

## Administrator

- Manage Users
- Manage Roles
- Manage Platform Configuration
- View System Reports
- Delete Tickets

---

# 5. Enterprise Roadmap

Future milestones will introduce:

- Terraform
- Ansible
- Docker Compose
- Kubernetes
- GitHub Actions
- Prometheus
- Grafana
- Loki
- Redis
- Celery
- Amazon S3
- Amazon EC2
- Amazon VPC
- Application Load Balancer
- Nginx
- Audit Logs
- Email Notifications
- Knowledge Base
- Asset Management
- Incident Management
- Change Management

---

# 6. Technology Constraints

The project uses or will use the following technologies.

Backend

- Python
- FastAPI

Database

- PostgreSQL

ORM

- SQLAlchemy

Database Migration

- Alembic

Authentication

- JWT
- OAuth2

Infrastructure as Code

- Terraform

Configuration Management

- Ansible

Containerization

- Docker

Container Orchestration

- Kubernetes

Monitoring

- Prometheus
- Grafana

Cloud Platform

- Amazon Web Services (AWS)

Version Control

- Git
- GitHub

CI/CD

- GitHub Actions

---

# 7. Success Criteria

CloudOps ServiceDesk will be considered production-ready when:

- Authentication is fully implemented.
- RBAC is fully enforced.
- Ticket lifecycle management is complete.
- Dashboard functionality is complete.
- Docker deployment is operational.
- AWS infrastructure is provisioned using Terraform.
- Servers are configured using Ansible.
- Kubernetes deployment is operational.
- CI/CD pipelines are fully automated.
- Monitoring and logging are operational.
- Documentation is complete.
- Production deployment is successful.

---

# 8. Document Maintenance

This Software Requirements Specification shall be reviewed and updated after each completed project milestone to ensure that implementation remains aligned with the project's objectives, architecture, enterprise roadmap, and production readiness goals.