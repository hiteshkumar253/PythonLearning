'''
write a program to print the follwing pattern
***
**
*
'''

n = int(input("Enter a number: "))

def pattern(n):
    if n == 0:
        return
    print('*' * n)
    pattern(n-1)

pattern(n)