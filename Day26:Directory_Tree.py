### Day 26: Directory Tree

### Create a function that prints the directory tree structure of a given path.

import os

def directory_tree(path, indent=''):
    if os.path.isdir(path):
        print(indent + os.path.basename(path) + '/')
        indent += '  '
        for item in os.listdir(path):
            directory_tree(os.path.join(path, item), indent)
    elif os.path.isfile(path):
        print(indent + os.path.basename(path))

# Call the function
directory_tree('/path/to/directory')