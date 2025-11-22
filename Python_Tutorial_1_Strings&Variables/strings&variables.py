# Variable: A variable is a name given to a memory location in a program.
# It is used to store data that can be referenced and manipulated throughout the program.
# In Python, you can create a variable by simply assigning a value to a name using the equals sign (=). 
# string is a sequence of characters enclosed in quotes (single or double).
# For example:

name = "Aqib"  # Here, 'name' is a variable that stores the string "Aqib".
age = 25       # 'age' is a variable that stores the integer 25.
print(name+" is "+str(age)+" years old.")  # Output: Aqib is 25 years old.


# In this example, we have two variables: 'name' and 'age'.
# We can use these variables in a print statement to display their values.
# String: A string is a data type that represents a sequence of characters.
# Strings are used to store and manipulate text in a program.

print(len(name)) # Output: 4
# The len() function returns the length of the string.
# In this case, it will output 4, as "Aqib" has 4 characters.
print(name.upper()) # Output: AQIB
# The upper() method converts all characters in the string to uppercase.
print(name.lower()) # Output: aqib
# The lower() method converts all characters in the string to lowercase.
print(name.replace("Aqib", "Bilal")) # Output: John
# The replace() method replaces occurrences of a specified substring with another substring.

name2 = "Aqib Ameen"
print(name2[0:4]) # Output: Aqib
# This is called string slicing. It extracts a portion of the string from index 0 to 4 (not inclusive of 4).
print(name2.split(" ")) # Output: ['Aqib', 'Ameen']
# The split() method splits the string into a list of substrings based on the specified delimiter (in this case, a space).
# In this example, we have a string variable 'name2' that contains the full name "Aqib Ameen".

p_g = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(p_g.count("a")) # Output: 19
# The count() method counts the occurrences of a specified substring in the string.
print(p_g.find("elit")) # Output: 56
# The find() method returns the index of the first occurrence of a specified substring in the string.
# If the substring is not found, it returns -1.
print(p_g.index("elit")) # Output: 56
# The index() method is similar to find(), but it raises a ValueError if the substring is not found.
# In this example, we have a longer string variable 'p_g' that contains a paragraph of text.
# We can use various string methods to manipulate and analyze the text.
# These are just a few examples of string methods in Python. There are many more methods available for manipulating strings.


# F-Strings: F-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces {}.
# They were introduced in Python 3.6 and provide a more readable and concise way to

greeting = "Assalamu Alaikum"
name_3 = "Aqib"

message = f"{greeting}, {name_3}. Welcome to the world of Python!"
#For example:
print(message)  # Output: Assalamu Alaikum, Aqib. Welcome to the world of Python!

 