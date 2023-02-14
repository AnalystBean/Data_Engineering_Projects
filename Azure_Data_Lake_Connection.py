from azure.storage.file import FileService


file_service = FileService(account_name='',
                           account_key='')


file_service.get_file_to_text('filesharename',
                              'directoryname',
                              'filename',
                              'path/to/local/file')