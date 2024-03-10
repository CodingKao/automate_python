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
    file = None
    if os.access(file_path, os.W_OK):
        file = open(file_path, 'W')
        file.write(content)
        print(f"File {file_path} successfully written.")
    else:
        print(f"Error: Permission denied.  Unable to write to file {file_path}.")
    if file is not None:
        file.close()

# Example usage
file_path = "example.txt"

# Read from File
file_content = read_file(file_path)

if file_content is not None:
    # Modify content
    modified_content = file_content + "\nNew line added."

    # Write back to file
    write_file(file_path, modified_content)