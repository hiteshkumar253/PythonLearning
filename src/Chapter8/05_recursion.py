'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 * factorial(1) = 2 * 1 = 2
factorial(3) = 3 * factorial(2) = 3 * 2 * 1 = 6
factorial(4) = 4 * factorial(3) = 4 * 3 * 2 * 1 = 24
factorial(5) = 5 * factorial(4) = 5 * 4 * 3 * 2 * 1 = 120
.
.
.
factorial(n) = n * factorial(n-1)

'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1) # 5 * factorial(4)

a = int(input("Enter a number to find factorial: "))

print("The factorial of this number is: ", factorial(a))