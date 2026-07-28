# Requirements Specification

## 1. Introduction

This document defines the functional and non-functional requirements for the CloudOps ServiceDesk platform.

The purpose of the platform is to provide a secure, cloud-native IT Service Management (ITSM) system that demonstrates modern software engineering, cloud engineering, and DevOps practices.

---

# 2. Functional Requirements

The application shall allow users to:

- Register an account.
- Log in securely.
- Reset forgotten passwords.
- Create IT support tickets.
- View submitted tickets.
- Update ticket information.
- Close completed tickets.
- Search tickets.
- Upload supporting files.
- View ticket history.

Administrators shall be able to:

- Manage users.
- Assign support tickets.
- Change ticket priorities.
- Manage ticket categories.
- View system reports.
- View application metrics.
- Manage user roles.

---

# 3. Non-Functional Requirements

The application shall:

- Be secure.
- Be scalable.
- Be containerized.
- Support cloud deployment.
- Be monitored continuously.
- Use Infrastructure as Code.
- Support CI/CD deployment.
- Follow REST API standards.
- Be documented.
- Support automated testing.

---

# 4. User Roles

Guest

- Register
- Log in

User

- Create tickets
- View tickets
- Update own tickets

Administrator

- Manage users
- Assign tickets
- Manage the system
- View reports
- Configure application settings

---

# 5. Success Criteria

The project will be considered complete when:

- All core features are implemented.
- The application runs successfully in Docker.
- The application is deployed to Azure Kubernetes Service (AKS).
- Infrastructure is provisioned using Terraform.
- CI/CD is automated with GitHub Actions.
- Monitoring is available through Prometheus and Grafana.