# Getting Started

# 1. Introduction

This guide explains how to set up and run CloudOps ServiceDesk in a local development environment.

It is intended for developers, technical reviewers, recruiters and interviewers who want to explore the project, understand its architecture or contribute to its development.

The guide will continue to evolve as additional enterprise technologies, cloud-native services and production deployment environments are introduced throughout the project lifecycle.

---

# 2. Prerequisites

Before running the project, ensure the following software is installed.

| Software | Purpose |
|----------|---------|
| Git | Clone the repository |
| Python 3.12 or later | Backend development |
| Docker Desktop | Containerized application |
| Docker Compose | Multi-container orchestration |
| Visual Studio Code | Development environment |
| GitHub Desktop | Version control (optional) |
| Terraform | Infrastructure as Code (IaC) |
| AWS CLI | AWS authentication and infrastructure deployment |
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

# 6. Install Terraform and AWS CLI

CloudOps ServiceDesk uses Terraform for Infrastructure as Code (IaC) and the AWS CLI for authentication and cloud resource management.

## Verify Terraform Installation

```bash
terraform --version
```

## Verify AWS CLI Installation

```bash
aws --version
```

## Configure AWS Credentials

```bash
aws configure
```

Enter the following information when prompted.

- AWS Access Key ID
- AWS Secret Access Key
- Default Region (for example: eu-north-1)
- Default Output Format (json)

## Verify AWS Authentication

```bash
aws sts get-caller-identity
```

The command should return your AWS Account ID, User ID and IAM ARN.

---

# 7. Configure Environment Variables

Create a `.env` file in the project root.

Configure the application settings, database connection and authentication values.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@postgres:5432/cloudops_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ENVIRONMENT=development
DEBUG=True
```

---

# 8. Run the Application

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

The following services will start automatically.

- FastAPI
- PostgreSQL
- Redis
- Celery Worker
- Nginx

Application

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

Run the database migrations.

```bash
alembic upgrade head
```

Start the FastAPI application.

```bash
uvicorn app.main:app --reload
```

In a second terminal, start the Celery worker.

```bash
celery -A app.celery.celery_app worker --loglevel=info
```

Application

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

# 9. Verify the Installation

Confirm the following.

- Docker containers start successfully.
- FastAPI application starts successfully.
- PostgreSQL container is running.
- Redis container is running.
- Celery worker is running.
- Nginx reverse proxy is running.
- Docker Health Check reports the application as healthy.
- Structured application logging is working.
- Swagger UI loads successfully.
- Health endpoint returns a successful response.
- Redis connects successfully.
- Background tasks execute successfully.
- Artificial Intelligence endpoints are available in Swagger UI.
- AI service imports successfully during application startup.
- AI classification, summarization and priority recommendation endpoints execute successfully.
- User registration works.
- User login returns a JWT access token.
- Protected endpoints require authentication.
- Terraform is installed successfully.
- AWS CLI is installed successfully.
- AWS credentials are configured successfully.
- Terraform initializes successfully.
- Terraform validates successfully.
- Terraform formatting completes successfully.
- Terraform execution plan completes successfully.

---

# 10. Project Structure

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

# 11. Current Enterprise Stack

The project currently includes:

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT Authentication
- Role-Based Access Control (RBAC)
- Docker
- Docker Compose
- Redis
- Celery
- Nginx Reverse Proxy
- Docker Health Checks
- Structured Logging
- Environment Separation
- Enterprise Health API
- Artificial Intelligence Service Layer
- Ticket Classification API
- Ticket Summarization API
- Ticket Priority Recommendation API
- OpenAPI (Swagger)
- Terraform
- AWS CLI
- Infrastructure as Code (IaC)

---

# 12. Planned Enterprise Enhancements

The following capabilities will be introduced during future development milestones.

- Amazon Virtual Private Cloud (VPC)
- Public Subnets
- Private Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Groups
- EC2 Instances
- Application Load Balancer
- Amazon S3
- Amazon RDS PostgreSQL
- IAM Roles and Policies
- CloudWatch Logging
- Route 53
- AWS Certificate Manager (ACM)
- HTTPS Load Balancer
- Terraform Remote State
- Terraform Reusable Modules
- Ansible Configuration Management
- GitHub Actions Continuous Integration (CI)
- GitHub Actions Continuous Deployment (CD)
- Kubernetes Orchestration
- Amazon Web Services (AWS) Production Deployment
- Prometheus Monitoring
- Grafana Dashboards
- Loki Centralized Logging
- Production Deployment

---

# 13. Troubleshooting

Common issues include:

- Docker Desktop not running.
- Docker containers fail to start.
- PostgreSQL connection errors.
- Redis connection errors.
- Celery worker not starting.
- Docker Health Check reports an unhealthy container.
- Missing environment variables.
- Alembic migration conflicts.
- Missing Python dependencies.
- Terraform is not installed.
- AWS CLI is not installed.
- AWS credentials are not configured.
- Terraform validation errors.
- Terraform initialization errors.
- Port conflicts.

---

# 14. Related Documentation

- PROJECT_OVERVIEW.md
- REQUIREMENTS.md
- 16-AI-Integration.md
- 17-Project-Status.md
- 18-Roadmap.md
- 21-Screenshots.md

---

# 15. Revision History

| Version | Description |
|----------|-------------|
| 1.0 | Initial Getting Started guide created. |
| 1.1 | Added Docker Compose deployment instructions. |
| 1.2 | Added Enterprise Health API and Docker execution workflow. |
| 1.3 | Added Structured Logging, Environment Separation, Redis Integration and Celery Background Processing. |
| 1.4 | Added Artificial Intelligence Service Layer and AI API execution workflow. |
| 1.5 | Added Terraform installation, AWS CLI configuration, Infrastructure as Code (IaC) workflow, Terraform validation and AWS authentication setup. |

---

# 16. Document Status

Actively Maintained