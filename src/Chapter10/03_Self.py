class Employee:

    language = "Python"   # Class variable/attribute
    salary = 50000  # Class variable/attribute

    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")

object1 = Employee()
object1.getInfo()  # Output: Language: Python, Salary: 50000
# Employee.getInfo(object1)  # Output: Language: Python, Salary: 50000

# above object1.getInfo() will throw error because getInfo() method is not able to access class variables directly
# We need to use 'self' to access class variables inside methods
# 'self' represents the instance/object of the class and allows access to the attributes and methods of the class in Python
# 'self' is a convention, you can use any other name but it's recommended to use 'self' for better readability
# 'self' must be the first parameter of any method in the class
#  When a method is called on an instance/object, the instance/object in this case object1 is automatically passed as the first argument to the method
# This is how the method gets access to the instance/object and its attributes
# So, we need to define the method with 'self' as the first parameter to access instance/object attributes and methods

### Basically, behind the scene object1.getinfo() is translated to Employee.getInfo(object1)
# This Employee.getInfo(object1) is how the instance/object is passed to the method.
# getInfo() method is called on the class itself, we need to pass the instance/object explicitly as an argument
# This is why we need to define the method with 'self' as the first parameter to access instance/object attributes and methods
