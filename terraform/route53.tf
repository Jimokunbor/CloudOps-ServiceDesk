# Create the Route 53 hosted zone

resource "aws_route53_zone" "main" {
  name = var.domain_name

  tags = merge(
    local.common_tags,
    {
      Name = "${local.project_name}-hosted-zone"
    }
  )
}

# Create the DNS record for the Application Load Balancer

resource "aws_route53_record" "application" {
  zone_id = aws_route53_zone.main.zone_id

  name = var.domain_name
  type = "A"

  alias {
    name                   = aws_lb.web_alb.dns_name
    zone_id                = aws_lb.web_alb.zone_id
    evaluate_target_health = true
  }
}