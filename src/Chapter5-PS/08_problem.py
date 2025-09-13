# Create a dictionary to store the names of your friends and their favorite programming languages.
# If the language of two friends are same, what will happen to the program?
# Use the input function to get the names and languages from the user.

d = {}

name = input("Enter first friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})                         # d = {'Alice': 'Python'}

name = input("Enter second friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})                         # d = {'Alice': 'Python', 'Bob': 'Java'}

name = input("Enter third friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})                        # Tom's language gets updated to Python! # d = {'Alice': 'Python', 'Bob': 'Java', 'Tom': 'Python'}

name = input("Enter fourth friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})                       # d = {'Alice': 'Python', 'Bob': 'Java', 'Tom': 'Python','Dave': 'Go'}


print(d)