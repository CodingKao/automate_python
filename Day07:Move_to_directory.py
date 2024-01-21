import os

def create_directory(directory_name):
    # Check if the directory already exists
    if not os.path.exists(directory_name):
        # Create the new directory
        os.makedirs(directory_name)
        print(f"Directory {directory_name} created successfully.")
    else:
        print(f"Error: Directory {directory_name} already exists.")

# Directory creation
directory_name = "my_directory07"

# Call the function to create the directory
create_directory(directory_name)