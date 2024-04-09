### Day 30: Capstone Project - Simple Automation Task

### Apply the skills learned in the past 29 days to automate a simple everyday task, such as organizing files, downloading data, or sending emails.

#Objective:
### Automate the organization of files by categorizing them into subdirectories based on their file extensions.

import os
import shutil

def organize_file(directory):
    # Create a dictionary to store file extensions 
    file_extensions = {}

    # Scan directory and categorize files 
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_name, file_extension = os.path.split(file)
            if file_extension not in file_extensions:
                file_extensions[file_extension] = []
            file_extensions[file_extension].append(file)

    # Create subdirectories for each file extension
    for extension, files in file_extension.items():