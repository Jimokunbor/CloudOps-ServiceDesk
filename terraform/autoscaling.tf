# Launch Template

resource "aws_launch_template" "web" {
  name_prefix   = "${local.project_name}-lt-"
  image_id      = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  key_name = var.key_pair_name

  vpc_security_group_ids = [
    aws_security_group.web.id
  ]

  iam_instance_profile {
    name = aws_iam_instance_profile.ec2_profile.name
  }

  user_data = base64encode(file("${path.module}/scripts/web_server.sh"))

  tag_specifications {
    resource_type = "instance"

    tags = merge(
      local.common_tags,
      {
        Name = "${local.project_name}-web-server"
      }
    )
  }

  tags = merge(
    local.common_tags,
    {
      Name = "${local.project_name}-launch-template"
    }
  )
}

# Auto Scaling Group

resource "aws_autoscaling_group" "web" {
  name = "${local.project_name}-asg"

  min_size         = 2
  desired_capacity = 2
  max_size         = 4

  vpc_zone_identifier = [
    aws_subnet.public_1.id,
    aws_subnet.public_2.id
  ]

  target_group_arns = [
    aws_lb_target_group.web_tg.arn
  ]

  health_check_type         = "ELB"
  health_check_grace_period = 300

  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }

  tag {
    key                 = "Name"
    value               = "${local.project_name}-web-server"
    propagate_at_launch = true
  }

  tag {
    key                 = "Project"
    value               = local.project_name
    propagate_at_launch = true
  }

  tag {
    key                 = "Environment"
    value               = var.environment
    propagate_at_launch = true
  }

  tag {
    key                 = "ManagedBy"
    value               = "Terraform"
    propagate_at_launch = true
  }
}