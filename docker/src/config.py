import os

S3_BUCKET               = "my-app-bucket-kirill"
AWS_ACCESS_KEY_ID       = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY   = os.environ.get("AWS_SECRET_ACCESS_KEY")
S3_LOCATION             = f'http://{S3_BUCKET}.s3.amazonaws.com/'

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000