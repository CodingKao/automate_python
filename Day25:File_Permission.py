### Day 25: File Permissions

### Develop a script that prints the permissions (read, write, execute) of a specified file.

import os
import stat

def file_permissions(file_path):
    if os.path.exists(file_path):
        file_stat = os.stat(file_path)
        permissions = stat.S_IMODE(file_stat.st_mode)
        print("File permissions for", file_path, ":")
        print("Readable:", bool(permissions & stat.S_IRUSR))
        print("Writable:", bool(permissions & stat.S_IWUSR))
        print("Executable:", bool(permissions & stat.S_IXUSR))
    else:
        print(f"Error: File '{file_path}' not found.")

# Usage
file_permissions("example.txt")