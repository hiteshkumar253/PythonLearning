# write a python program to convert inches to centimeters. 

inches = float(input("Enter length in inches: "))

def inches_to_cm(inches):
    cm = inches * 2.54
    return cm

n = inches_to_cm(inches)
print(f"Length in centimeters: {n} cm")