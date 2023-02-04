import boto3

# Create an S3 client
s3 = boto3.client('s3')

# List all of your S3 buckets
response = s3.list_buckets()

# Print the names of all buckets
for bucket in response['Buckets']:
    print(bucket['Name'])