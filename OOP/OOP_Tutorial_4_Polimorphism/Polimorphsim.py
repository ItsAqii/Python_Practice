# polimorphism in python

# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class Vehicle: # Parent class
  def __init__(self, brand, model):  # Constructor to initialize brand and model
    self.brand = brand          # Instance variable for brand
    self.model = model

  def move(self):    # Method to be overridden in child classes
    print("Move!")    # Default implementation

class Car(Vehicle):   # Child class inheriting from Vehicle
  pass

class Boat(Vehicle):  # Child class inheriting from Vehicle
  def move(self):
    print("Sail!")

class Plane(Vehicle):  # Child class inheriting from Vehicle
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1): # Iterate through the objects
  print(x.brand) # Print the brand of the object
  print(x.model)  # Print the model of the object
  x.move() # Call the move method, demonstrating polymorphism
