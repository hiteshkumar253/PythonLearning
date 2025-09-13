with open("log.txt", "r") as file:
    content = file.read()

    if "python" in content.lower():
        print("The word python is present in the content")
    else:
        print("The word python is Not Present in the content")