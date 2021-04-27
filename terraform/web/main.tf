provider "aws" {
    region = "us-east-2"
    profile = "kirill"
}

variable "name" {
    description = "Name the instance on deploy"
}

resource "aws_instance" "kirill_web" {
    ami = "ami-08962a4068733a2b6"
    instance_type = "t2.micro"
    key_name = "t2micro_ft"
    tags = {
        Name = "${var.name}"
    }
}