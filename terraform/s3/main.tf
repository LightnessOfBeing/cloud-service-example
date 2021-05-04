provider "aws" {
    region = "us-east-2"
    profile = "default"
}

resource "aws_s3_bucket" "my-app-bucket-kirill" {
    bucket = "my-app-bucket-kirill"
    acl    = "private"
}