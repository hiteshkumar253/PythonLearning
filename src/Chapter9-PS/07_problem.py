# return the line number of the first occurrence of the word "python" in the file "log.txt". 
# Make your search case insensitive. If the word is not found, print -1.

with open("log.txt", "r") as file:
    contents = file.readlines()
lineno = 1
for content in contents:
    if "python" in content:
        print(f" Yes python is present at line number {lineno}")
        break
    lineno += 1

else:
    print("NO python is not present")