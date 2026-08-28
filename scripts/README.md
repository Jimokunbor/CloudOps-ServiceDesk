# CloudOps ServiceDesk Scripts

## Overview

This directory contains automation scripts used to deploy, configure, monitor and maintain the CloudOps ServiceDesk infrastructure and application.

The scripts support Infrastructure as Code (Terraform), server configuration, application deployment, system administration, monitoring, backup and operational maintenance.

As the project evolves, additional scripts will be introduced to automate enterprise deployment, security and infrastructure management tasks.

---

# Current Scripts

## web_server.sh

### Purpose

Automatically configures a newly created Amazon EC2 instance during its first boot using Terraform User Data.

### Responsibilities

- Updates the Ubuntu operating system
- Installs the Apache Web Server
- Enables Apache to start automatically after reboot
- Starts the Apache service
- Deploys the CloudOps ServiceDesk landing page

### Used By

- Terraform EC2 Instance
- Terraform Launch Template
- Auto Scaling Group

### Why It Is Important to CloudOps ServiceDesk

This script automatically prepares every new EC2 instance with the required web server configuration, ensuring consistent deployments while eliminating manual server setup.

---

# Planned Scripts

## deploy_application.sh

### Purpose

Deploys the latest version of the CloudOps ServiceDesk application to the production web server.

### Why It Is Important to CloudOps ServiceDesk

Automates application deployment, making software updates faster, more reliable and consistent across all application servers.

---

## configure_ssm.sh

### Purpose

Registers Amazon EC2 instances with AWS Systems Manager (SSM) and configures secure remote administration.

### Why It Is Important to CloudOps ServiceDesk

Enables secure server management without requiring SSH access, improving operational security and simplifying infrastructure administration.

---

## install_cloudwatch_agent.sh

### Purpose

Installs and configures the Amazon CloudWatch Agent for centralized monitoring and log collection.

### Why It Is Important to CloudOps ServiceDesk

Provides continuous monitoring of infrastructure health, application performance and system logs, allowing issues to be identified and resolved quickly.

---

## backup_database.sh

### Purpose

Creates automated backups of the PostgreSQL database.

### Why It Is Important to CloudOps ServiceDesk

Protects critical application data by creating regular database backups that can be used for recovery after failures or accidental data loss.

---

## restore_database.sh

### Purpose

Restores PostgreSQL databases from previously created backups.

### Why It Is Important to CloudOps ServiceDesk

Supports disaster recovery by restoring application data quickly, reducing downtime and maintaining business continuity.

---

## health_check.sh

### Purpose

Performs automated health checks against the application, web server and supporting infrastructure.

### Why It Is Important to CloudOps ServiceDesk

Continuously verifies that application services are operating correctly, helping detect failures early and maintain a reliable production environment.

---

## cleanup.sh

### Purpose

Performs routine server maintenance by removing temporary files and unnecessary system data.

### Why It Is Important to CloudOps ServiceDesk

Maintains server performance, optimizes storage usage and keeps the operating system clean and efficient over time.

---

# Future Scripts

As additional AWS services are implemented, this directory may include automation scripts for:

- AWS Secrets Manager
- Amazon RDS PostgreSQL
- Amazon Route 53
- AWS Certificate Manager (ACM)
- VPC Endpoints
- VPC Peering
- AWS WAF
- Infrastructure validation
- Security hardening
- Disaster recovery
- Performance optimization

---

# Status

Actively Maintained