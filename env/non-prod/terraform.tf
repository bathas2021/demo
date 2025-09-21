provider "aws" {
  region = "us-east-1"
}

resource "aws_ecr_repository" "my_repo" {
  name = "my-app-repo"

  image_scanning_configuration {
    scan_on_push = true
  }

  image_tag_mutability = "MUTABLE"
}


