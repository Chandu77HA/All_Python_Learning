# Polymorphism


"""

Polymorphism is a key concept in Object-Oriented Programming (OOP) that allows objects to be treated as 
instances of their parent class, even when they are instances of a subclass. It provides a way to use a 
single interface to represent different types of objects or, more specifically, to perform a single action 
in multiple ways. Python supports two types of polymorphism: compile-time (or static) polymorphism and runtime (or dynamic) polymorphism.

1. Compile-time Polymorphism (Method Overloading):
Compile-time polymorphism involves having multiple methods in the same class with the same name but different parameter lists. 
The method that gets called is determined at compile time based on the number and types of arguments passed.

Example in Python:

"""


class MathOperations:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z


# Creating an instance of MathOperations
math_instance = MathOperations()

# This will result in an error as Python does not support method overloading in the traditional sense.
# Instead, the latest defined method will override the previous one.
# math_instance.add(2, 3)  # Error: TypeError


# To achieve similar functionality, you can use default values for parameters
class MathOperationsWithDefaults:
    def add(self, x, y, z=None):
        if z is not None:
            return x + y + z
        else:
            return x + y


# Creating an instance of MathOperationsWithDefaults
math_instance_with_defaults = MathOperationsWithDefaults()

print(math_instance_with_defaults.add(2, 3))       # Output: 5
print(math_instance_with_defaults.add(2, 3, 4))    # Output: 9
