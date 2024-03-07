# Day 17: Read and Write JSON

# Create a script that reads a JSON file, modifies its content, and writes it back to the file.

import json

def modify_and_write_json(file_path, modification_function):
    # Read JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)