# Reading a file in Python

# open() function opens a file in read mode by default
# 'file.txt' is the file name which is to be read
# It should be present in the same directory as this python file
# If it is not present in the same directory then provide the full path of the file
# For example: f = open("C:/Users/Test/Desktop/PythonLearning/Chapter9/file.txt")
# open the file in read mode

f = open("file.txt")

# read() function reads the whole file
# If the file is large then it may take some time
# You can also specify the number of characters to be read by passing an integer value to read()
# For example: f.read(10) will read only first 10 characters of the file
# Here we are reading the whole file
# store the content of the file in a variable
data = f.read()

# print the content of the file
print(data)

# Always close the file after use
f.close()