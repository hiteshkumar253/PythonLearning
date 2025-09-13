class Employee:
    language = "Python"   # Class variable/attribute
    salary = 50000  # Class variable/attribute

object1 = Employee()
print( object1.language, object1.salary)  # Output: Python 50000

object2 = Employee()
object2.language = "C++"     # Instance variable/attribute
print(object2.language, object2.salary)  # Output: Python 50000

# Instance variable 'language' is created for object2, it does not affect the class variable
# object1 still accesses the class variable
# Instnce variable takes precedence over class variable when accessed via instance/object