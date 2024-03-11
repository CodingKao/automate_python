### Day 17: Read and Write JSON

## Create a script that reads a JSON file, modifies its content, and writes it back to the file.

import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def modify_and_write_json(file_path, modification_function):
    data = read_json(file_path)

    if data is not None:
        modified_data = modification_function(data)
        write_json(file_path, modified_data)
        print(f"File {file_path} successfully modified and written.")
    else:
        print(f"Error: Failed to read JSON file {file_path}.")

# Example modification function
def example_modification(data):
    # Modify the JSON data 
    data['new_key'] = 'new_value'
    return data

# Specify the path to your JSON file
json_file_path = "example.json"

# Call the function to modify and write the JSON file
modify_and_write_json(json_file_path, example_modification)