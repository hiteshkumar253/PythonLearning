# Write a class named Calculator which performs basic mathematical operations like square, cube and squareroot.

class Calculator:

    def __init__(self, n):
        self.n = n
        print("Calculator object created with value as:", self.n)


    def square(self):
        return self.n * self.n
    
    def cube(self):
        return self.n * self.n * self.n
    
    def squareroot(self):
        return self.n * self.n  * 0.5
    
    @staticmethod         # static method does not take 'self' as first argument
    def hello():
        print("Hello, I am a static method.")


Calc = Calculator(4)
print(Calc.square())
print(Calc.cube())
print(Calc.squareroot())
Calc.hello()