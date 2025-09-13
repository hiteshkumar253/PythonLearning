# This script lists all files and directories in a specified directory.
# os module in Python provides a way of using operating system dependent functionality like reading or
# writing to the file system.


import os  # Importing the os module to interact with the operating system

# Specify the path to the directory you want to list
# Use '.' for current directory
directory_path = '.'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
print(f"Contents of directory '{directory_path}':")

print(contents)


