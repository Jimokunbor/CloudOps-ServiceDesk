# Random Bucket Suffix

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

# Amazon S3 Bucket

resource "aws_s3_bucket" "project_storage" {
  bucket = "${local.project_name}-${random_id.bucket_suffix.hex}"

  tags = merge(
    local.common_tags,
    {
      Name = "${local.project_name}-storage"
    }
  )
}

# Bucket Ownership Controls

resource "aws_s3_bucket_ownership_controls" "project_storage" {
  bucket = aws_s3_bucket.project_storage.id

  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

# Block Public Access

resource "aws_s3_bucket_public_access_block" "project_storage" {
  bucket = aws_s3_bucket.project_storage.id

  block_public_acls       = true
  ignore_public_acls      = true
  block_public_policy     = true
  restrict_public_buckets = true
}

# Bucket Versioning

resource "aws_s3_bucket_versioning" "project_storage" {
  bucket = aws_s3_bucket.project_storage.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Server-Side Encryption

resource "aws_s3_bucket_server_side_encryption_configuration" "project_storage" {
  bucket = aws_s3_bucket.project_storage.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Lifecycle Configuration

resource "aws_s3_bucket_lifecycle_configuration" "project_storage" {
  bucket = aws_s3_bucket.project_storage.id

  rule {
    id     = "cleanup-old-versions"
    status = "Enabled"

    noncurrent_version_expiration {
      noncurrent_days = 30
    }
  }
}