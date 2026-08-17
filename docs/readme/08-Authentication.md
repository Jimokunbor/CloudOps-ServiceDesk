# Authentication

## Introduction

Authentication and authorization are fundamental security components of CloudOps ServiceDesk. They ensure that only verified users can access protected resources while restricting operations according to assigned roles.

The platform uses modern authentication standards that are widely adopted in enterprise backend applications.

---

# Objectives

The authentication system has been designed to:

- Verify user identity.
- Protect application resources.
- Secure API endpoints.
- Enforce Role-Based Access Control (RBAC).
- Prevent unauthorised access.
- Support future enterprise security enhancements.

---

# Authentication Architecture

The authentication process follows the workflow below.

```text
User Login
      │
      ▼
Credential Validation
      │
      ▼
Password Verification
      │
      ▼
JWT Token Generation
      │
      ▼
Bearer Token
      │
      ▼
Protected API Endpoint
```

Every protected request must include a valid JWT Bearer Token.

---

# Current Implementation

The following authentication features are currently implemented.

## User Registration

The platform allows new users to register by providing:

- Full Name
- Email Address
- Password

Passwords are securely hashed before being stored in the database.

---

## User Login

Registered users authenticate using:

- Email Address
- Password

Successful authentication returns a JWT access token.

---

## Password Security

User passwords are protected using:

- Passlib
- Bcrypt password hashing

Plain-text passwords are never stored.

---

## JWT Authentication

The platform currently uses JSON Web Tokens (JWT) for stateless authentication.

JWT tokens are issued after successful login and must accompany all protected API requests.

---

## OAuth2

CloudOps ServiceDesk implements OAuth2 Password Flow to authenticate users through FastAPI's security framework.

---

## Role-Based Access Control (RBAC)

The platform currently supports:

- Administrator
- Technician

Each protected endpoint validates the authenticated user's role before allowing access.

---

# Authentication Technologies

| Technology | Purpose |
|------------|---------|
| JWT | Stateless authentication |
| OAuth2 | Authentication framework |
| Passlib | Password hashing |
| Bcrypt | Secure password encryption |
| FastAPI Security | Authentication dependencies |

---

# Current Protected Endpoints

Current protected endpoints include:

Authentication

- /auth/me
- /auth/admin

Tickets

- Create Ticket
- View Tickets
- Update Ticket
- Delete Ticket
- Assign Ticket
- Update Ticket Status
- Dashboard Summary

---

# Security Principles

The authentication system follows these principles:

- Least Privilege
- Secure Password Storage
- Stateless Authentication
- Endpoint Protection
- Role Validation
- Separation of Authentication and Authorization

---

# Enterprise Roadmap

Future security improvements include:

- Refresh Tokens
- Password Reset
- Multi-Factor Authentication (MFA)
- Single Sign-On (SSO)
- Login History
- Session Management
- Account Lockout
- Security Audit Logging

---

# Related Documentation

- 04-Technology-Stack.md
- 05-System-Architecture.md
- 07-API-Reference.md
- 11-Security.md

---

# Revision History

| Version | Description |
|----------|-------------|
| 1.0 | Initial authentication documentation. |

---

# Document Status

Draft