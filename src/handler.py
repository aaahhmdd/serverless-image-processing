import boto3
from utils import resize_image, watermark_image

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = f'/tmp/{key}'
        resized_path = f'/tmp/resized-{key}'
        watermarked_path = f'/tmp/watermarked-{key}'

        # Download original image
        s3.download_file(bucket, key, download_path)

        # Resize image
        resize_image(download_path, resized_path)

        # (Optional) Watermark image
        watermark_image(resized_path, watermarked_path)

        # Upload processed image
        target_bucket = bucket.replace('uploads', 'processed')
        s3.upload_file(watermarked_path, target_bucket, key)