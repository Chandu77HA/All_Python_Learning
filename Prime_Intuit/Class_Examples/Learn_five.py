# Polymorphism in Python

'''
What is Polymorphism: The word polymorphism means having many forms. 
In programming, polymorphism means the same function name (but different signatures) 
being used for different types. The key difference is the data types and number of arguments used in function.
'''
# Example of inbuilt polymorphic functions:

# Python program to demonstrate in-built poly-
# morphic functions
 
# len() being used for a string
print(len("geeks"))
 
# len() being used for a list
print(len([10, 20, 30]))

# Output
# 5
# 3

# Examples of user-defined polymorphic functions:

# A simple Python function to demonstrate
# Polymorphism

def add(x, y, z = 0):
	return x + y+z

# Driver code
print(add(2, 3))
print(add(2, 3, 4))

# Output
# 5
# 9

# Polymorphism with class methods:

'''
The below code shows how Python can use two different class types, 
in the same way. We create a for loop that iterates through a tuple of objects. 
Then call the methods without being concerned about which class type each object is. 
We assume that these methods actually exist in each class. 
'''

class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()


# Output

'''
New Delhi is the capital of India.
Hindi is the most widely spoken language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.
'''

# Polymorphism with Inheritance: 
'''
In Python, Polymorphism lets us define methods in the child class that have the same name as the 
methods in the parent class. In inheritance, the child class inherits the methods from the parent class. 
However, it is possible to modify a method in a child class that it has inherited from the parent class. 
This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the 
child class. In such cases, we re-implement the method in the child class. This process of re-implementing 
a method in the child class is known as Method Overriding.

'''

class Bird:
def intro(self):
	print("There are many types of birds.")
	
def flight(self):
	print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
def flight(self):
	print("Sparrows can fly.")
	
class ostrich(Bird):
def flight(self):
	print("Ostriches cannot fly.")
	
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


# Output

'''
There are many types of birds.
Most of the birds can fly but some cannot.
There are many types of birds.
Sparrows can fly.
There are many types of birds.
Ostriches cannot fly.

'''

# Polymorphism with a Function and objects: 
'''
It is also possible to create a function that can take any object, allowing for polymorphism. 
In this example, let’s create a function called “func()” which will take an object which we will name “obj”. 
Though we are using the name ‘obj’, any instantiated object will be able to be called into this function. 
Next, let’s give the function something to do that uses the ‘obj’ object we passed to it. In this case, 
let’s call the three methods, viz., capital(), language() and type(), each of which is defined in the two 
classes ‘India’ and ‘USA’. Next, let’s create instantiations of both the ‘India’ and ‘USA’ classes if 
we don’t have them already. With those, we can call their action using the same func() function:
'''


def func(obj):
    obj.capital()
    obj.language()
    obj.type()
  
obj_ind = India()
obj_usa = USA()
  
func(obj_ind)
func(obj_usa)

class India():
    def capital(self):
        print("New Delhi is the capital of India.")
  
    def language(self):
        print("Hindi is the most widely spoken language of India.")
  
    def type(self):
        print("India is a developing country.")
  
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
  
    def language(self):
        print("English is the primary language of USA.")
  
    def type(self):
        print("USA is a developed country.")
 
def func(obj):
    obj.capital()
    obj.language()
    obj.type()
  
obj_ind = India()
obj_usa = USA()
  
func(obj_ind)
func(obj_usa)

# Output

'''
New Delhi is the capital of India.
Hindi is the most widely spoken language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.

'''

# Simple example of polymorphism: 
# polymorphism in Python using inheritance and method overriding:

class Animal:
	def speak(self):
		raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
	def speak(self):
		return "Woof!"

class Cat(Animal):
	def speak(self):
		return "Meow!"

# Create a list of Animal objects
animals = [Dog(), Cat()]

# an = Animal()
# print(an.speak())

# Call the speak method on each object
for animal in animals:
	print(animal.speak())

# Output

# Woof!
# Meow!

# Class or Static Variables in Python

'''
All objects share class or static variables. An instance or non-static variables are different 
for different objects (every object has a copy). For example, let a Computer Science Student be 
represented by a class CSStudent. The class may have a static variable whose value is “cse” for 
all objects. And class may also have non-static members like name and roll.

 In C++ and Java, we can use static keywords to make a variable a class variable. The variables 
 which don’t have a preceding static keyword are instance variables. See this for the Java example 
 and this for the C++ example.

Explanation:
In Python, a static variable is a variable that is shared among all instances of a class, 
rather than being unique to each instance. It is also sometimes referred to as a class variable, 
because it belongs to the class itself rather than any particular instance of the class.

Static variables are defined inside the class definition, but outside of any method definitions. 
They are typically initialized with a value, just like an instance variable, but they can be 
accessed and modified through the class itself, rather than through an instance.

'''


'''
Features of Static Variables
Static variables are allocated memory once when the object for the class is created for the first time.
Static variables are created outside of methods but inside a class
Static variables can be accessed through a class but not directly with an instance.
Static variables behavior doesn’t change for every object.
The Python approach is simple; it doesn’t require a static keyword. 

Note: All variables which are assigned a value in the class declaration are class variables. 
And variables that are assigned values inside methods are instance variables.


'''

# Example:

# Python program to show that the variables with a value
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
	stream = 'cse'				 # Class Variable
	def __init__(self,name,roll):
		self.name = name		 # Instance Variable
		self.roll = roll		 # Instance Variable

# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name) # prints "Geek"
print(b.name) # prints "Nerd"
print(a.roll) # prints "1"
print(b.roll) # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"

