# String functions in Python
# String functions are built-in methods that allow you to manipulate and work with strings in various ways.
# Here are some commonly used string functions in Python:

name = "hitesh"

print(len(name))  # length of string

print(name.endswith("esh"))  # check if string ends with "esh"
print(name.endswith("eshq"))  # check if string ends with "eshq"
print(name.startswith("Hi"))  # check if string starts with "Hi", will return False as it is case-sensitive
print(name.startswith("t"))  # check if string starts with "t"

print(name.capitalize())  # capitalize first letter of string

print(name.lower())  # convert string to lowercase
print(name.upper())  # convert string to uppercase