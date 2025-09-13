st = "Hey Hitesh, How are you? Hope you are doing good."
# 'w' is the write mode. It will create a new file if it does not exist.
# If the file already exists, it will overwrite the existing content.
# open the file in write mode
# If you want to append to an existing file, use 'a' mode instead of 'w'
# a = open("myfile.txt", "a")
# Here we are using 'w' mode
# If the file is not present in the same directory then provide the full path of the file
# For example: a = open("C:/Users/Test/Desktop/PythonLearning/Chapter9/myfile.txt", "w")
# open the file in write mode
# If the file does not exist, it will be created
# If the file exists, it will overwrite the existing content
# write the string to the file
# Always close the file after writing
# If you do not close the file, the content may not be written to the file properly
a = open("myfile.txt", "w")

# write the string to the file
# write() function writes the string to the file
# It does not add a newline character at the end of the string
# So, if you write multiple times, all the content will be in a single line
# To add a newline character, you can use '\n' at the end of the string
# For example: st = "Hey Hitesh, How are you?\nHope you are doing good."
# a.write(st)
# Here we are writing only once, so no need to add '\n'
a.write(st)

# Always close the file after writing
a.close()
