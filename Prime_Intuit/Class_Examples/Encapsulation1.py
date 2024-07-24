# Encapsulation:

"""
Definition: Encapsulation is the bundling of data (attributes) and the methods that operate 
on the data into a single unit, known as a class. It helps in hiding the internal details of 
an object and exposing only what is necessary.
Example in Python:
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Creating an instance of the Student class
student1 = Student("Alice", 20)

# Accessing attributes and calling a method
print(student1.name)        # Output: Alice
student1.display_info()     # Output: Name: Alice, Age: 20
