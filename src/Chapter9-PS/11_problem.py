with open("old.txt", "r") as file:
    contents = file.read()

with open("renamed_by_python.txt", "w") as file:
    file.write(contents)