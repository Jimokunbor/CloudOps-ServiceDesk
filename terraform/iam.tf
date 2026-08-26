data "aws_iam_policy_document" "ec2_assume_role" {
  statement {
    actions = [
      "sts:AssumeRole"
    ]

    principals {
      type = "Service"

      identifiers = [
        "ec2.amazonaws.com"
      ]
    }
  }
}

resource "aws_iam_role" "ec2_role" {
  name = "${local.project_name}-ec2-role"

  assume_role_policy = data.aws_iam_policy_document.ec2_assume_role.json

  tags = {
    Name        = "${local.project_name}-ec2-role"
    Environment = local.environment
    ManagedBy   = "Terraform"
  }
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "${local.project_name}-instance-profile"

  role = aws_iam_role.ec2_role.name

  tags = {
    Name        = "${local.project_name}-instance-profile"
    Environment = local.environment
    ManagedBy   = "Terraform"
  }
}