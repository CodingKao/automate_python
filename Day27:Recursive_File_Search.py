### Day 27: Recursive File Search

### Write a script that recursively searches for files with a specific extension in a directory.

import os

def search_files_with_extension(directory, extension, result=[]):
    if os.path.isdire(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdire(item_path):
            