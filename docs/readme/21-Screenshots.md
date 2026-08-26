## 6.13 AI Module Import Verification

**Purpose**

Demonstrates successful integration of the Artificial Intelligence module into the CloudOps ServiceDesk application. The screenshot confirms that the AI service imports successfully without errors, verifying that the enterprise AI architecture has been correctly configured and is available for use by the application.

**Screenshot**

![AI Module Import Verification](../../screenshots/01-backend/17-ai-module-import-verification.png)

---

## 6.14 AI API Documentation

**Purpose**

Demonstrates successful registration of the Artificial Intelligence service within the automatically generated OpenAPI (Swagger UI) documentation. The screenshot confirms that the AI module exposes dedicated endpoints for ticket classification, ticket summarization and priority recommendation as part of the enterprise REST API.

**Screenshot**

![AI Swagger UI](../../screenshots/01-backend/18-ai-swagger-ui.png)

---

## 6.15 AI Runtime Verification

**Purpose**

Demonstrates successful runtime integration of the Artificial Intelligence service with the CloudOps ServiceDesk platform. The screenshot confirms that the FastAPI application, Celery worker and AI service initialize correctly during application startup, verifying that the AI service layer is fully operational within the enterprise application.

**Screenshot**

![AI Runtime Verification](../../screenshots/01-backend/19-ai-runtime-verification.png)

---

## 6.16 AI Service Testing

**Purpose**

Demonstrates successful testing of the CloudOps ServiceDesk Artificial Intelligence service through the Swagger UI. The screenshot confirms that the AI module is fully integrated into the application and exposes ticket classification, ticket summarization and priority recommendation endpoints. It also verifies successful execution of all three AI requests and their JSON responses, demonstrating that the internal AI service layer is operational and prepared for future integration with external Large Language Model (LLM) providers.

**Screenshot**

![AI Service Testing](../../screenshots/01-backend/20-ai-service-testing.png)

---

## 6.17 Terraform Project Structure

**Purpose**

Demonstrates the professional Terraform project structure adopted for the CloudOps ServiceDesk infrastructure. The screenshot confirms the organization of Terraform configuration files, reusable modules, environment directories and supporting scripts, following Infrastructure as Code (IaC) best practices for enterprise cloud deployments.

**Screenshot**

![Terraform Project Structure](../../screenshots/01-backend/21-terraform-project-structure.png)

---

## 6.18 Terraform Installation Verification

**Purpose**

Demonstrates successful installation and verification of Terraform on the local development environment. The screenshot confirms that Terraform is correctly installed and accessible from the command line, providing the foundation for infrastructure provisioning and management.

**Screenshot**

![Terraform Installation Verification](../../screenshots/01-backend/22-terraform-installation-verification.png)

---

## 6.19 AWS CLI Installation Verification

**Purpose**

Demonstrates successful installation and configuration of the AWS Command Line Interface (AWS CLI). The screenshot confirms that the AWS CLI is installed correctly and available for authenticating and interacting with AWS services from the local development environment.

**Screenshot**

![AWS CLI Installation Verification](../../screenshots/01-backend/23-aws-cli-installation-verification.png)

---

## 6.20 Terraform Initialization

**Purpose**

Demonstrates successful initialization of the Terraform working directory. The screenshot confirms that Terraform downloaded the required provider plugins, initialized the backend configuration and prepared the project for infrastructure provisioning.

**Screenshot**

![Terraform Initialization](../../screenshots/01-backend/24-terraform-initialization.png)

---

## 6.21 Terraform Validation

**Purpose**

Demonstrates successful validation of the Terraform configuration. The screenshot confirms that all Terraform configuration files are syntactically correct and free from validation errors, ensuring that the infrastructure definition is ready for planning and deployment.

**Screenshot**

![Terraform Validation](../../screenshots/01-backend/25-terraform-validation.png)

---

## 6.22 Terraform Formatting

**Purpose**

Demonstrates successful formatting of the Terraform configuration using HashiCorp's official formatting standard. The screenshot confirms that the infrastructure code follows a consistent and professional coding style across all Terraform configuration files.

**Screenshot**

![Terraform Formatting](../../screenshots/01-backend/26-terraform-formatting.png)

---

## 6.23 Terraform Execution Plan

**Purpose**

Demonstrates successful execution of the Terraform planning phase. The screenshot confirms that Terraform compared the current configuration with the AWS environment and generated an execution plan, verifying that the infrastructure state matches the configuration before deployment.

