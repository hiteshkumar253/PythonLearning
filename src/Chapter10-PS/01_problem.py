# Create a class named Programmer for storing information of various programmers working at Microsoft.

class Programmer:

    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode


p = Programmer("Prateek", 100000, 411057)
print(p.name, p.salary, p.pincode, p.company)

r = Programmer("Rohit", 120000, 411058)
print(r.name, r.salary, r.pincode, r.company)

t = Programmer("Tilak", 140000, 411059)
print(t.name, t.salary, t.pincode, t.company)