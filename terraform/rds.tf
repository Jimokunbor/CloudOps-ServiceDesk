# Database Subnet Group

resource "aws_db_subnet_group" "postgres" {
  name = "${local.project_name}-db-subnet-group"

  subnet_ids = [
    aws_subnet.private_1.id,
    aws_subnet.private_2.id
  ]

  tags = merge(
    local.common_tags,
    {
      Name = "${local.project_name}-db-subnet-group"
    }
  )
}

# Amazon RDS PostgreSQL

resource "aws_db_instance" "postgres" {
  identifier = "${local.project_name}-postgres"

  engine         = "postgres"
  engine_version = "17.5"
  instance_class = var.db_instance_class

  allocated_storage     = var.db_allocated_storage
  max_allocated_storage = 100
  storage_type          = "gp3"
  storage_encrypted     = true

  db_name  = var.db_name
  username = var.db_username
  password = var.db_password

  port = 5432

  publicly_accessible = false
  multi_az            = false

  db_subnet_group_name = aws_db_subnet_group.postgres.name

  vpc_security_group_ids = [
    aws_security_group.rds.id
  ]

  backup_retention_period = 1
  deletion_protection     = false
  skip_final_snapshot     = true

  apply_immediately = true

  lifecycle {
    ignore_changes = [
      password
    ]
  }

  tags = merge(
    local.common_tags,
    {
      Name = "${local.project_name}-postgres"
    }
  )
}