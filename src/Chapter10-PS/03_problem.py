# create a class  with class attribute a; create an object from it and set 'a' directly using obect.a=0.
# does it change the class attribute?

class MyClass:
    a = 10

obj = MyClass()
print("Before changing, class attribute a:", MyClass.a)
print("Before changing, object attribute a:", obj.a)

obj.a = 0
print("After changing, class attribute a:", MyClass.a)
print("After changing, object attribute a:", obj.a)

# Answer: No, it does not change the class attribute. 
# It creates an instance attribute 'a' for the object 'obj', leaving the class attribute unchanged.