**Screenshot**

![Terraform Execution Plan](../../screenshots/01-backend/27-terraform-plan.png)

---

**## 6.24 Terraform Provider Verification**

**Purpose**

Demonstrates successful configuration and verification of the Terraform AWS provider. The screenshot confirms that Terraform is correctly configured to authenticate and communicate with Amazon Web Services, establishing the foundation for Infrastructure as Code (IaC) deployments.

**Screenshot**

![Terraform Provider Verification](../../screenshots/01-backend/28-terraform-provider-verification.png)

---

**## 6.25 Terraform Variables Verification**

**Purpose**

Demonstrates successful implementation of reusable Terraform input variables. The screenshot confirms that project configuration values have been centralized, improving infrastructure flexibility, consistency and maintainability across the CloudOps ServiceDesk project.

**Screenshot**

![Terraform Variables Verification](../../screenshots/01-backend/29-terraform-variables-verification.png)

---

**## 6.26 Terraform Local Values**

**Purpose**

Demonstrates successful implementation of Terraform local values. The screenshot confirms that reusable project naming conventions and common configuration values have been centralized, reducing code duplication while improving readability and maintainability.

**Screenshot**

![Terraform Local Values](../../screenshots/01-backend/30-terraform-local-values.png)

---

**## 6.27 Virtual Private Cloud (VPC) Terraform Plan**

**Purpose**

Demonstrates successful execution of the Terraform planning phase before deploying the Virtual Private Cloud (VPC). The screenshot confirms that Terraform identified the required networking resources and generated an execution plan for review prior to infrastructure deployment.

**Screenshot**

![Terraform VPC Plan](../../screenshots/01-backend/31-vpc-terraform-plan.png)

---

**## 6.28 Virtual Private Cloud (VPC) Deployment**

**Purpose**

Demonstrates successful deployment of the Virtual Private Cloud (VPC) using Terraform. The screenshot confirms that the networking infrastructure was provisioned successfully within the AWS environment.

**Screenshot**

![VPC Deployment Success](../../screenshots/01-backend/32-vpc-deployment-success.png)

---

**## 6.29 AWS VPC Verification**

**Purpose**

Demonstrates successful verification of the deployed Virtual Private Cloud within the AWS Management Console. The screenshot confirms that the VPC was created successfully with the expected configuration and is ready to host cloud infrastructure resources.

**Screenshot**

![AWS VPC Verification](../../screenshots/01-backend/33-vpc-aws-console-verification.png)

---

**## 6.30 VPC Resource Tags**

**Purpose**

Demonstrates successful implementation of standardized resource tagging for the Virtual Private Cloud. The screenshot confirms that consistent naming and tagging conventions have been applied to support infrastructure organization, governance and lifecycle management.

**Screenshot**

![VPC Resource Tags](../../screenshots/01-backend/34-vpc-resource-tags.png)

---

**## 6.31 Public Subnets Terraform Plan**

**Purpose**

Demonstrates successful execution of the Terraform planning phase before deploying the public subnets. The screenshot confirms that Terraform identified the required subnet resources and generated the expected infrastructure execution plan.

**Screenshot**

![Public Subnets Plan](../../screenshots/01-backend/35-public-subnets-plan.png)

---

**## 6.32 Public Subnets Deployment**

**Purpose**

Demonstrates successful deployment of the public subnets using Terraform. The screenshot confirms that the public networking infrastructure was provisioned successfully across multiple Availability Zones.

**Screenshot**

![Public Subnets Apply](../../screenshots/01-backend/36-public-subnets-apply.png)

---

**## 6.33 Public Subnet 1 Verification**

**Purpose**

Demonstrates successful verification of the first public subnet within the AWS Management Console. The screenshot confirms that the subnet has been created successfully with the expected network configuration.

**Screenshot**

![Public Subnet 1 Verification](../../screenshots/01-backend/37-public-subnet-1-aws-verification.png)

---

**## 6.34 Public Subnet 2 Verification**

**Purpose**

Demonstrates successful verification of the second public subnet within the AWS Management Console. The screenshot confirms that the subnet was provisioned successfully to provide high availability within the cloud infrastructure.

**Screenshot**

![Public Subnet 2 Verification](../../screenshots/01-backend/38-public-subnet-2-aws-verification.png)

---

**## 6.35 Private Subnets Terraform Plan**

**Purpose**

