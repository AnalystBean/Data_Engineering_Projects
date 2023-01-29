from azure.storage.blob import BlobServiceClient

# Create a blob service client
blob_service_client = BlobServiceClient.from_connection_string(
    'connectionstring')

# Get a container client
container_client = blob_service_client.get_container_client('container')

# Get a blob client
blob_client = container_client.get_blob_client('blob')

# Download the blob
blob_client.download_blob().readall()
