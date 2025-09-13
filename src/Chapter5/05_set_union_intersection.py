# Set Union and Intersection
# Set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

s1 = {1, 45, 6, 78}  # set can have multiple data types
s2 = {7, 8, 1, 78}  # set can have multiple data types

print(s1.union(s2))  # prints the union of two sets, which is a set containing all unique elements from both sets
print(s1.intersection(s2)) # prints the intersection of two sets, which is a set containing only the elements that are present in both sets
print(s1.difference(s2))  # prints the difference of two sets, which is a set containing elements that are in s1 but not in s2
print(s2.difference(s1)) # prints the difference of two sets, which is a set containing elements that are in s2 but not in s1
print(s1.symmetric_difference(s2))  # prints the symmetric difference of two sets, which is a set containing elements that are in either s1 or s2 but not in both
print(s2.symmetric_difference(s1))  # prints the symmetric difference of two sets, which is a set containing elements that are in either s2 or s1 but not in both
print(s1.isdisjoint(s2))  # prints True if the two sets have no elements in common, False otherwise
print(s1.issubset(s2))  # prints True if all elements of s1 are in s2, False otherwise
print(s2.issubset(s1))  # prints True if all elements of s2 are in s1, False otherwise
print(s1.issuperset(s2))  # prints True if all elements of s2 are in s1, False otherwise
print(s2.issuperset(s1))  # prints True if all elements of s1 are in s2, False otherwise
print(s1.copy())  # prints a shallow copy of the set s1
print(s1)  # prints the original set s1
print(len(s2))  # prints the length of the set s2
print(type(s1))  # prints the type of the set s1
print(min(s1))  # prints the minimum value in the set s1
print(max(s2))  # prints the maximum value in the set s2
print(sum(s2))  # prints the sum of all elements in the set s2
print(sorted(s1))  # prints a sorted list of all elements in the set s1
