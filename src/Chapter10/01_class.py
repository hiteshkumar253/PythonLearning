class Employee:
    language = "Python"   # Class variable/attribute
    salary = 50000  # Class variable/attribute

object1 = Employee()
object1.name = "Alice"   # Instance variable/attribute

print(object1.name, object1.language, object1.salary)  # Output: Alice Python 50000

object2 = Employee()
object2.name = "Bob"     # Instance variable/attribute
print(object2.name, object2.language, object2.salary)  # Output: Bob Python 50000