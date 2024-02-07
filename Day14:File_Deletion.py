### Day 14: File Deletion
# Write a function that deletes the "hello.txt" file.

import os

def delete_file(file_path):
    # Check if the file exists before attempting to delete it
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"The file {file_path} has been deleted successfully.")
    else:
        print(f"The file {file_path} does not exist.")

# Specify the path to the 'hello.txt' file
file_path = "hello.txt"

# Call the function to delete the file
delete_file(file_path)

