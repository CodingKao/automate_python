# Day 2: File Creattion
# Write a script that creates a new text file name "hello.txt" and writes "Hello, Python!" into it.

# Defind a function 
def create_and_write_file(file_name, content):
    # Open the file name 'file_name' in write ('w') mode
    file = open(file_name, 'w')

    # Write the specified content into the file
    file.write(content)

    # Close the file to ensure proper handling
    file.close()

    # Print message to indicate file has been created
    print(f"File '{file_name}' created successfully.")

# File creation with content
# Define the file name as "hello.txt"
file_name = "hello.txt"

# Define the content to be written into the file as "hello, Python!"
file_content = "hello, Python!"

# Call the function with the specified file name and content
create_and_write_file(file_name, file_content)