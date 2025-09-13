
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