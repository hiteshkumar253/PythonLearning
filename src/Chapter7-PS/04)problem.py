n = int(input("Enter the number: "))

for i in range(2,n):
    if(n%i) == 0:
        print(f"{n} is not a prime nubmer")
        break

else:
        print(f"{n} is a Prime number ")

