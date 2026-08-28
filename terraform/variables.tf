variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "eu-west-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "cloudops-servicedesk"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "development"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_1_cidr" {
  description = "CIDR block for Public Subnet 1"
  type        = string
  default     = "10.0.1.0/24"
}

variable "public_subnet_2_cidr" {
  description = "CIDR block for Public Subnet 2"
  type        = string
  default     = "10.0.2.0/24"
}

variable "private_subnet_1_cidr" {
  description = "CIDR block for Private Subnet 1"
  type        = string
  default     = "10.0.11.0/24"
}

variable "private_subnet_2_cidr" {
  description = "CIDR block for Private Subnet 2"
  type        = string
  default     = "10.0.12.0/24"
}

variable "availability_zone_1" {
  description = "Primary Availability Zone"
  type        = string
  default     = "eu-west-1a"
}

variable "availability_zone_2" {
  description = "Secondary Availability Zone"
  type        = string
  default     = "eu-west-1b"
}

variable "instance_type" {
  description = "EC2 instance type used by the Launch Template and Auto Scaling Group"
  type        = string
  default     = "t3.micro"
}

variable "key_pair_name" {
  description = "AWS EC2 Key Pair name"
  type        = string
  default     = "cloudops-servicedesk-key"
}

variable "db_instance_class" {
  description = "Amazon RDS instance class"
  type        = string
  default     = "db.t3.micro"
}

variable "db_allocated_storage" {
  description = "Initial storage allocated for PostgreSQL"
  type        = number
  default     = 20
}

variable "db_name" {
  description = "CloudOps ServiceDesk database name"
  type        = string
  default     = "cloudopsdb"
}

variable "db_username" {
  description = "Master username for PostgreSQL"
  type        = string
  default     = "cloudopsadmin"
}

variable "db_password" {
  description = "Master password for PostgreSQL"
  type        = string
  sensitive   = true
}