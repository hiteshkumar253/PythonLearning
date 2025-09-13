# Tuples are immutable, meaning their elements cannot be changed after they are created.
# Here is an example demonstrating this property:
a = (34, 234, "Hitesh")

a[2] = "Jitesh"

print(a)  # This will raise a TypeError: 'tuple' object does not support item assignment