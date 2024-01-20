# Day 3: File Reading
# Develop a function that reads and prints the contents of the "hello.txt" file

def read_and_print_file(file_name):
    file = open(file_name, 'r')
    content = file.read()
    print(content)
    file.close()

# File reading and printing 
file_name = "hello.txt"
read_and_print_file(file_name)