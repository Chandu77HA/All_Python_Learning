# Inheritance:

"""
Definition: Inheritance is a mechanism that allows a new class (subclass or derived class) 
to inherit properties and behaviors of an existing class (base class or parent class). 
It promotes code reusability and establishes a relationship between classes.
Example in Python:
    """


class Animal:
    def speak(self):
        pass

    def motility(self):
        print("Yes animals are able to move.")


class Dog(Animal):
    def speak(self):
        return "Bow!"


class Wolf(Animal):
    def speak(self):
        return "Woof!"


# Creating an instance of the Dog class
dog_instance = Dog()

# Calling the speak method from the Dog class
print(dog_instance.speak())   # Output: Bow!

# Calling the motility method from the Animal class
dog_instance.motility()  # Yes animals are able to move.

# Creating an instance of the Wolf class
wolf_instance = Wolf()

# Calling the speak method from the Wolf class
print(wolf_instance.speak())   # Output: Woof!

# Calling the motility method from the Animal class
wolf_instance.motility()  # Yes animals are able to move.
