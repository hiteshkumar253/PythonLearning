st = "Hey Hitesh, How are you? Hope you are doing good."

a = open("myfile.txt", "a") # 'a' is the append mode. It will create a new file if it does not exist.
# If the file already exists, it will append the new content to the existing content.
# open the file in append mode


a.write(st)

# Always close the file after writing
a.close()
