# Day 3: File Reading
# Develop a function that reads and prints the contents of the "hello.txt" file

# Define a function that reads and prints the contents of a txt file
def read_and_print_file(file_name):
    # Open the file in read mode
    file = open(file_name, 'r')

    # Read the contents of the file and store it in variable
    content = file.read()
    
    # Print the content of the files to the console
    print(content)
    
    # Close the file 
    file.close()

# File reading and printing 
file_name = "hello.txt"

# Call the function with the specified file name
read_and_print_file(file_name)