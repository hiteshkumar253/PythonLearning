marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
     0: "Hitesh"
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Harry": 99, "Renuka": 100})
print(marks)

print(marks.items())

print(marks.get("Harry")) 
print(marks["Harry"])     
        
print(marks.pop(0))          # Hitesh
print(marks)                   # {'Harry': 99, 'Shubham': 56, 'Rohan': 23}


print(marks.popitem())          # Hitesh
print(marks)                   # {'Harry': 99, 'Shubham': 56, 'Rohan': 23}

# diff between below line of codes (interveiw questions)

print(marks.get("Harry2"))         # Prints None
print(marks["Harry2"])             # Returns an error