# Now if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream) # prints 'ece'
print(b.stream) # prints 'cse'

# To change the stream for all instances of the class we can change it
# directly from the class
CSStudent.stream = 'mech'

print(a.stream) # prints 'ece'
print(b.stream) # prints 'mech'


# Output

'''
cse
cse
Kiran
Praveen
1
2
cse
ece
cse
ece
mech

'''

class MyClass:
    static_var = 0
 
    def __init__(self):
        MyClass.static_var += 1
        self.instance_var = MyClass.static_var
 
obj1 = MyClass()
print(obj1.instance_var)  # Output: 1
 
obj2 = MyClass()
print(obj2.instance_var)  # Output: 2
 
print(MyClass.static_var)  # Output: 2

# Output
# 1
# 2
# 2

'''
Explanation:
in this example, we define a class MyClass that has a static variable static_var initialized to 0. 
We also define an instance variable instance_var that is unique to each instance of the class.

When we create an instance of the class (obj1), we increment the value of the static variable by 1 
and assign it to the instance variable. When we create another instance of the class (obj2), we i
ncrement the static variable again and assign the new value to the instance variable for that instance.

Finally, we print out the value of the static variable using the class itself, rather than an instance 
of the class. As you can see, the value of the static variable is shared among all instances of the class, 
and it is incremented each time a new instance is created.

Static variables can be useful for maintaining state across all instances of a class, or for sharing 
data among all instances of a class. However, it’s important to use them carefully and to ensure that 
their values are synchronized with the state of the program, especially in a multithreaded environment.

Advantages:
Memory efficiency: Since static variables are shared among all instances of a class, they can save memory 
by avoiding the need to create multiple copies of the same data.
Shared state: Static variables can provide a way to maintain shared state across all instances of a class, 
allowing all instances to access and modify the same data.
Easy to access: Static variables can be accessed using the class name itself, without needing an instance 
of the class. This can make it more convenient to access and modify the data stored in a static variable.
Initialization: Static variables can be initialized when the class is defined, making it easy to ensure that 
the variable has a valid starting value.
Readability: Static variables can improve the readability of the code, as they clearly indicate that the 
data stored in the variable is shared among all instances of the class.
Disadvantages:
Inflexibility: Static variables can be inflexible, as their values are shared across all instances of the 
class, making it difficult to have different values for different instances.
Hidden dependencies: Static variables can create hidden dependencies between different parts of the code, 
making it difficult to understand and modify the code.
Thread safety: Static variables can be problematic in a multithreaded environment, as they can introduce 
race conditions and synchronization issues if not properly synchronized.
Namespace pollution: Static variables can add to the namespace of the class, potentially causing name 
conflicts and making it harder to maintain the code.
Testing: Static variables can make it more difficult to write effective unit tests, as the state of the 
static variable may affect the behavior of the class and its methods.
Overall, static variables can be a useful tool in Python programming, but they should be used with care 
and attention to potential downsides, such as inflexibility, hidden dependencies, and thread safety concerns.
'''

# Class method vs Static method in Python

'''

In this article, we will cover the basic difference between the class method vs Static 
method in Python and when to use the class method and static method in python.

What is Class Method in Python? 
The @classmethod decorator is a built-in function decorator that is an expression 
that gets evaluated after your function is defined. The result of that evaluation 
shadows your function definition. A class method receives the class as an implicit 
first argument, just like an instance method receives the instance 

Syntax Python Class Method: 

class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
fun: function that needs to be converted into a class method
returns: a class method for function.
A class method is a method that is bound to the class and not the object of the class.
They have the access to the state of the class as it takes a class parameter that points 
to the class and not the object instance.
It can modify a class state that would apply across all the instances of the class. 
For example, it can modify a class variable that will be applicable to all the instances.

'''

# What is the Static Method in Python?

'''
A static method does not receive an implicit first argument. A static method 
is also a method that is bound to the class and not the object of the class. 
This method can’t access or modify the class state. It is present in a class 
because it makes sense for the method to be present in class.

Syntax Python Static Method: 

class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...
returns: a static method for function fun.

'''

'''
Class method vs Static Method
The difference between the Class method and the static method is:

A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that 
take some parameters and work upon those parameters. On the other hand class methods must have 
class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod 
decorator to create a static method in python.
When to use the class or static method?
We generally use the class method to create factory methods. Factory methods return class 
objects ( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.
How to define a class method and a static method?
To define a class method in python, we use @classmethod decorator, and to define a static 
method we use @staticmethod decorator. 
Let us look at an example to understand the difference between both of them. Let us say 
we want to create a class Person. Now, python doesn’t support method overloading like C++ or 
Java so we use class methods to create factory methods. In the below example we use a class 
method to create a person object from birth year.

As explained above we use static methods to create utility functions. In the below example we 
use a static method to check if a person is an adult or not. 

One simple Example :

class method:
'''

class MyClass:
	def __init__(self, value):
		self.value = value

	def get_value(self):
		return self.value

# Create an instance of MyClass
obj = MyClass(10)

# Call the get_value method on the instance
print(obj.get_value()) # Output: 10

# Output
# 10


# Static method:-

class MyClass:
	def __init__(self, value):
		self.value = value

	@staticmethod
	def get_max_value(x, y):
		return max(x, y)

# Create an instance of MyClass
obj = MyClass(10)

print(MyClass.get_max_value(20, 30))

print(obj.get_max_value(20, 30))



# Output
# 30
# 30

# Below is the complete Implementation

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))


# Output:

# 21
# 25
# True