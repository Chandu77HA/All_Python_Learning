# Abstraction

"""
Abstraction is a fundamental concept in Object-Oriented Programming (OOP) that involves hiding the complex 
implementation details of an object and exposing only the essential features. It allows developers to focus on 
the functionality of an object without getting bogged down by the intricacies of its internal workings. In Python, 
abstraction is often achieved through abstract classes and abstract methods.

Abstract Classes and Abstract Methods:
An abstract class is a class that cannot be instantiated on its own and may contain one or more abstract methods. 
An abstract method is a method declared in an abstract class without providing an implementation. Subclasses inheriting 
from the abstract class must provide concrete implementations for the abstract methods, thereby enforcing a common interface.

Example in Python:

"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Creating instances of Circle and Rectangle
circle_instance = Circle(5)
rectangle_instance = Rectangle(4, 6)

# Calling the area method on both instances
print(circle_instance.area())       # Output: 78.5
print(rectangle_instance.area())    # Output: 24


"""
In this example, the Shape class is an abstract class with an abstract method area(). 
The Circle and Rectangle classes inherit from Shape and provide concrete implementations for the area method. 
The abstraction lies in defining a common interface (area) for different shapes without specifying how each shape calculates its area.
"""

"""
Benefits of Abstraction:
Simplifies Complexity: Abstraction simplifies the representation of real-world entities by 
focusing on essential features and hiding unnecessary details, making code more manageable.

Promotes Code Reusability: Abstract classes and methods enable the creation of a common interface, 
facilitating the reuse of code in different parts of a program or in future projects.

Enhances Maintainability: By encapsulating implementation details within abstract classes, 
changes to the internal workings of a class won't affect the code that uses the class, promoting easier maintenance.

Enforces Consistency: Abstraction ensures that subclasses adhere to a common interface, 
promoting consistency in the way objects are used and reducing the likelihood of errors.

Supports Polymorphism: Abstraction is closely tied to polymorphism, allowing objects of 
different classes to be treated uniformly through a common interface.

Overall, abstraction is a powerful tool in software design that contributes to creating modular, 
extensible, and maintainable code. It enables developers to build systems that are more adaptable 
to change and easier to understand.
"""
