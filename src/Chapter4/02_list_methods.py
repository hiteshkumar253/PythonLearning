# List Methods in Python
# List methods are built-in functions that allow you to manipulate and modify lists in Python.
# Here are some commonly used list methods in Python:


friends = ["Apple", "Orange", 5, 345.89, False, "Akash", "Rohan"]

print(friends)

friends.append("Hitesh")  # .append is a list method which inserts at the end of a list

print(friends)

l1 = [3, 5, 9, 2, 46]
print(l1)
print(l1.sort())  # l1.sort() sorts the list in place and returns None.

# If you want to print the sorted list then you have to print the list after sorting, here is a correct way to do it:

l1.sort()  # sorts the list in place
print("Sorted list:", l1)  # prints the sorted list

l1.reverse()  # l1.reverse() reverses the list in place and returns None.
print("Reversed list:", l1)  # prints the reversed list

l1.insert(2, 434535)  # inserts 434535 at index 2
print(l1)  # prints the list after insertion

l1.pop()  # removes the last element of the list
print(l1)  # prints the list after removing the last element

l1.remove(434535)  # removes the first occurrence of 434535 from the list
print(l1)  # prints the list after removing 434535
