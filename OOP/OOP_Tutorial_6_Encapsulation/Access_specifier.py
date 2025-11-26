# IN capsulation, access specifiers are used to set the accessibility of classes, methods, and variables.
# In Python, there are three types of access specifiers:
# 1. Public: Members (attributes and methods) declared as public are accessible from anywhere.
# 2. Protected: Members declared as protected are accessible within the class and its subclasses.   

# Protected members are prefixed with a single underscore (_).

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

class Sub_Employee(Employee):
    def Show_salary(self):
        print("Salary:", self._salary)  # Accessing protected attribute
    

emp = Sub_Employee("Alice", 60000)
print(emp.name)
emp.Show_salary()


#3 . Private: Members declared as private are accessible only within the class itself.
# Private members are prefixed with a double underscore (__).

class Employee_Private:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def Show_salary(self):
        return self.__salary  # Accessing private attribute via method

emp_private = Employee_Private("Bob", 70000)
print(emp_private.name)
print(emp_private.Show_salary())  # Accessing private attribute via method  

# Note: Direct access to protected and private members from outside the class is discouraged.
# For example, the following lines would raise an AttributeError:
# print(emp._salary)          # Accessing protected attribute directly (not recommended)    
# print(emp_private.__salary)  # Accessing private attribute directly (not recommended)     

# Example usage:
# emp = Employee("Alice", 60000) 