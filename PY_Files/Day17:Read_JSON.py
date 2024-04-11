# Day 17: Read and Write JSON

# Create a script that reads a JSON file, modifies its content, and writes it back to the file.

import json

def modify_and_write_json(file_path, modification_function):
    # Read JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Modify the content using the provided modification function
    modified_data = modification_function(data)

    # Write the modified content back to the same file
    with open(file_path, 'w') as file:
        json.dump(modified_data, file, indent=2)

def example_modification(data):
    # Modify the JSON data (Example: Add a new key-value pair)
    data['new_key'] = 'new_value'
    return data

# Specify the path to your JSON file
json_file_path = "example.json"

# Call the function to modify and write the JSON file
modify_and_write_json(json_file_path, example_modification)
