# What will be the length of the set `s` after the following operations?

s = set()
s.add(20)  # integer
s.add(20.0)  # float, same value as integer 20
s.add('20')  # string

print(s)  # Output the set to see its contents
print(len(s))  #