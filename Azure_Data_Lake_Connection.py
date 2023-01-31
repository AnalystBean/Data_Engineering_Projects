from azure.storage.file import FileService

# Create a file service object
file_service = FileService(account_name='',
                           account_key='')

# Download a file
file_service.get_file_to_text('filesharename',
                              'directoryname',
                              'filename',
                              'path/to/local/file')