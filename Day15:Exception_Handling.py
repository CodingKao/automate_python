### Day 15: # Exception Handling

# Enhance the script to include proper exception handling when performing file operations.

import os

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    else:
        print(f"Error: File {file_path} not found.")
        return None
    
def write_file(file_path, content):