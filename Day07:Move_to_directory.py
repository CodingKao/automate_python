import os

def create_directory(directory_name):
    # Check if the directory already exists
    if not os.path.exists(directory_name):
        # Create the new directory
        os.makedirs(directory_name)
        print(f"Directory {directory_name} created successfully.")