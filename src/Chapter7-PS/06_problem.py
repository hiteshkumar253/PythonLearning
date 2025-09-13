num = int(input("enther the number: "))

product = 1

# using for loop

for i in range(1, num+1):
    product=product * i

print(f"Factorial of number {num} is {product}")

# using while loop
# i=1
# while(i<=num):
#     product *= i
#     i += 1

# pprint(f"Factorial of number {num} is {product}")