# replace the given word donkey to ##### in the file donkey.txt

# with open("file.txt", "r") as file:
#     content = file.read()
#     content = content.replace("donkey", "#####")


# with open("file.txt", "w") as file:
#     file.write(content)

# Alternative approach

with open("file.txt", "r") as file:
    content = file.read()

with open("file.txt", "w") as file:
    file.write(content.replace("donkey", "#####"))