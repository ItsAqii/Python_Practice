# Example:
#  This example shows how to use a getter and a setter method to safely access 
#  and update a private attribute (__salary).

class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount.") 

# Create an Employee object
emp = Employee()    
print(emp.get_salary())  # Accessing salary using getter method
emp.set_salary(60000)    # Updating salary using setter method
print(emp.get_salary())  # Accessing updated salary using getter method
