### Day 24: Basic File Operations with os.path

### Explore the `os.path` module and implement basic file operations like joining paths and checking file existence.

import os

# Join paths

path1 = "folder1"
path2 = "file.txt"
joined_path = os.path.join(path1, path2)
print("joined path:", joined_path)

# Check file existence
file_to_check = "file.txt"
if os.path.exists(file_to_check):
    print(f"File {file_to_check} exist.")
else:
    print(f"File {file_to_check} does not exist.:")