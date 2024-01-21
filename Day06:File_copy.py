# Create a script that copies the content of "hello.txt" to a new file named "hello_copy.txt".

def copy_file(source_file, destination_file):
    # Open the source file in read ('r) mode
    source = open(source_file, 'r')

    # Read the content of the source file
    content = source.read()

    # Clost the source file
    source.close()

    # Open the destination file in write mode
    destination = open(destination_file, 'w')

    # Write the content to the destination file
    destination.write(content)

    # Close the destination file
    destination.close()

    print(f"Content copied from {source_file} to {destination_file}")

# Source and destination files 
source_file = "hello.txt"
destination_file = "hello_copy.txt"

# Call the function to copy the content
copy_file(source_file, destination_file)

