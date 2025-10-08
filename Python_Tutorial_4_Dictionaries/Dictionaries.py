# Dictionaries in Python
# A dictionary is a collection of key-value pairs. Each key is unique and is used to access the corresponding value.
# Creating a dictionary
'''my_dict = {'name': 'Aqib', 'age': 24, 'city': 'Lahore'}
print(my_dict)
# Accessing values
print(my_dict['name'])  # Output: Aqib
print(my_dict.get('age'))  # Output: 24
# Adding or updating key-value pairs
my_dict['email'] = 'aqibameen790@gmail.com'  # Add new key-value pair
print(my_dict)
my_dict['age'] = 25  # Update age
print(my_dict)
# Removing key-value pairs
del my_dict['city']  # Remove key 'city'
print(my_dict)
my_dict.pop('email')  # Remove key 'email'
print(my_dict)'''

# Example of a dictionary with different data types
'''
Marks = {}

# input from user
Name = input("Enter your name: ")
Marks["Name"] = Name

sub1 = input("Enter subject 1 name: ")
Marks[sub1] = int(input("Enter marks for subject 1: "))

sub2 = input("Enter subject 2 name: ")
Marks[sub2] = int(input("Enter marks for subject 2: "))

sub3 = input("Enter subject 3 name: ")
Marks[sub3] = int(input("Enter marks for subject 3: "))

print(Marks)'''


student = {__name__: 'Aqib', 'age': 24, 'marks': [85, 90, 78]}
for key, value in student.items():
    print(key, value)
