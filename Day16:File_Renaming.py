### Day 16: File Renaming

## Develop a function to rename the "hello_copy.txt" file to "greetings.txt".

import os

def rename_file():
    old_file_name = "hello_copy.txt"
    new_file_name ="greetings.txt"

    # Check if the file exists before renaming
    if os.path.isfile(old_file_name):
        os.rename(old_file_name, new_file_name)
        print(f"File renamed succcessfully from {old_file_name} to {new_file_name}")
    else:
        print(f"Error:  File {old_file_name} does not exist.")

# Call the function to rename the file
rename_file()