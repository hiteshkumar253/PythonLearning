with open("poem.txt", "r") as file:
    content = file.read()
    if "twinkle" in content:
        print("The word twinkle is present in the content")
    else:
        print("The word twinkle is Not Present in the content")


# Alternative approach without 'with' statement
   
# f = open("poem.txt")
# content = f.read()
# if "twinkle" in content:
#     print("Found")