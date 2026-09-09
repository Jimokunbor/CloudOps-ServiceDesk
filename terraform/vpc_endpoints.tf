# Allow private access to Amazon S3

resource "aws_vpc_endpoint" "s3" {
  vpc_id = aws_vpc.main.id

  service_name = "com.amazonaws.${var.aws_region}.s3"

  vpc_endpoint_type = "Gateway"

  route_table_ids = [
    aws_route_table.private.id
  ]

  tags = merge(
    local.common_tags,
    {
      Name = "${local.project_name}-s3-endpoint"
    }
  )
}