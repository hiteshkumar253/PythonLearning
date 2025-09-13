class Employee:

    language = "Python"   # Class variable/attribute
    salary = 50000

    def __init__(self, name, salary, language):
        self.name = name          # Instance variable/attribute
        self.salary = salary      # Instance variable/attribute
        self.language = language  # Instance variable/attribute
        print("Constructor/Init method called")
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")
        # __init__ method is called automatically when an instance/object of the class is created
        # It is used to initialize the instance/object attributes
        # It is also known as constructor in other programming languages
        # It is a special method in Python, it is called automatically when an instance/object of the class is created
        # It is defined using double underscores before and after the method name


    def getInfo(self):
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

object1 = Employee("Alice", 60000, "Java")  # __init__ method is called automatically

print(object1.name, object1.salary, object1.language)  # Output: Alice Java 60000
