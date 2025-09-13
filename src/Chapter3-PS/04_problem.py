given_string = input("Enter the String: ")

a= given_string.find("  ")

if(a != -1):
    print(f"double space detected at index: ", a)
    print(f"Corrected string: ", given_string.replace("  ", " "))
else:
    print("no double space found")