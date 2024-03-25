### Day 27: Recursive File Search

### Write a script that recursively searches for files with a specific extension in a directory.

import os

def search_files_with_extension(directory, extension, result=[]):
    if os.path.isdire(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                search_files_with_extension(item_path, extension, result)
            elif os.path.isfile(item_path) and item.endswith(extension):
                result.append(item_path)