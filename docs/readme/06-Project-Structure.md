# Project Structure

## Introduction

CloudOps ServiceDesk follows a structured, enterprise-oriented repository layout that separates application components according to their responsibilities. This organisation improves maintainability, readability, scalability and collaboration while supporting modern software engineering, cloud engineering and DevOps practices.

Each directory has a clearly defined purpose, allowing developers, recruiters, reviewers and future contributors to understand the overall architecture without needing to inspect the implementation details first.

---

# Repository Structure

```text
CloudOps-ServiceDesk/

│
├── .github/
├── alembic/
├── app/
├── database/
├── diagrams/
├── docker/
├── docs/
├── kubernetes/
├── monitoring/
├── nginx/
├── screenshots/
├── scripts/
├── terraform/
├── tests/
│
├── .env
├── alembic.ini
├── docker-compose.yml
├── LICENSE
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Directory Overview

## .github/

Contains GitHub configuration, repository templates and future GitHub Actions workflows for Continuous Integration (CI) and Continuous Deployment (CD).

---

## alembic/

Stores all database migration scripts and Alembic configuration used to manage PostgreSQL schema versioning throughout the application lifecycle.

---

## app/

Contains the complete backend application source code.

This directory includes:

- API endpoints
- Authentication
- Authorization
- Business services
- Artificial Intelligence services
- Database models
- Validation schemas
- Configuration
- Security
- Utilities
- Background task processing

---

## database/

Stores database resources, SQL scripts, development data and supporting database documentation.

---

## diagrams/

Contains architecture diagrams, infrastructure diagrams, workflow diagrams, deployment diagrams, database diagrams and other technical illustrations used throughout the documentation.

---

## docker/

Contains Docker configuration files required to build and manage the application's containerized environment.

---

## docs/

Contains all technical documentation maintained throughout the project lifecycle.

Documentation includes:

- Project documentation
- Architecture documentation
- Infrastructure documentation
- Deployment documentation
- AI documentation
- Project management documentation
- Developer documentation

---

## kubernetes/

Contains Kubernetes manifests and deployment configuration prepared for future container orchestration.

---

## monitoring/

Contains monitoring configuration for enterprise observability platforms including Prometheus, Grafana and Loki.

---

## nginx/

Contains NGINX reverse proxy configuration used to securely route incoming requests to the FastAPI application.

---

## screenshots/

Contains implementation screenshots used throughout the technical documentation to provide evidence of completed milestones.

---

## scripts/

Contains automation scripts used for infrastructure provisioning, application deployment, server configuration and operational tasks.

---

## terraform/

Contains the Infrastructure as Code (IaC) implementation for provisioning Amazon Web Services (AWS) infrastructure.

The directory currently includes:

- Provider configuration
- Project variables
- Local values
- Virtual Private Cloud (VPC)
- Public subnets
- Private subnets
- Internet Gateway
- NAT Gateway
- Route tables
- Security Groups
- IAM Roles
- IAM Instance Profiles
- Amazon EC2 deployment
- User Data scripts

---

## tests/

Contains automated tests used to validate application functionality, authentication, business logic, APIs and future infrastructure components.

---

# Root Files

## .env

Stores environment-specific configuration values that are excluded from version control.

---

## alembic.ini

Contains Alembic configuration used to manage database migrations.

---

## docker-compose.yml

Defines the multi-container Docker environment used for local development.

---

## LICENSE

Defines the software license governing the project.

---

## README.md

Provides the public overview of the repository together with setup instructions and links to the complete technical documentation.

---

## requirements.txt

Lists all Python package dependencies required to build and run the backend application.

---

## .gitignore

Specifies files and directories that should not be committed to the Git repository.

---

# Project Organisation Principles

The repository has been organised according to the following engineering principles:

- Separation of Concerns
- Layered Architecture
- Modular Design
- Scalability
- Maintainability
- Infrastructure as Code (IaC)
- Documentation-Driven Development
- Enterprise Repository Structure
- Cloud-Native Engineering
- Production-Oriented Development

---

# Benefits of the Project Structure

The chosen repository structure provides several advantages:

- Separates responsibilities across independent components.
- Improves maintainability and long-term scalability.
- Simplifies navigation for developers, reviewers and recruiters.
- Supports Infrastructure as Code (IaC) development.
- Encourages modular software engineering practices.
- Simplifies onboarding for future contributors.
- Supports enterprise cloud deployment workflows.
- Enables future automation through DevOps and CI/CD pipelines.
- Provides a structured foundation for production-ready cloud infrastructure.