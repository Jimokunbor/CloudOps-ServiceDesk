resource "aws_instance" "web_server_1" {
  ami           = "ami-08c7a4b4f234dfa77"
  instance_type = "t3.micro"

  subnet_id = aws_subnet.public_1.id

  vpc_security_group_ids = [
    aws_security_group.web.id
  ]

  iam_instance_profile = aws_iam_instance_profile.ec2_profile.name

  associate_public_ip_address = true

  metadata_options {
    http_endpoint = "enabled"
    http_tokens   = "required"
  }

  user_data = file("${path.module}/scripts/web_server.sh")

  tags = {
    Name        = "${local.project_name}-web-server-1"
    Environment = local.environment
    ManagedBy   = "Terraform"
  }
}