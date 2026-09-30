# AWS monthly cost budget for CloudOps ServiceDesk
resource "aws_budgets_budget" "cloudops_monthly_cost" {
  name         = "cloudops-servicedesk-monthly-budget"
  budget_type  = "COST"
  limit_amount = "10"
  limit_unit   = "USD"
  time_unit    = "MONTHLY"

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = 50
    threshold_type             = "PERCENTAGE"
    notification_type          = "FORECASTED"
    subscriber_email_addresses = ["jimokunbor88@gmail.com"]
  }

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = 80
    threshold_type             = "PERCENTAGE"
    notification_type          = "ACTUAL"
    subscriber_email_addresses = ["jimokunbor88@gmail.com"]
  }

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = 100
    threshold_type             = "PERCENTAGE"
    notification_type          = "ACTUAL"
    subscriber_email_addresses = ["jimokunbor88@gmail.com"]
  }

  tags = merge(
    local.common_tags,
    {
      Name = "cloudops-servicedesk-monthly-budget"
    }
  )
}