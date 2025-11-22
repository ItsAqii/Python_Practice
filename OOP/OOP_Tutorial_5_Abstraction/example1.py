from abc import ABC, abstractmethod

class Animal(ABC):
    @property # Abstract property
    @abstractmethod # Abstract method
    def species(self):
        pass  # Abstract property, must be implemented by subclasses

class Dog(Animal):
    @property
    def species(self): # Implementing the abstract property
        return "Canine" #   Returning the species of the Dog

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)  # Output: Canine