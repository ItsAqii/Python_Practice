
# Input three numbers from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Check which one is greatest
if a >= b and a >= c:
    print("The greatest number is:", a)
elif b >= a and b >= c:
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c)