Demonstrates successful execution of the Terraform planning phase before deploying the private subnets. The screenshot confirms that Terraform generated the expected execution plan for the private networking infrastructure.

**Screenshot**

![Private Subnets Plan](../../screenshots/01-backend/39-private-subnets-plan.png)

---

**## 6.36 Private Subnets Deployment**

**Purpose**

Demonstrates successful deployment of the private subnets using Terraform. The screenshot confirms that isolated networking resources were provisioned successfully for secure backend services.

**Screenshot**

![Private Subnets Deployment](../../screenshots/01-backend/40-private-subnets-created.png)

---

**## 6.37 Private Subnet 1 Verification**

**Purpose**

Demonstrates successful verification of the first private subnet within the AWS Management Console. The screenshot confirms that the subnet was created successfully for hosting private infrastructure resources.

**Screenshot**

![Private Subnet 1 Verification](../../screenshots/01-backend/41-private-subnet-1.png)

---

**## 6.38 Private Subnet 2 Verification**

**Purpose**

Demonstrates successful verification of the second private subnet within the AWS Management Console. The screenshot confirms that the subnet was provisioned successfully to support highly available private workloads.

**Screenshot**

![Private Subnet 2 Verification](../../screenshots/01-backend/42-private-subnet-2.png)

---

**## 6.39 Internet Gateway Terraform Plan**

**Purpose**

Demonstrates successful execution of the Terraform planning phase before deploying the Internet Gateway. The screenshot confirms that Terraform identified the required internet connectivity resource prior to deployment.

**Screenshot**

![Internet Gateway Plan](../../screenshots/01-backend/43-internet-gateway-plan.png)

---

**## 6.40 Internet Gateway Deployment**

**Purpose**

Demonstrates successful deployment of the Internet Gateway using Terraform. The screenshot confirms that outbound internet connectivity was successfully established for public cloud resources.

**Screenshot**

![Internet Gateway Deployment](../../screenshots/01-backend/44-internet-gateway-created.png)

---

**## 6.41 Internet Gateway Verification**

**Purpose**

Demonstrates successful verification of the deployed Internet Gateway within the AWS Management Console. The screenshot confirms that the gateway has been correctly attached to the CloudOps ServiceDesk Virtual Private Cloud.

**Screenshot**

![Internet Gateway Verification](../../screenshots/01-backend/45-internet-gateway-verification.png)

---

**## 6.42 Public Route Table Terraform Plan**

**Purpose**

Demonstrates successful execution of the Terraform planning phase before deploying the public route table. The screenshot confirms that Terraform generated the expected routing configuration for internet-facing resources.

**Screenshot**

![Public Route Table Plan](../../screenshots/01-backend/46-public-route-table-terraform-plan.png)

---

**## 6.43 Public Route Table Deployment**

**Purpose**

Demonstrates successful deployment of the public route table using Terraform. The screenshot confirms that internet routing was configured successfully for the public subnets.

**Screenshot**

![Public Route Table Deployment](../../screenshots/01-backend/47-public-route-table-terraform-created.png)

---

**## 6.44 Public Route Table Verification**

**Purpose**

Demonstrates successful verification of the public route table within the AWS Management Console. The screenshot confirms that public routing has been configured correctly to support internet connectivity.

**Screenshot**

![Public Route Table Verification](../../screenshots/01-backend/48-public-route-table-verification.png)

---

**## 6.45 Private Route Table Terraform Plan**

**Purpose**

Demonstrates successful execution of the Terraform planning phase before deploying the private route table. The screenshot confirms that Terraform generated the required routing configuration for private network resources.

**Screenshot**

![Private Route Table Plan](../../screenshots/01-backend/49-terraform-private-route-table-plan.png)

---

**## 6.46 Private Route Table Deployment**

**Purpose**

Demonstrates successful deployment of the private route table using Terraform. The screenshot confirms that secure routing for private infrastructure resources was provisioned successfully.

**Screenshot**

![Private Route Table Deployment](../../screenshots/01-backend/50-terraform-private-route-table-apply.png)

---

**## 6.47 Private Route Table Verification**

**Purpose**

Demonstrates successful verification of the private route table within the AWS Management Console. The screenshot confirms that private routing has been configured correctly for isolated cloud resources.

**Screenshot**

![Private Route Table Verification](../../screenshots/01-backend/51-aws-private-route-table-verification.png)

---

**## 6.48 NAT Gateway Terraform Plan**

**Purpose**

