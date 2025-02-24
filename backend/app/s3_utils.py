import boto3
from botocore.client import Config

s3_client = boto3.client("s3", endpoint_url="http://localstack:4566", config=Config(signature_version="s3v4"))

def upload_to_s3(file, bucket="products-bucket", key="image"):
    s3_client.upload_fileobj(file, bucket, key)
    return f"http://localstack:4566/{bucket}/{key}"