variable "aws_region"    { default = "eu-west-1" }
variable "project_name"  { default = "cicd-demo" }
variable "environment"   { default = "prod" }
variable "github_repo" {
  description = "GitHub repo in format owner/repo"
}