# Getting Started

# 1. Introduction

This guide explains how to set up and run CloudOps ServiceDesk in a local development environment.

It is intended for developers, technical reviewers, recruiters, and interviewers who want to explore the project, understand its architecture, or contribute to its development.

The guide will continue to evolve as additional enterprise technologies and cloud deployment environments are introduced throughout the project lifecycle.

---

# 2. Prerequisites

Before running the project, ensure the following software is installed on your machine.

| Software | Purpose |
|----------|---------|
| Git | Clone the repository |
| Python 3.12 or later | Backend development |
| Docker Desktop | Containerized application |
| Docker Compose | Multi-container orchestration |
| Visual Studio Code | Development environment |
| GitHub Desktop | Version control (optional) |
| pgAdmin 4 | Database administration (optional) |
| Postman | API testing (optional) |

---

# 3. Clone the Repository

Clone the repository from GitHub.

```bash
git clone https://github.com/Jimokunbor/CloudOps-ServiceDesk.git
```

Navigate into the project directory.

```bash
cd CloudOps-ServiceDesk
```

---

# 4. Create a Virtual Environment

Create a Python virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

---

# 5. Install Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

---

# 6. Configure Environment Variables

Create a `.env` file in the project root.

Configure the application settings, database connection and authentication values.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@postgres:5432/cloudops_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# 7. Run the Application

CloudOps ServiceDesk supports two execution methods.

## Option 1 — Docker Compose (Recommended)

Build the application.

```bash
docker compose build
```

Start all services.

```bash
docker compose up
```

This starts:

- FastAPI
- PostgreSQL
- Redis
- Nginx

The application will be available at:

```text
http://localhost
```

Swagger Documentation

```text
http://localhost/docs
```

Health Endpoint

```text
http://localhost/health/
```

---

## Option 2 — Local Development

Run database migrations.

```bash
alembic upgrade head
```

Start the FastAPI application.

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

Health Endpoint

```text
http://127.0.0.1:8000/health/
```

---

# 8. Verify the Installation

Confirm the following:

- Docker containers start successfully.
- FastAPI application starts successfully.
- PostgreSQL container is running.
- Redis container is running.
- Nginx reverse proxy is running.
- Swagger UI loads successfully.
- Health endpoint returns a successful response.
- User registration works.
- User login returns a JWT access token.
- Protected endpoints require authentication.

---

# 9. Project Structure

CloudOps ServiceDesk follows a modular enterprise architecture.

Key directories include:

- app/
- alembic/
- docker/
- docs/
- kubernetes/
- monitoring/
- scripts/
- terraform/
- tests/
- screenshots/

---

# 10. Current Enterprise Stack

The project currently includes:

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT Authentication
- Role-Based Access Control (RBAC)
- Docker
- Docker Compose
- Redis
- Nginx Reverse Proxy
- Enterprise Health API
- OpenAPI (Swagger)

---

# 11. Planned Enterprise Enhancements

The following capabilities will be introduced during future development milestones.

- Artificial Intelligence Integration
- Celery Background Processing
- Terraform Infrastructure Provisioning
- Ansible Configuration Management
- Amazon Web Services (AWS)
- GitHub Actions CI/CD
- Kubernetes Orchestration
- Prometheus Monitoring
- Grafana Dashboards
- Loki Centralized Logging
- Production Deployment

---

# 12. Troubleshooting

Common issues include:

- Docker Desktop not running.
- Docker containers fail to start.
- PostgreSQL connection errors.
- Missing environment variables.
- Alembic migration conflicts.
- Missing Python dependencies.
- Redis connection errors.
- Port conflicts.

---

# 13. Related Documentation

- PROJECT_OVERVIEW.md
- REQUIREMENTS.md
- 16-AI-Integration.md
- 17-Project-Status.md
- 18-Roadmap.md
- 21-Screenshots.md

---

# 14. Revision History

| Version | Description |
|----------|-------------|
| 1.0 | Initial Getting Started guide created. |
| 1.1 | Added Docker Compose deployment instructions. |
| 1.2 | Added Enterprise Health API and Docker execution workflow. |

---

# 15. Document Status

Actively Maintained