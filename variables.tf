variable "region" {
  default = "ap-south-1"
}
variable "instance_type" {
  default = "t2.micro"
}
variable "key_name" {
  description = "EC2 Key Pair"
}
variable "bucket_name" {
  description = "S3 bucket for static website"
}

