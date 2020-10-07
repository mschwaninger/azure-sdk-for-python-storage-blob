
import os
import uuid
import sys
from azure.storage.blob import BlockBlobService, PublicAccess
from datetime import datetime

# ---------------------------------------------------------------------------------------------------------
# Method that creates a test file in a folder.
# This sample application creates a test file, uploads the test file to the Blob storage,
# lists the blobs in the container, and downloads the file with a new name.
# ---------------------------------------------------------------------------------------------------------
# accountname: Azure storage account name
# accountkey: Access keys to authenticate your applications
# container_name: Container name aus dem storage account 
# ---------------------------------------------------------------------------------------------------------
# Documentation References:
# Associated Article - https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python
# What is a Storage Account - http://azure.microsoft.com/en-us/documentation/articles/storage-whatis-account/
# Getting Started with Blobs-https://docs.microsoft.com/en-us/azure/storage/blobs/storage-python-how-to-use-blob-storage
# Blob Service Concepts - http://msdn.microsoft.com/en-us/library/dd179376.aspx
# Blob Service REST API - http://msdn.microsoft.com/en-us/library/dd135733.aspx
# ----------------------------------------------------------------------------------------------------------

# Variable definition
accountname = '{azure_storage_account_name}' 
accountkey = '{ azure_access_keys}'
container_name = '{azure_container_name}'
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
dataformat = 'json'
filename = 'testdata'
path = '~\Documents'

try:
    # Create the BlockBlockService that the system uses to call the Blob service for the storage account.
    block_blob_service = BlockBlobService(account_name=accountname, account_key=accountkey)
    
    # Set the permission so the blobs are public.
    block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container) 

    # Create a file in Documents to test the upload and download.
    local_path = os.path.expanduser(path)
    local_file_name = filename + "-" + timestamp + "." + dataformat
    full_path_to_file = os.path.join(local_path, local_file_name)

    # Create a container if necessary.
    # container_name = 'testcontainer'
    # block_blob_service.create_container(container_name)    

    # Write some text to the file.
    file = open(full_path_to_file, 'w')
    file.write('"{ "name": "Georg","alter": 47,"verheiratet": false,"beruf": null,"kinder": [{ "name": "Lukas", "alter": 19, "schulabschluss": "Gymnasium" }, { "name": "Lisa", "alter": 14, "schulabschluss": null }] }"')
    file.close()

    # Upload the created file, use local_file_name for the blob name.
    block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)
except Exception as exep:
    print(exep)


