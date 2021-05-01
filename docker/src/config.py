import boto3

session = boto3.Session()
credentials = session.get_credentials()

credentials = credentials.get_frozen_credentials()
AWS_ACCESS_KEY_ID = credentials.access_key
AWS_SECRET_ACCESS_KEY = credentials.secret_key

S3_BUCKET               = "my-app-bucket-kirill"
S3_LOCATION             = f'http://{S3_BUCKET}.s3.amazonaws.com/'
print(AWS_ACESS_KEY_ID, AWS_SECRET_ACCESS_KEY)