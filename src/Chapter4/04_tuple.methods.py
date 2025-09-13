# Tuple Methods, allow you to manipulate and access elements in tuples in Python.
# Here are the two main tuple methods in Python:
# count(): This method returns the number of occurrences of a specified value in a tuple.
# index(): This method returns the index of the first occurrence of a specified value in a tuple.
# Note: Tuples are immutable, so they do not have methods that modify the tuple like lists do.

a = (1, 45, 342, 3424, False, 45, "Rohan", "Shivam")
print(a)

no = a.count(45)  # counts the number of occurrences of 45 in the tuple
print(no)

i = a.index(3424)  # returns the index of the first occurrence of 3424 in the tuple
print(i)

print(len(a))  # prints the length of the tuple
