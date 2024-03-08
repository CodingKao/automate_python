### Day 15: # Exception Handling

# Enhance the script to include proper exception handling when performing file operations.

import os

def read_file(file_path):
    if os.path.exists(file_path):
        file = None
        content = None

        if os.access(file_path, os.R_OK):
            file = open(file_path, 'r')
            content = file.read()
        else:
            print(f"Error: Permission denied.  Unable to read from file {file_path}.")
        if file is not None:
            file.close()
        return content
    else:
        print(f"Error: File {file_path} not found.")
        return content
    
def write_file(file_path, content):