friends = ["Apple", "Orange", 5, 345.89, False, "Aakash", "Rohan"]

print(friends)

friends.append("Hitesh")  # .append is a list method which inserts at the end of a list

print(friends)



l1 = [3, 5, 9, 2, 46]
print(l1)

print(l1.sort())  # l1.sort() sorts the list in place and returns None. So when you do print(l1.sort()), it prints None.

#Correct Way:

l1.sort()
print("Sorted list:", l1)

l1.reverse()
print("Reversed list:", l1)

l1.insert(2,434535)
print(l1)

l1.pop()
print(l1)

l1.remove(434535)
print(l1)