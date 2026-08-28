# Store the database credentials

resource "aws_secretsmanager_secret" "database" {
  name        = "${local.project_name}-database-credentials"
  description = "Database credentials for CloudOps ServiceDesk"

  tags = {
    Name        = "${local.project_name}-database-secret"
    Environment = local.environment
    ManagedBy   = "Terraform"
  }
}

# Store the secret values

resource "aws_secretsmanager_secret_version" "database" {
  secret_id = aws_secretsmanager_secret.database.id

  secret_string = jsonencode({
    username = var.db_username
    password = var.db_password
  })
}