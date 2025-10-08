def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} is: {fact}")

# Example call
factorial(5)

 # Function to convert USD to PKR
def usd_to_pkr(usd):
    pkr = usd * 284
    print(f"{usd} USD = {pkr} INR")

# Example call
usd_to_pkr(10)
