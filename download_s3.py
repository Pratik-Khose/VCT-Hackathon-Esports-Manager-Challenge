import os
import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Bucket name
bucket_name = 'vcthackathon-data'

# Function to download and rename files
def download_file_with_safe_name(bucket, key, download_path):
    # Replace colons with underscores in the filename
    safe_key = key.replace(':', '_')

    # Create the directory if it doesn't exist
    safe_path = os.path.join(download_path, safe_key)
    os.makedirs(os.path.dirname(safe_path), exist_ok=True)

    # Download the file
    print(f"Downloading {key} as {safe_key}")
    s3.download_file(bucket, key, safe_path)

# Function to list and download all files from the bucket
def download_all_files(bucket, download_path):
    # List all objects in the bucket
    s3_resource = boto3.resource('s3')
    bucket_obj = s3_resource.Bucket(bucket)

    for obj in bucket_obj.objects.all():
        download_file_with_safe_name(bucket, obj.key, download_path)

# Download all files to the specified local folder
download_all_files(bucket_name, './Data')
