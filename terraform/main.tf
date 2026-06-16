provider "aws" {
  region = "us-east-1"
}

resource "aws_iam_user" "developer" {
  name = "john.doe"
}

resource "aws_iam_user" "security" {
  name = "sarah.smith"
}

resource "aws_iam_group" "developers" {
  name = "Developers"
}

resource "aws_iam_group" "security_team" {
  name = "Security-Team"
}