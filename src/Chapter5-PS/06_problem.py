d = {}

name = input("Enter first friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})                         # d = {'Alice': 'Python'}

name = input("Enter second friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})                         # d = {'Alice': 'Python', 'Bob': 'Java'}

name = input("Enter third friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})                        # d = {'Alice': 'Python', 'Bob': 'Java', 'Tom': 'C++'}

name = input("Enter fourth friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})             # d = {'Alice': 'Python', 'Bob': 'Java','Tom': 'C++', 'Dave': 'Go'}


print(d)