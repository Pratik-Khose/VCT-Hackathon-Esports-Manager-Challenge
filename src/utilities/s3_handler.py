import boto3

s3_client = boto3.client("s3")

def upload_to_s3(bucket, faiss_key, pkl_key):
    faiss_path = "/tmp/valorant_csv_faiss.faiss"
    pkl_path = "/tmp/valorant_csv_faiss.pkl"
    
    s3_client.upload_file(Filename=faiss_path, Bucket=bucket, Key=faiss_key)
    s3_client.upload_file(Filename=pkl_path, Bucket=bucket, Key=pkl_key)

def download_from_s3(bucket, faiss_key, pkl_key):
    s3_client.download_file(Bucket=bucket, Key=faiss_key, Filename="/tmp/valorant_csv_faiss.faiss")
    s3_client.download_file(Bucket=bucket, Key=pkl_key, Filename="/tmp/valorant_csv_faiss.pkl")
