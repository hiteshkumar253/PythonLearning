
d = {}

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