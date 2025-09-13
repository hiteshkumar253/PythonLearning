
temp = float(input("Enter temperature in Fahrenheit: "))

# Write a program to convert Fahrenheit to Celsius.

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*5/9
    return celsius

result = fahrenheit_to_celsius(temp)
print(f"Temperature in Fahrenheit: {result} °C")
print(f"Temperature in Fahrenheit: {round(result,2)} °C")