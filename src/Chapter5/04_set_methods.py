# Set Methods in Python
# Set methods are built-in functions that allow you to manipulate and modify sets in Python.
# Sets do not allow duplicate values.
# Here are some commonly used set methods in Python:

s = {1, 5, 32, 54,5, 5, 5, "Harry"}

print(s, type(s))  # Note: Sets do not allow duplicate values, so the multiple 5s will be stored as a single 5.

s.add(566)            # The .add() method is used to add a single element to a set.
print(s, type(s))
s.remove(1)           # The .remove() method is used to remove a specific element from a set.
print(s, type(s))   