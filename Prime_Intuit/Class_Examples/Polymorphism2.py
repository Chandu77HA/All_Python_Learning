"""
    2. Runtime Polymorphism (Method Overriding):
Runtime polymorphism, also known as dynamic polymorphism, involves the use of inheritance and method overriding. 
In this case, a method in the superclass is overridden in the subclass, providing a specific implementation in the subclass.
    
"""

# Example in Python:


class Animal:
    def speak(self):
        return "Generic animal sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Creating instances of Animal, Dog, and Cat
generic_animal = Animal()
dog_instance = Dog()
cat_instance = Cat()

# Polymorphic function call
print(generic_animal.speak())   # Output: Generic animal sound
print(dog_instance.speak())      # Output: Woof!
print(cat_instance.speak())      # Output: Meow!

"""
In this example, the speak method in the Animal class is overridden in both the Dog and Cat subclasses. 
When you call speak on an instance of Animal, Dog, or Cat, the appropriate overridden method is executed, 
demonstrating runtime polymorphism.

Polymorphism is a powerful and flexible feature that allows for more generic and extensible code by 
treating objects based on their common interface. It enhances code readability, reusability, and maintainability in complex software systems.
"""
