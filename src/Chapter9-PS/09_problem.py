with open("this.txt", "r") as file:
    content1 = file.read()

with open("this_copy.txt", "r") as file:
    content2 = file.read()

if content1 == content2:
        print("Yes, the two files are identical")
else:
        print("No, the two files are not identical")