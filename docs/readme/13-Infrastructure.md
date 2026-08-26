# Infrastructure

## Introduction

CloudOps ServiceDesk is being developed within a secure, scalable and production-oriented Amazon Web Services (AWS) environment. The infrastructure is designed using modern cloud engineering principles to provide security, automation, scalability and operational reliability.

Infrastructure is provisioned using Infrastructure as Code (IaC) with Terraform, ensuring every cloud resource is deployed consistently, repeatably and through version-controlled configuration rather than manual creation.

---

# Infrastructure Objectives

The infrastructure has been designed to:

- Provide a secure cloud environment.
- Support scalable application deployment.
- Improve reliability and availability.
- Automate infrastructure provisioning.
- Simplify operational management.
- Support future enterprise expansion.
- Demonstrate modern cloud engineering and Infrastructure as Code (IaC) practices.

---

# Cloud Platform

## Amazon Web Services (AWS)

Amazon Web Services (AWS) provides the cloud platform for CloudOps ServiceDesk.

The current implementation provisions enterprise networking, compute resources and security using Terraform while preparing the platform for production deployment through additional AWS managed services.

---

# Current Infrastructure

The following infrastructure components have already been implemented.

## Networking

Current implementation includes:

- Amazon Virtual Private Cloud (VPC)
- Public Subnets
- Private Subnets
- Internet Gateway
- NAT Gateway
- Public Route Tables
- Private Route Tables
- Security Groups

Purpose

Provide secure, isolated and scalable network communication between cloud resources.

---

## Compute

Current implementation includes:

- Amazon EC2
- Apache Web Server
- EC2 User Data Automation

Purpose

Provide compute resources for hosting and validating the CloudOps ServiceDesk application within AWS.

---

## Identity and Access Management

Current implementation includes:

- IAM User
- IAM Role
- IAM Instance Profile

Purpose

Provide secure authentication and authorization for AWS resources while following the Principle of Least Privilege.

---

## Infrastructure as Code

Current implementation includes:

- Terraform Provider Configuration
- Variables
- Local Values
- Resource Tagging
- Infrastructure Planning
- Infrastructure Validation
- Infrastructure Provisioning

Purpose

Provision AWS infrastructure using reusable, version-controlled Infrastructure as Code.

---

# Planned Infrastructure Components

The following infrastructure components will be implemented during future development milestones.

## Load Balancing

- Application Load Balancer (ALB)

Purpose

Distribute incoming traffic across multiple application servers while improving scalability, availability and fault tolerance.

---

## Storage

- Amazon S3

Purpose

Store uploaded files, application assets, Terraform state (future) and backup resources.

---

## Database

- Amazon RDS PostgreSQL

Purpose

Provide a managed, scalable and highly available PostgreSQL database service.

---

## Monitoring

- Amazon CloudWatch
- Prometheus
- Grafana

Purpose

Collect infrastructure metrics, application metrics, logs and operational dashboards.

---

## Security

Future infrastructure security services include:

- AWS Certificate Manager (ACM)
- AWS WAF
- AWS Secrets Manager
- AWS Systems Manager Parameter Store
- AWS CloudTrail
- VPC Endpoints

Purpose

Improve cloud security, compliance, auditing and secure secret management.

---

## Container Platform

Future deployment will include:

- Docker
- Kubernetes
- Amazon Elastic Kubernetes Service (EKS)

Purpose

Support scalable container orchestration and production-ready application deployment.

---

# Infrastructure Automation

Infrastructure provisioning is automated using Terraform.

Terraform currently manages:

- AWS Provider
- Variables
- Local Values
- Amazon VPC
- Public Subnets
- Private Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Groups
- IAM Roles
- IAM Instance Profiles
- Amazon EC2
- Apache User Data provisioning

Future Terraform modules will provision:

- Application Load Balancer
- Amazon S3
- Amazon RDS
- Auto Scaling
- CloudWatch
- Route 53
- AWS Certificate Manager

This approach ensures infrastructure can be recreated consistently across development, testing and production environments.

---

# Infrastructure Security

The current infrastructure incorporates multiple security controls.

Current implementation includes:

- Virtual Private Cloud (VPC) isolation.
- Public and private subnet separation.
- Security Groups.
- IAM Roles.
- IAM Instance Profiles.
- EC2 User Data automation.
- IMDSv2 enforcement.
- Principle of Least Privilege.
- Infrastructure tagging.

Future security enhancements include:

- Private EC2 instances behind an Application Load Balancer.
- AWS WAF.
- HTTPS using AWS Certificate Manager.
- Secrets Manager.
- CloudTrail auditing.

---

# Scalability

The infrastructure has been designed to support future growth through:

- Application Load Balancer.
- Auto Scaling Groups.
- Kubernetes orchestration.
- Amazon Elastic Kubernetes Service (EKS).
- Containerized deployment.
- Modular Terraform architecture.
- Managed database services.

---

# Current Infrastructure Architecture

```text
                    Internet
                        │
                        ▼
                Internet Gateway
                        │
                        ▼
          Amazon Virtual Private Cloud
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
 Public Subnet                    Private Subnet
        │                               │
        ▼                               ▼
 Security Group                 NAT Gateway
        │
        ▼
 Amazon EC2
        │
        ▼
 Apache Web Server
```

The entire infrastructure is provisioned automatically using Terraform.

---

# Target Enterprise Infrastructure

```text
                    Internet
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
          ┌─────────────┴─────────────┐
          ▼                           ▼
     Amazon EC2                  Amazon EC2
    Auto Scaling Group      Auto Scaling Group
          │                           │
          └─────────────┬─────────────┘
                        ▼
                FastAPI Application
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
 Amazon RDS PostgreSQL             Amazon S3
                        │
                        ▼
                  CloudWatch
                        │
                        ▼
       Prometheus • Grafana • Loki
```

This architecture represents the production target for CloudOps ServiceDesk and provides a secure, scalable and highly available cloud-native platform.

---

# Related Documentation

- 04-Technology-Stack.md
- 05-System-Architecture.md
- 12-DevOps.md
- 14-Deployment.md

---

# Revision History

| Version | Description |
|----------|-------------|
| 1.0 | Initial infrastructure documentation created. |
| 1.1 | Added Terraform Infrastructure as Code (IaC), Amazon VPC, public and private networking, Internet Gateway, NAT Gateway, route tables, Security Groups, IAM, Amazon EC2 deployment, infrastructure automation and updated enterprise infrastructure roadmap. |

---

# Document Status

Actively Maintained