Demonstrates successful execution of the Terraform planning phase before deploying the NAT Gateway. The screenshot confirms that Terraform identified the required outbound networking resources prior to deployment.

**Screenshot**

![NAT Gateway Plan](../../screenshots/01-backend/52-nat-gateway-terraform-plan.png)

---

**## 6.49 NAT Gateway Deployment**

**Purpose**

Demonstrates successful deployment of the NAT Gateway using Terraform. The screenshot confirms that secure outbound internet connectivity was successfully provisioned for resources located within the private subnets.

**Screenshot**

![NAT Gateway Deployment](../../screenshots/01-backend/53-nat-gateway-terraform-apply.png)

---

**## 6.50 NAT Gateway Verification**

**Purpose**

Demonstrates successful verification of the deployed NAT Gateway within the AWS Management Console. The screenshot confirms that the gateway is operational and ready to provide outbound internet access for private cloud resources.

**Screenshot**

![NAT Gateway Verification](../../screenshots/01-backend/54-nat-gateway-verification.png)

---

**## 6.51 Security Groups Terraform Plan**

**Purpose**

Demonstrates successful execution of the Terraform planning phase before deploying the Security Groups. The screenshot confirms that Terraform identified the required firewall rules protecting the cloud infrastructure.

**Screenshot**

![Security Groups Plan](../../screenshots/01-backend/55-terraform-security-groups-plan.png)

---

**## 6.52 Security Groups Deployment**

**Purpose**

Demonstrates successful deployment of the Security Groups using Terraform. The screenshot confirms that network access control rules were successfully provisioned for the CloudOps ServiceDesk infrastructure.

**Screenshot**

![Security Groups Deployment](../../screenshots/01-backend/56-terraform-security-groups-deployment.png)

---

**## 6.53 Web Security Group Verification**

**Purpose**

Demonstrates successful verification of the Web Server Security Group within the AWS Management Console. The screenshot confirms that the required inbound HTTP and SSH rules were configured correctly to allow secure administrative access and public web traffic.

**Screenshot**

![Web Security Group Verification](../../screenshots/01-backend/57-aws-web-security-group-verification.png)

---

**## 6.54 PostgreSQL Security Group Verification**

**Purpose**

Demonstrates successful verification of the PostgreSQL database Security Group within the AWS Management Console. The screenshot confirms that database connectivity has been restricted according to the planned infrastructure security design.

**Screenshot**

![PostgreSQL Security Group Verification](../../screenshots/01-backend/58-aws-postgresql-security-group-verification.png)

---

**## 6.55 AWS Security Groups Verification**

**Purpose**

Demonstrates successful verification of all deployed Security Groups within the AWS Management Console. The screenshot confirms that the infrastructure firewall configuration has been successfully applied across the CloudOps ServiceDesk environment.

**Screenshot**

![AWS Security Groups Verification](../../screenshots/01-backend/59-aws-all-security-group-verification.png)

---

**## 6.56 EC2 Deployment Terraform Plan**

**Purpose**

Demonstrates successful execution of the Terraform planning phase before deploying the Amazon EC2 web server. The screenshot confirms that Terraform generated the expected execution plan for the compute infrastructure.

**Screenshot**

![EC2 Deployment Plan](../../screenshots/01-backend/60-terraform-ec2-deployment-plan.png)

---

**## 6.57 EC2 Deployment**

**Purpose**

Demonstrates successful deployment of the Amazon EC2 web server using Terraform. The screenshot confirms that the compute instance, IAM role and associated cloud resources were provisioned successfully.

**Screenshot**

![EC2 Deployment Complete](../../screenshots/01-backend/61-terraform-ec2-deployment-complete.png)

---

**## 6.58 EC2 Web Server Verification**

**Purpose**

Demonstrates successful verification of the deployed EC2 web server within the AWS Management Console. The screenshot confirms that the instance is running successfully with the expected networking configuration, IAM role, security group and public connectivity.

**Screenshot**

![EC2 Web Server Verification](../../screenshots/01-backend/62-ec2-web-server-verification.png)

---

**## 6.59 CloudOps ServiceDesk Web Application Deployment**

**Purpose**

Demonstrates successful deployment of the CloudOps ServiceDesk web application on the Amazon EC2 web server. The screenshot confirms that Apache was configured successfully through Terraform User Data and automatically serves the CloudOps ServiceDesk landing page.

**Screenshot**

