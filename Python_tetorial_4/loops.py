# Loops in python
# while loop
i = 1
while i <= 5:
    print(i)
    i += 1  # Increment i by 1  # i = i + 1     
print("While loop ended")
# for loop
for i in range(1, 6):
    print(i)
print("For loop ended") 

#WAP to find the sum of first n numbers. (using while)
# Input the value of n
n = int(input("Enter a number (n): "))

# Initialize variables
i = 1
total = 0

# Use while loop to find sum
while i <= n:
    total += i
    i += 1

# Display the result
print("The sum of first", n, "numbers is:", total)

# Input the value of n
n = int(input("Enter a number (n): "))

# Loop through numbers from 1 to n
for i in range(1, n + 1):
    fact = 1
    # Calculate factorial of i
    for j in range(1, i + 1):
        fact *= j
    # Print factorial of each number
    print(f"Factorial of {i} = {fact}")
# WAP to find the factorial of first n numbers. (using for)