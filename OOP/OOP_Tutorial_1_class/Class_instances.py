# class in Python

# Class is a blueprint for creating objects.
# An object is an instance of a class.
# A class can have attributes (data) and methods (functions).
'''
class employee:
    # class attribute
    company = "Google"

    # constructor
    def __init__(self, name, age, salary):
        self.name = name  # instance attribute
        self.age = age    # instance attribute
        self.salary = salary  # instance attribute

    # method
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Company: {self.company}")
'''
# creating instances of the class

class employee:
    def __init__(self, name, last_name, age, salary, email):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.salary = salary
        self.email = email
    def full_name(self):
        return '{} {}'.format(self.name, self.last_name)

# creating instances of the class

emp1 = employee("Aqib", "Javed", 24, 50000, "aqib.am@gmail.com") # instance 1

emp2 = employee("Ali", "Noor", 25, 60000, "ali.am@gmail.com")   # instance 2

#print(emp1)
#print(emp2)
#print(emp1.salary)
#print(emp2.email)
print(emp1.full_name())
print(emp2.full_name())
