# Program to find the sum of n natural numbers with recursion
# For example, if n = 5, then the sum is 1 + 2 + 3 + 4 + 5 = 15.
# The program should take a positive integer n as input and output the sum of the first n natural numbers.
# Example:
# Input: 5, output: 15
# Explanation: The sum of the first 5 natural numbers is : 1 + 2 + 3 + 4 + 5  = 15
# Hint: You can use the formula for the sum of the first n natural numbers: sum(n-1) + n

# Solution:
# Taking input from the user
# Function to calculate the sum of first n natural numbers
# Main code to execute the function and display the result
     

n = int(input("Enter a positive integer: "))

def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1) + n
    
print(f"The sum of first {n} natural numbers is {sum(n)}")