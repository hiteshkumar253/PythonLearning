# wipe out the contents of a file

with open("this_copy.txt", "w") as file:
    file.write("") # writing empty string to the file to wipe out the contents