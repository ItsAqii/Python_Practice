class Student: # Define a class named Student
    # Constructor to initialize name and marks
    def __init__(self, name, marks1, marks2, marks3): # __init__ is a special method that is called when an object is instantiated
        self.name = name
        self.marks1 = marks1 # self is a reference to the current instance of the class
        self.marks2 = marks2
        self.marks3 = marks3

    # Method to calculate and print average marks
    def print_average(self):  # Method to calculate and print average marks
        avg = (self.marks1 + self.marks2 + self.marks3) / 3 # Calculate average
        print(f"{self.name}'s average marks: {avg:.2f}") # Print average with 2 decimal places


# Example usage
student1 = Student("Aarav", 85, 90, 80)
student1.print_average()
