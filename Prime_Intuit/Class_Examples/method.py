
"""
In Python, method overriding and method overloading have different meanings 
compared to some other programming languages like Java or C++. Python does not 
support traditional method overloading based on the number or types of parameters. 
Instead, Python focuses on method overriding, which allows a subclass to provide a 
specific implementation of a method that is already defined in its superclass.

Method Overriding:

Method overriding occurs when a subclass provides a specific implementation for a 
method that is already defined in its superclass. The overridden method in the subclass 
should have the same name, parameters, and return type as the method in the superclass.

Here's an example of method overriding in Python:

In this example, the speak method in the Dog class overrides the speak method in the Animal 
class, providing a specific implementation for dogs.
"""
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal()
dog = Dog()

animal.speak()  # Output: "Animal speaks"
dog.speak()     # Output: "Dog barks"

"""
Method Overloading:

As mentioned earlier, Python does not support traditional method overloading based on the 
number or types of parameters like some other languages do. However, you can achieve a similar 
effect by using default parameter values and variable-length argument lists.

Here's a simplified example:
"""

class Calculator:
    def add(self, a, b=0):
        return a + b

calc = Calculator()

result1 = calc.add(5)
result2 = calc.add(3, 7)

print(result1)  # Output: 5
print(result2)  # Output: 10

"""
In this example, the add method can take one or two arguments. If you provide only one argument, 
it assumes the second argument is 0. This mimics method overloading based on the number of arguments.

Please note that this is not true method overloading like in languages like Java, where you can have 
multiple methods with the same name but different parameter types. In Python, you achieve similar behavior 
by defining a single method that can handle multiple parameter combinations.

So, in Python, method overriding is a fundamental concept for customizing behavior in subclasses, 
while method overloading is achieved by using default arguments and variable-length argument lists to 
handle different parameter combinations within a single method. 
"""
