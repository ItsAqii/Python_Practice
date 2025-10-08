    #WAF to print the elements of a list in a single line
def print_list(lst):
    print("Elements of the list:", end=" ")
    for item in lst:
        print(item, end=" ")
    print()  # For a new line after printing

# Example call
fruits = ["apple", "banana", "cherry"]
print_list(fruits)
# Output: Elements of the list: apple banana cherry
