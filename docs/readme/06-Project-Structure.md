# Project Structure

## Introduction

CloudOps ServiceDesk follows a structured project layout that separates application components according to their responsibilities. This organisation improves maintainability, readability, scalability, and collaboration while supporting enterprise software engineering practices.

Each directory has a clearly defined purpose, allowing new contributors and reviewers to understand the project without needing to inspect the source code first.

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
├── LICENSE
├── README.md
└── requirements.txt
```

---

# Directory Overview

## .github/

Contains GitHub-specific configuration, including future GitHub Actions workflows for Continuous Integration and Continuous Deployment (CI/CD).

---

## alembic/

Stores all database migration scripts and Alembic configuration used to manage PostgreSQL schema versioning.

---

## app/

Contains the application's source code.

This directory includes:

- API endpoints
- Business services
- Database models
- Validation schemas
- Security components
- Application configuration
- Utility functions

---

## database/

Stores SQL scripts, database resources, seed data, and supporting database documentation.

---

## diagrams/

Contains architecture diagrams, database diagrams, workflow diagrams, deployment diagrams, and other visual documentation used throughout the project.

---

## docker/

Contains Docker-related configuration files used to build and run containerized versions of the application.

---

## docs/

Contains all project documentation.

Documentation is organised into:

- Internal development documentation
- Software requirements
- Project overview
- README source files
- Future architecture documentation

---

## kubernetes/

Contains Kubernetes deployment manifests and related configuration files used for container orchestration.

---

## monitoring/

Contains monitoring configuration for services such as Prometheus and Grafana.

---

## nginx/

Contains reverse proxy configuration used to route requests to the backend application.

---

## scripts/

Contains automation scripts that simplify development, deployment, maintenance, and operational tasks.

---

## terraform/

Contains Infrastructure as Code (IaC) modules used to provision AWS resources.

---

## tests/

Contains automated tests for validating application functionality, business logic, and API behaviour.

---

# Root Files

## .env

Stores environment-specific configuration values that should not be committed to version control.

---

## alembic.ini

Contains Alembic configuration used for database migrations.

---

## LICENSE

Defines the software license governing the project.

---

## README.md

Provides the public overview of the repository and links to supporting documentation.

---

## requirements.txt

Lists all Python package dependencies required to build and run the application.

---

# Project Organisation Principles

The repository has been organised according to the following engineering principles:

- Separation of Concerns
- Modular Design
- Scalability
- Maintainability
- Clear Directory Ownership
- Documentation-Driven Development
- Infrastructure as Code
- Production-Oriented Project Structure

---

# Benefits of the Project Structure

The chosen repository structure provides several advantages:

- Improves maintainability by separating responsibilities.
- Simplifies navigation for developers and reviewers.
- Supports future project growth without major restructuring.
- Encourages modular software development.
- Aligns with enterprise software engineering practices.
- Simplifies onboarding for future contributors.