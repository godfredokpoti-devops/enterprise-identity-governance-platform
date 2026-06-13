output "iam_role_name" {
  value = aws_iam_role.identity_admin.name
}

output "iam_policy_name" {
  value = aws_iam_policy.identity_policy.name
}