output "developer_user" {
  value = aws_iam_user.developer.name
}

output "security_user" {
  value = aws_iam_user.security.name
}