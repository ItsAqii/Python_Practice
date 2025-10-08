# Function in Python
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
# Output: Hello, Alice!
# Function with default parameter
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())
# Output: Hello, Guest! 
# Function with variable-length arguments
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4))
# Output: 10
# Function with keyword arguments
def introduce(name, age):
    return f"My name is {name} and I am {age} years old."
print(introduce(age=30, name="Bob"))
# Output: My name is Bob and I am 30 years old.
