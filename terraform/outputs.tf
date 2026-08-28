output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "web_server_public_ip" {
  description = "Web Server Public IP"
  value       = aws_instance.web_server_1.public_ip
}

output "application_url" {
  description = "CloudOps ServiceDesk URL"
  value       = "http://${aws_instance.web_server_1.public_ip}"
}

output "load_balancer_dns" {
  description = "Application Load Balancer DNS Name"
  value       = aws_lb.web_alb.dns_name

}

output "rds_endpoint" {
  description = "Amazon RDS Endpoint"
  value       = aws_db_instance.postgres.endpoint
}

output "rds_port" {
  description = "Amazon RDS Port"
  value       = aws_db_instance.postgres.port
}

output "rds_identifier" {
  description = "Amazon RDS Identifier"
  value       = aws_db_instance.postgres.identifier
}