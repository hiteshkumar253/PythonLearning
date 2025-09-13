# Dictionary Methods
# Dictionary methods are built-in functions that allow you to manipulate and modify dictionaries in Python.


marks = {"Harry": 100, "Shubham": 56, "Rohan": 23, 0: "Hitesh"}

print(marks.items())  # returns a view object that displays a list of a dictionary's key-value tuple pairs
print(marks.keys())   # returns a view object that displays a list of all the keys in the dictionary
print(marks.values())  # returns a view object that displays a list of all the values in the dictionary

marks.update({"Harry": 99, "Renuka": 100})  # updates the value of key "Harry" to 99 and adds a new key-value pair "Renuka": 100
print(marks)

print(marks.items())

print(marks.get("Harry"))  # 99
print(marks["Harry"])   # 99

print(marks.pop(0))  # Hitesh
print(marks)  # {'Harry': 99, 'Shubham': 56, 'Rohan': 23}

print(marks.popitem())  # Hitesh
print(marks)  # {'Harry': 99, 'Shubham': 56, 'Rohan': 23}

# diff between below line of codes (interveiw questions)

print(marks.get("Harry2"))  # Prints None, as "Harry2" key is not present in the dictionary
print(marks["Harry2"])      # KeyError: 'Harry2'
