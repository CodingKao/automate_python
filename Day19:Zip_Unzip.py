### Day 19: Zip and Unzip

### Develop functions to zip and unzip files using the `zipfile` module.

import zipfile
import os

def zip_files(zip_filename, files_to_zip):
    zip_file = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)

    for file_to_zip in files_to_zip:
        if os.path.exists(file_to_zip):
            zip_file.write(file_to_zip, os.path.basename(file_to_zip))
        else:
            print(f"Error: File '{file_to_zip}' not found.")
            zip_file.close()
            return
    
    zip_file.close()