![CloudOps ServiceDesk Web Application](../../screenshots/01-backend/63-cloudops-servicedesk-web-application-deployment.png)

---

**## 6.60 CloudOps ServiceDesk Public Access Verification**

**Purpose**

Demonstrates successful end-to-end deployment of the CloudOps ServiceDesk infrastructure. The screenshot confirms that the application is publicly accessible through the EC2 public IP address, validating the successful configuration of the VPC, public subnet, Internet Gateway, route tables, Security Groups, EC2 instance, Apache web server and Terraform Infrastructure as Code deployment.

**Screenshot**

![CloudOps ServiceDesk Public Access Verification](../../screenshots/01-backend/64-cloudops-servicedesk-web-application-public-access.png)

---

**## 6.61 Ansible**

**Purpose**

Demonstrates automated infrastructure configuration, software provisioning and server management using Ansible to ensure consistent and repeatable deployments across the CloudOps ServiceDesk environment.

**Screenshot**

*To be added after implementation.*

---

**## 6.62 GitHub Actions**

**Purpose**

Demonstrates Continuous Integration (CI) workflow automation using GitHub Actions for infrastructure validation, application testing and deployment pipelines.

**Screenshot**

*To be added after implementation.*

---

**## 6.63 Kubernetes**

**Purpose**

Demonstrates container orchestration and application deployment using Kubernetes, providing automated scaling, self-healing and high availability for the CloudOps ServiceDesk platform.

**Screenshot**

*To be added after implementation.*

---

**## 6.64 AWS Production Infrastructure**

**Purpose**

Demonstrates the complete production deployment of the CloudOps ServiceDesk infrastructure within Amazon Web Services, including networking, compute, storage, security, monitoring and application services.

**Screenshot**

*To be added after implementation.*

---

**## 6.65 Prometheus**

**Purpose**

Demonstrates infrastructure and application metrics collection using Prometheus for performance monitoring and operational visibility.

**Screenshot**

*To be added after implementation.*

---

**## 6.66 Grafana**

**Purpose**

Demonstrates infrastructure and application dashboard visualization using Grafana, providing real-time monitoring, performance analysis and operational reporting.

**Screenshot**

*To be added after implementation.*

---

**## 6.67 Loki**

**Purpose**

Demonstrates centralized log aggregation, storage and visualization using Loki for infrastructure and application log analysis.

**Screenshot**

*To be added after implementation.*

---

**## 6.68 Production Deployment**

**Purpose**

Demonstrates the completed production deployment of the CloudOps ServiceDesk platform, validating the successful integration of all infrastructure, application and DevOps components within the enterprise cloud environment.

**Screenshot**

*To be added after implementation.*

---

# 7. Screenshot Standards

Every screenshot included in this document should:

- Be clear, readable and high resolution.

- Display only the relevant implementation or completed feature.

- Follow the project's screenshot naming convention.

- Reflect the latest implementation.

- Include a short purpose describing what the screenshot demonstrates.

- Be captured after successful execution or deployment.

- Exclude sensitive information such as passwords, tokens and secret keys.

---

# 8. Related Documentation

- 17-Project-Status.md

- 18-Roadmap.md

- 19-Getting-Started.md

---

# 9. Revision History

| Version | Description |
|----------|-------------|
| 1.0 | Initial screenshots documentation created. |
| 1.1 | Backend Foundation screenshots added. |
| 1.2 | Added Docker Compose, Docker Desktop, PostgreSQL database, Swagger through Nginx and Nginx reverse proxy screenshots. |
| 1.3 | Added Health API documentation and FastAPI Health Endpoint screenshots. |
| 1.4 | Added Docker Health Check, Structured Logging, Environment Configuration, Redis Integration, Celery Background Processing and Docker Multi-Container Platform screenshots. |
| 1.5 | Added AI Module Import Verification, AI API Documentation, AI Runtime Verification and AI Service Testing screenshots. |
| 1.6 | Added Terraform Project Structure, Terraform Installation Verification, AWS CLI Installation Verification, Terraform Initialization, Terraform Validation, Terraform Formatting and Terraform Execution Plan screenshots. |
| 1.7 | Added Terraform Provider configuration, Terraform variables, local values, Virtual Private Cloud (VPC), public and private subnets, Internet Gateway, NAT Gateway, public and private route tables, Security Groups, Amazon EC2 deployment and CloudOps ServiceDesk web application deployment screenshots. |

---

# 10. Document Status

Actively Maintained