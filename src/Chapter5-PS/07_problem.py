# Create a dictionary to store the names of your friends and their favorite programming languages.
# If the name of 2 friends are same, what will happen to the program?
# Use the input function to get the names and languages from the user.


d = {}  # Initialize an empty dictionary

name = input("Enter first friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})                         # d = {'Alice': 'Python'}

name = input("Enter second friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})                         # d = {'Alice': 'Python', 'Bob': 'Java'}

name = input("Enter third friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})                        # Alice's language gets updated to C++! # d = {'Alice': 'C++', 'Bob': 'Java'}

name = input("Enter fourth friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})                       # d = {'Alice': 'C++', 'Bob': 'Java','Dave': 'Go'}


print(d)