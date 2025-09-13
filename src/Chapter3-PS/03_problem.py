given_string = input("Enter the String: ")

a= given_string.find("  ")   # .find string method returns the index of the first occurance only of the double space

if(a != -1):
    print(f"double space detected at index: ", a)
else:
    print("no double space found")