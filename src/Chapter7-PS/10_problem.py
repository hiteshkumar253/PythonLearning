number = int(input("Enter the number : "))
# i=10
# print(f"Table of number {number} in reversed order")
# while(i>=1):

#     print(f"{number} X {i} =", number*i)
#     i -=1
   
print(f"Table of number {number} in reversed order")
for i in range(10,0,-1):
    print(f"{number} X {i} =", number*i)