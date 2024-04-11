### Day 30: Capstone Project - Simple Automation Task

### Apply the skills learned in the past 29 days to automate a simple everyday task, such as organizing files, downloading data, or sending emails.

#Objective:
### Automate the organization of files by categorizing them into subdirectories based on their file extensions.

import os
import shutil

def organize_files(directory):
    # Create a dictionary to store file extensions and their corresponding subdirectories
    file_extensions = {}

    # Scan the directory and categorize files by extension
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_name, file_extension = os.path.splitext(file)
            if file_extension not in file_extensions:
                file_extensions[file_extension] = []
            file_extensions[file_extension].append(file)

    # Create subdirectories for each file extension
    for extension, files in file_extensions.items():
        subdirectory = os.path.join(directory, extension[1:].upper() + "_Files")
        os.makedirs(subdirectory, exist_ok=True)
        
        # Move files to their respective subdirectories
        for file in files:
            source = os.path.join(directory, file)
            destination = os.path.join(subdirectory, file)
            shutil.move(source, destination)
            print(f"Moved '{file}' to '{subdirectory}'")

if __name__ == "__main__":
    directory = "/home/kao/courses/Python-projects/automate_python" 
    organize_files(directory)