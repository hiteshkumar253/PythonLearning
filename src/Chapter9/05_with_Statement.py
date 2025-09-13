f = open("file.txt")
data = f.read()
print(data)
f.close() 


with open("myfile.txt") as a:
    print(a.read()) 
    
# 'with' statement automatically closes the file after the block of code is executed
# So, you do not need to explicitly close the file