provider "aws" {
    region = "us-east-2"
    profile = "default"
}

variable "name" {
    description = "Name the instance on deploy"
}

resource "aws_instance" "default_jenkins" {
    ami = "ami-08962a4068733a2b6"
    instance_type = "t2.micro"
    key_name = "t2micro_ft"
    tags = {
        Name = "${var.name}"
    }
}