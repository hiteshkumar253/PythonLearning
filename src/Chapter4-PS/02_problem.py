# Write a program to store marks of 6 students in a list and display them in sorted manner.

marks_list = []  #

student1 = int(input("Enter the marks here: "))
marks_list.append(student1)  # adding marks of student1 to the list

student2 = int(input("Enter the marks here: "))
marks_list.append(student2)  # adding marks of student2 to the list

student3 = int(input("Enter the marks here: "))
marks_list.append(student3)  # adding marks of student3 to the list

student4 = int(input("Enter the marks here: "))
marks_list.append(student4)  # adding marks of student4 to the list

student5 = int(input("Enter the marks here: "))
marks_list.append(student5)  # adding marks of student5 to the list

student6 = int(input("Enter the marks here: "))
marks_list.append(student6)  # adding marks of student6 to the list

print("Original marks_list: ", marks_list)  # printing the original list

marks_list.sort()  # sorts the list in ascending order

print("Sorted marks_list: ", marks_list)  # printing the sorted list
