import boto3


def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    s3 = boto3.resource('s3')
    s3.Bucket(bucket).download_file(file_name, f"./downloads/{file_name}")
    return response