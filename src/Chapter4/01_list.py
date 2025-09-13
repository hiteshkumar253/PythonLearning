# List in Python
# List is a collection of items which is ordered and changeable. Allows duplicate members.
# Lists are written with square brackets.
# Example:

friends = ["Apple", "Orange", 5, 345.89, False, "Akash", "Rohan"]  # List can have multiple data types

print(friends)  # prints the entire list
print(friends[0])  # prints the first item of the list

friends[0] = "Grapes"  # unlike strings List are mutable, we can change the value of a list
print(friends)  # prints the entire list after changing the first item

print(friends[6])  # prints the 7th item of the list

print(friends[1:4])  # prints items from index 1 to 3 (excluding 4)
print(friends[3:])  # prints items from index 3 to end of the list
print(friends[:4])  # prints items from index 0 to 3 (excluding 4)