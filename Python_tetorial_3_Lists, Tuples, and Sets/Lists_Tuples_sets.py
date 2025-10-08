# list operations
# Demonstrating basic list operations in Python
# Creating a list
# Accessing elements
# Slicing
# Length of the list
# Appending and removing elements
# Reversing the list
# Note: Lists are mutable, meaning they can be changed after creation

'''my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
print("First element of the list:", my_list[0]) # Accessing the first element
print("Last element of the list:", my_list[-1]) # Accessing the last element
print("List slice (1 to 3):", my_list[1:4]) # Slicing the list
print("List length:", len(my_list)) # Length of the list
print("List after appending 6:", my_list + [6])  # Appending 6 to the list
print("List after removing 2:", [x for x in my_list if x != 2])  # Removing 2 from the list
print(reversed(my_list))  # Reversing the list'''

# tuple operations
# Demonstrating basic tuple operations in Python
# Creating a tuple
# Accessing elements
# Slicing
# Length of the tuple
# Note: Tuples are immutable, meaning they cannot be changed after creation
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

print("First element of the tuple:", my_tuple[0]) # Accessing the first element
print("Last element of the tuple:", my_tuple[-1]) # Accessing the last element
print("Tuple slice (1 to 3):", my_tuple[1:4]) #

print("Tuple length:", len(my_tuple)) # Length of the tuple
# Note: Tuples do not support item removal or reversal as they are immutable
print(reversed(my_tuple))  # Reversing the tuple Slicing the tuple

# my_tuple[0] = 10  # Attempting to change the first element (will raise an error)
# This will raise a TypeError because tuples are immutable

# set operations
# Demonstrating basic set operations in Python
# Creating a set
# Adding and removing elements
# Set operations: union, intersection, difference
# Note: Sets are unordered collections of unique elements
'''
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)
my_set.add(6)  # Adding an element
print("Set after adding 6:", my_set)
my_set.remove(3)  # Removing an element
print("Set after removing 3:", my_set)
another_set = {4, 5, 6, 7, 8}
print("Another set:", another_set)
print("Union of sets:", my_set.union(another_set))
print("Intersection of sets:", my_set.intersection(another_set))
print("Difference of sets:", my_set.difference(another_set))
'''
# Note: Sets do not support indexing or slicing as they are unordered
# print("First element of the set:", my_set[0])  # This will raise an error
# print("Set slice (1 to 3):", my_set[1:4])  # This will raise an error

# my_set[0] = 10  # Attempting to change the first element (will raise an error)
# This will raise a TypeError because sets do not support indexing
# print(reversed(my_set))  # This will raise an error because sets are unordered

# Ask the user to enter names of their 3 favorite movies
'''
movie1 = input("Enter the name of your first favorite movie: ")
movie2 = input("Enter the name of your second favorite movie: ")
movie3 = input("Enter the name of your third favorite movie: ")

# Store them in a list
favorite_movies = [movie1, movie2, movie3]

# Display the list
print("Your favorite movies are:", favorite_movies)
'''

# Given tuple of grades
grades = ("C", "D", "A", "A", "B", "B", "A")

# Count number of students with 'A' grade
count_A = grades.count("A")
print("Number of students with 'A' grade:", count_A)

# Convert the tuple to a list
grades_list = list(grades)

# Sort the list from 'A' to 'D'
grades_list.sort()

# Display the sorted list
print("Sorted grades (A to D):", grades_list)

# set 
# Given set of numbers
numbers = {1, 2, 3, 4, 5}   
# Add number 6 to the set
numbers.add(6)
# Remove number 3 from the set
numbers.remove(3)
# Display the final set
print("Final set of numbers:", numbers)
# Note: The order of elements in the set may vary as sets are unordered collections
# Attempting to access an element by index will raise an error
# print("First element of the set:", numbers[0])  # This will raise an error
# print("Set slice (1 to 3):", numbers[1:4])  # This will raise an error
# Attempting to change an element by index will raise an error
# numbers[0] = 10  # This will raise an error
# print(reversed(numbers))  # This will raise an error because sets are unordered
# Note: Sets do not support indexing or slicing as they are unordered
# print("First element of the set:", numbers[0])  # This will raise an error
# print("Set slice (1 to 3):", numbers[1:4])
# This will raise an error
# numbers[0] = 10  # Attempting to change the first element (will raise an error)
# This will raise a TypeError because sets do not support indexing

# To store 9 and 9.0 as separate values in a set

# Method 1: By storing them as different data types
s1 = {9, "9.0"}
print("Method 1:", s1)

# Method 2: By storing type information along with the value
s2 = {(int, 9), (float, 9.0)}
print("Method 2:", s2)