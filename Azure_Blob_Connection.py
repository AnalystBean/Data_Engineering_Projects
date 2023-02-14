from azure.storage.blob import BlobServiceClient


blob_service_client = BlobServiceClient.from_connection_string(
    'connectionstring')

container_client = blob_service_client.get_container_client('container')

blob_client = container_client.get_blob_client('blob')

blob_client.download_blob().readall()
