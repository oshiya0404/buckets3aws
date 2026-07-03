import boto3

s3 = boto3.client("s3", region_name="ca-central-1")

url = s3.generate_presigned_url(
    "get_object",
    Params={
        "Bucket": "oshiyas3",
        "Key": "notes/EECS3404_Week09A_CNN.pdf"
    },
    ExpiresIn=300,
)

print(url)