# Day 3: File Reading
# Develop a function that reads and prints the contents of the "hello.txt" file

# Define a function that reads and prints the contents of txt files
def read_and_print_files(hello_file, test_file):
    # Open the files in read mode
    hello = open(hello_file, 'r')
    test = open(test_file, 'r')

    # Read the contents of the files and store them in variables
    hello_content = hello.read()
    test_content = test.read()
    
    # Print the content of the files to the console
    print(hello_content)
    print(test_content)
    
    # Close the files 
    hello.close()
    test.close()

# File reading and printing 
hello_file = "hello.txt"
test_file = "test.txt"

# Call the function with the specified file names
read_and_print_files(hello_file, test_file)
