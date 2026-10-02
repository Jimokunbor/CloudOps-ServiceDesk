output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "web_server_public_ip" {
  description = "Web Server Public IP"
  value       = var.enable_standalone_ec2 ? aws_instance.web_server_1[0].public_ip : null
}

output "application_url" {
  description = "CloudOps ServiceDesk URL"
  value       = var.enable_standalone_ec2 ? "http://${aws_instance.web_server_1[0].public_ip}" : null
}

output "load_balancer_dns" {
  description = "Application Load Balancer DNS Name"
  value       = var.enable_load_balancer ? aws_lb.web_alb[0].dns_name : null
}

output "rds_endpoint" {
  description = "Amazon RDS Endpoint"
  value       = var.enable_rds ? aws_db_instance.postgres[0].endpoint : null
}

output "rds_port" {
  description = "Amazon RDS Port"
  value       = var.enable_rds ? aws_db_instance.postgres[0].port : null
}

output "rds_identifier" {
  description = "Amazon RDS Identifier"
  value       = var.enable_rds ? aws_db_instance.postgres[0].identifier : null
}