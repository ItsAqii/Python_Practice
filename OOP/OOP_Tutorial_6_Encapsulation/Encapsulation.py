# Encapsulation in Python
# Encapsulation is the way of restricting access to certain attributes and methods of an object.
# This is done to prevent the accidental modification of data.
class Employee:
    def __init__(self, name , salary):
        self.name = name
        self._salary = salary  # Protected attribute

    def get_salary(self):
        return self._salary
    
emp = Employee("Robirt", 50000)
print(emp.name)          # Accessing public attribute
print(emp.get_salary())  # Accessing protected attribute via method
