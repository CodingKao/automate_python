# ### Day 7: Directory Creation
# Develop a function that creates a new directory named "my_directory".

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
directory_name = "my_directory"

# Call function
create_directory(directory_name)