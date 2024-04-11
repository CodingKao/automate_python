### Day 21: Calculate File Size

## Create a function that calculates and prints the size of a given file.

import os

def get_file_size(file_path):
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        print(f"The size of '{file_path}' is {size} byttes.")
    else:
        print(f"Error: '{file_path}; not found.")

# Put in practice
get_file_size("prefix_example.txt")