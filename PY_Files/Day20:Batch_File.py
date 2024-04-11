### Day 20: Batch File Renaming

### Write a script that renames all text files in the current directory to have a "prefix_" before their original names.

import os

def rename_text_files(prefix):
    files = os.listdir()
    for filename in files:
        if filename.endswith('.txt'):
            new_name = f"{prefix}_{filename}"
            if os.path.exists(new_name):
                print(f"Error: File '{new_name}' already exists.")
            else:
                os.rename(filename, new_name)

# Example usage
rename_text_files("prefix")
