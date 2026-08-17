# CloudOps ServiceDesk

Enterprise-style IT Service Management (ITSM) platform demonstrating modern Backend Engineering, Cloud Engineering, DevOps, Infrastructure as Code, and Cloud-Native application development.

---

## Project Overview

CloudOps ServiceDesk is a production-oriented IT Service Management (ITSM) platform developed to demonstrate enterprise software engineering practices and modern cloud technologies.

The project simulates a real-world enterprise service desk where users can create, manage, and track IT support requests while administrators oversee ticket assignment, user management, and operational workflows.

Beyond implementing core ITSM functionality, the project showcases cloud-native architecture, Infrastructure as Code (IaC), containerization, automation, orchestration, monitoring, and continuous delivery using industry-standard technologies.

This repository is being developed as both a practical engineering project and a professional portfolio demonstrating enterprise backend and cloud engineering skills.

---

## Current Project Status

Current Version

```text
v1.0.0
```

Development Status

```text
Active Development
```

Current Milestone

```text
Documentation Completed
Backend Foundation Completed
Docker Containerization (Next)
```

---

## Implemented Features

Current implementation includes:

- User registration
- JWT authentication
- Password hashing
- Role-Based Access Control (RBAC)
- User profile endpoint
- Ticket creation
- Ticket update
- Ticket deletion
- Ticket assignment
- Ticket dashboard
- Ticket lifecycle management
- PostgreSQL integration
- Alembic database migrations
- OpenAPI (Swagger UI)
- Modular FastAPI architecture

---

## Planned Enterprise Features

The project roadmap includes implementation of:

- Docker
- Docker Compose
- Redis
- Celery
- Terraform
- Ansible
- Amazon Web Services (AWS)
- GitHub Actions
- Kubernetes
- Prometheus
- Grafana
- Loki
- Production Deployment

---

## Technology Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Database

- PostgreSQL
- Alembic

### Security

- JWT Authentication
- Passlib
- BCrypt

### DevOps

- Docker
- Docker Compose
- GitHub Actions

### Cloud

- Amazon Web Services (Planned)
- Terraform
- Ansible

### Container Orchestration

- Kubernetes

### Monitoring

- Prometheus
- Grafana
- Loki

### Version Control

- Git
- GitHub

---

## Project Structure

```text
CloudOps-ServiceDesk
│
├── app/
├── alembic/
├── database/
├── docs/
├── screenshots/
├── docker/
├── terraform/
├── kubernetes/
├── monitoring/
├── scripts/
├── tests/
├── requirements.txt
└── README.md
```

---

## Documentation

Comprehensive project documentation is available under:

```text
docs/
```

Documentation includes:

- Project Overview
- Requirements Specification
- Technology Stack
- System Architecture
- API Reference
- Authentication
- Ticket Lifecycle
- Database Design
- DevOps
- Infrastructure
- Deployment
- Enterprise Technologies
- Project Status
- Roadmap
- Screenshots
- Getting Started
- License

---

## Getting Started

Clone the repository.

```bash
git clone https://github.com/Jimokunbor/CloudOps-ServiceDesk.git
```

Navigate to the project.

```bash
cd CloudOps-ServiceDesk
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run database migrations.

```bash
alembic upgrade head
```

Start the application.

```bash
uvicorn app.main:app --reload
```

Open Swagger UI.

```text
http://127.0.0.1:8000/docs
```

---

## Development Roadmap

The project is being developed incrementally using milestone-based development.

Completed

- Backend Foundation
- Authentication
- Ticket Management
- Documentation

Upcoming

- Docker
- Docker Compose
- Redis
- Celery
- Terraform
- Ansible
- AWS
- GitHub Actions
- Kubernetes
- Monitoring
- Production Deployment

---

## License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

## Author

Developed by:

**Jim Okunbor**

Bachelor of Science (Honours) in Computing

Cloud Engineering | Backend Development | DevOps | Infrastructure Engineering