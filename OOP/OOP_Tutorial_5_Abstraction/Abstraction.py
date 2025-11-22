# Data abstraction means showing only the essential features and hiding the complex internal details.
# In Python, abstraction can be achieved using abstract classes and methods from the 'abc' module.

from abc import ABC, abstractmethod

class Greeting (ABC):
    @abstractmethod
    def say_hello(self):
        pass # Abstract method, must be implemented by subclasses

class English(Greeting):
    def say_hello(self):
        return "Hello!"
    
g = English()
print(g.say_hello())

