import os

# Specify the path to the directory you want to list
# Use '.' for current directory
directory_path = '.'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
print(f"Contents of directory '{directory_path}':")

print(contents)


