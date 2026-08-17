# Getting Started

# 1. Introduction

This guide explains how to set up and run CloudOps ServiceDesk in a local development environment.

It is intended for developers, technical reviewers, recruiters, and interviewers who want to explore the project, understand its architecture, or contribute to its development.

The guide will continue to evolve as additional technologies and deployment environments are introduced throughout the project lifecycle.

---

# 2. Prerequisites

Before running the project, ensure the following software is installed on your machine.

| Software | Purpose |
|----------|---------|
| Git | Clone the repository |
| Python 3.12 or later | Run the backend application |
| PostgreSQL 17 | Database server |
| Visual Studio Code | Development environment |
| pgAdmin 4 | Database management |
| GitHub Desktop | Version control (optional) |
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

Configure the database connection and JWT settings.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/cloudops_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# 7. Configure PostgreSQL

Create a PostgreSQL database named:

```text
cloudops_db
```

Run the Alembic migrations.

```bash
alembic upgrade head
```

---

# 8. Start the Application

Launch the FastAPI application.

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

# 9. Open the API Documentation

Swagger UI

```text
http://127.0.0.1:8000/docs
```

ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 10. Verify the Installation

Confirm the following:

- FastAPI starts successfully.
- PostgreSQL connects successfully.
- Alembic migrations complete successfully.
- Swagger UI loads correctly.
- User registration works.
- User login returns a JWT access token.
- Protected endpoints require authentication.

---

# 11. Project Structure

The project follows a modular enterprise architecture.

Key directories include:

- app/
- alembic/
- docs/
- screenshots/
- terraform/
- docker/
- kubernetes/
- monitoring/
- scripts/
- tests/

---

# 12. Planned Enterprise Enhancements

The following capabilities will be introduced during future development milestones.

- Docker containerization
- Docker Compose
- Redis
- Celery background processing
- Terraform infrastructure provisioning
- Ansible configuration management
- Amazon Web Services (AWS) deployment
- GitHub Actions CI/CD
- Kubernetes orchestration
- Prometheus monitoring
- Grafana dashboards
- Loki centralized logging
- Production deployment

---

# 13. Troubleshooting

Common issues include:

- Python virtual environment not activated.
- PostgreSQL service not running.
- Database connection errors.
- Missing environment variables.
- Alembic migration conflicts.
- Missing Python dependencies.

---

# 14. Related Documentation

- PROJECT_OVERVIEW.md
- REQUIREMENTS.md
- 16-Project-Status.md
- 17-Roadmap.md
- 18-Screenshots.md

---

# 15. Revision History

| Version | Description |
|----------|-------------|
| 1.0 | Initial Getting Started guide created. |

---

# 16. Document Status

Completed