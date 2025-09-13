f = open("file.txt")
# lines = f.readlines()
# # print(lines)
# # print(type(lines))  # This will show that 'lines' is a list


# line1 = f.readline() # This will read only the first line of the file
# print(line1, type(line1))

# line2 = f.readline() # This will read only the second line of the file
# print(line2, type(line2))

# line3 = f.readline() # This will read only the third line of the file
# print(line3, type(line3))

# line4 = f.readline() # This will read only the fourth line of the file
# print(line4, type(line4))

line = f.readline()
while(line != ""):  # This will check if line is not empty
    print(line)
    line = f.readline() # This will read only the next line of the file with in the loop


# Always close the file after use   
f.close()   