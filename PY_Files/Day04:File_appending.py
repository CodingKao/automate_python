# Day 4: File appending
# Modify the script to append a new line

def append_to_file(file_name, new_line):
    # Open the file in append (a) mode
    file = open(file_name, 'a')

    # Append new line to the file
    file.write(new_line + '\n')

    # Close the file
    file.close()

# File Appending
file_name = "hello.txt"
new_line = "Python is powerful!"

# Call the function
append_to_file(file_name, new_line)