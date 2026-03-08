cicd-pipeline-aws

A production-grade CI/CD pipeline that automatically lints, tests, builds, 
and deploys a containerised Flask API to AWS ECS Fargate on every push to 
main. The entire pipeline runs in under 3 minutes with zero manual steps.

 Project Structure
```
cicd-pipeline-aws/
├── app/
│   ├── backend/
│   │   ├── app.py              
│   │   ├── requirements.txt
│   │   └── Dockerfile          
│   └── frontend/
│       └── index.html
├── tests/
│   └── test_app.py            
├── terraform/
│   ├── main.tf                
│   ├── variables.tf
│   ├── outputs.tf
│   └── modules/
│       ├── networking/         
│       ├── ecr/                
│       ├── alb/               
│       └── ecs/                
└── .github/
    └── workflows/
        ├── ci.yml              
        └── cd.yml              
```

Deploy

cd terraform

terraform init

terraform apply -var="github_repo=YOUR_USERNAME/cicd-pipeline-aws"

terraform output next_steps

git push origin main


GitHub Secrets 

AWS_ROLE_ARN
AWS_REGION
ECR_REPOSITORY
ECS_CLUSTER
ECS_SERVICE
ECS_TASK_DEFINITION
ECS_CONTAINER_NAME
ALB_DNS_NAME

