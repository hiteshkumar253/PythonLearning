# Negative Slicing in Python
# Negative slicing allows you to slice a string using negative indices, which count from the end of the string.
# The last character of the string has an index of -1, the second last character has an index of -2, and so on.

name = "Hitesh"

print(name)


print(name[-6:-2])  # start from index -6 all the way till -2 (excluding -2)

print(name[0:4])  # start from index 0 all the way till 4 (excluding 4)

print(name[:6])  # start from index 0 all the way till 6 (excluding 6)

print(name[-4:])  # start from index -4 all the way till end of string

print(name[:-5])  # start from index 0 all the way till -5 (excluding -5)

print(name[0:6:2])  # start from index 0 all the way till 6 (excluding 6) with a step of 2