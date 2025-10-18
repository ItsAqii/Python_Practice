class Employee:
    # Class variable
    raise_amount = 1.05
    # Constructor
    def __init__(self, f_name, l_name, pay):
        self.f_name = f_name  # Instance variable
        self.l_name = l_name  # Instance variable
        self.pay = pay  # Instance variable
        self.email = f_name + '.' + l_name + '@company.com'     # Instance variable


    def fullname(self):
        return '{} {}'.format(self.f_name, self.l_name)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Salman', 'Khan', 50000)
emp_2 = Employee('Shahrukh', 'Khan', 60000)
print(emp_1.pay)  # Output: 50000
emp_1.apply_raise()
print(emp_1.pay)  # Output: 52500 

print(emp_1.__dict__)  # Output: {'f_name': 'Salman', 'l_name': 'Khan', 'pay': 50000, 'email': '

