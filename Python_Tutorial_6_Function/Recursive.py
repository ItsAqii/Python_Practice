
def sum_n(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    else:
        return n + sum_n(n - 1)

# Example call
num = int(input("Enter a number (n): "))
result = sum_n(num)
print(f"The sum of first {num} natural numbers is: {result}")


def print_list(lst, index=0):
    # Base case: stop when index reaches the length of list
    if index == len(lst):
        return
    # Print the current element
    print(lst[index])
    # Recursive call for the next element
    print_list(lst, index + 1)

# Example call
items = ["apple", "banana", "cherry", "mango"]
print_list(items)
