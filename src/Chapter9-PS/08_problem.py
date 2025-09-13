with open("this.txt", "r") as file:
    contents = file.read()

with open("this_copy.txt", "w") as file:
    file.write(contents)    