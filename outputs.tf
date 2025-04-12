output "instance_public_ip" {
  value = aws_instance.web.public_ip
}

output "s3_bucket_name" {
  value = aws_s3_bucket.static_site.bucket
}

output "lambda_function_name" {
  value = aws_lambda_function.s3_logger.function_name
}

