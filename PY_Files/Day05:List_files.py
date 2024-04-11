import os

def list_files():
    # Get a list of all files in current directory
    files = os.listdir()

    # Print each file name
    for file in files:
        print(file)

# Call the function to list all files
list_files()