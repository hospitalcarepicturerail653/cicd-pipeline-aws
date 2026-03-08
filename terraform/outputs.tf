output "alb_dns_name"              { value = module.alb.dns_name }
output "ecr_repository_url"        { value = module.ecr.repository_url }
output "ecs_cluster_name"          { value = module.ecs.cluster_name }
output "ecs_service_name"          { value = module.ecs.service_name }
output "ecs_task_definition_family" { value = module.ecs.task_definition_family }
output "github_actions_role_arn"   { value = aws_iam_role.github_actions.arn }

output "next_steps" {
  value = <<-EOT
    Add these as GitHub Secrets:
    AWS_ROLE_ARN        = ${aws_iam_role.github_actions.arn}
    AWS_REGION          = ${var.aws_region}
    ECR_REPOSITORY      = ${module.ecr.repository_url}
    ECS_CLUSTER         = ${module.ecs.cluster_name}
    ECS_SERVICE         = ${module.ecs.service_name}
    ECS_TASK_DEFINITION = ${module.ecs.task_definition_family}
    ECS_CONTAINER_NAME  = flask-api
    ALB_DNS_NAME        = ${module.alb.dns_name}
  EOT
}