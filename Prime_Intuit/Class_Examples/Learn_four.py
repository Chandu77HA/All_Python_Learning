# Types of inheritance Python

'''
Inheritance is defined as the mechanism of inheriting the properties of 
the base class to the child class. Here we a going to see the types of inheritance in Python.

'''

# Types of Inheritance in Python

'''
Types of Inheritance depend upon the number of child and parent classes involved. 
There are four types of inheritance in Python:
'''

# Single Inheritance:

'''
Single inheritance enables a derived class to inherit properties 
from a single parent class, thus enabling code reusability and the 
addition of new features to existing code.
'''

# Example:

# Python program to demonstrate
# single inheritance

# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class


class Child(Parent):
	def func2(self):
		print("This function is in child class.")


# Driver's code
object = Child()
object.func1()
object.func2()


# Output:

# This function is in parent class.
# This function is in child class.

# Multiple Inheritance:

'''
When a class can be derived from more than one base class this 
type of inheritance is called multiple inheritances. In multiple inheritances, 
all the features of the base classes are inherited into the derived class.

'''
# Example:

# Python program to demonstrate
# multiple inheritance

# Base class1
class Mother:
	mothername = ""

	def mother(self):
		print(self.mothername)

# Base class2


class Father:
	fathername = ""

	def father(self):
		print(self.fathername)

# Derived class


class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)


# Driver's code
s1 = Son()
s1.fathername = "RAMA"
s1.mothername = "SITA"
s1.parents()


# Output:

# Father : RAM
# Mother : SITA

# Multilevel Inheritance :

'''
In multilevel inheritance, features of the base class and the derived class 
are further inherited into the new derived class. This is similar to a relationship 
representing a child and a grandfather. 
'''
# Example:

# Python program to demonstrate
# multilevel inheritance

# Base class


class Grandfather:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

# Intermediate class


class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername

		# invoking constructor of Grandfather class
		Grandfather.__init__(self, grandfathername)

# Derived class


class Son(Father):
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname

		# invoking constructor of Father class
		Father.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)


# Driver code
s1 = Son('Chandan', 'Arun', 'Basappa')
print(s1.grandfathername)
s1.print_name()

# Output:

# Basappa
# Grandfather name : Basappa
# Father name : Arun
# Son name : Chandan

# Hierarchical Inheritance:

'''
When more than one derived class are created from a single base this type of 
inheritance is called hierarchical inheritance. In this program, we have a 
parent (base) class and two child (derived) classes.
'''

# Example:

# Python program to demonstrate
# Hierarchical inheritance


# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class1


class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")

# Derivied class2


class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")


# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()


# Output:

'''
This function is in parent class.
This function is in child 1.
This function is in parent class.
This function is in child 2.
'''

# Hybrid Inheritance:

'''
Inheritance consisting of multiple types of inheritance is called hybrid inheritance.
'''

# Python program to demonstrate
# hybrid inheritance


class School:
	def func1(self):
		print("This function is in school.")


class Student1(School):
	def func2(self):
		print("This function is in student 1. ")


class Student2(School):
	def func3(self):
		print("This function is in student 2.")


class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()
object.func4()


# Output:

# This function is in school.
# This function is in student 1.
# This function is in student 3.

# Encapsulation in Python

'''
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
It describes the idea of wrapping data and the methods that work on data within one unit. 
This puts restrictions on accessing variables and methods directly and can prevent the accidental 
modification of data. To prevent accidental change, an object’s variable can only be changed by an 
object’s method. Those types of variables are known as private variables.

A class is an example of encapsulation as it encapsulates all the data that is member functions, 
variables, etc. The goal of information hiding is to ensure that an object’s state is always valid 
by controlling access to attributes that are hidden from the outside world.
'''

'''

Consider a real-life example of encapsulation, in a company, there are different sections 
like the accounts section, finance section, sales section etc. The finance section handles 
all the financial transactions and keeps records of all the data related to finance. Similarly, 
the sales section handles all the sales-related activities and keeps records of all the sales. 
Now there may arise a situation when due to some reason an official from the finance section 
needs all the data about sales in a particular month. In this case, he is not allowed to directly 
access the data of the sales section. He will first have to contact some other officer in the sales 
section and then request him to give the particular data. This is what encapsulation is. Here the 
data of the sales section and the employees that can manipulate them are wrapped under a single 
name “sales section”. Using encapsulation also hides the data. In this example, the data of the 
sections like sales, finance, or accounts are hidden from any other section.

'''

# Protected members

'''
Protected members (in C++ and JAVA) are those members of the class that cannot 
be accessed outside the class but can be accessed from within the class and its subclasses. 
To accomplish this in Python, just follow the convention by prefixing the name of the member 
by a single underscore “_”.

Although the protected variable can be accessed out of the class as well as in the derived 
class (modified too in derived class), it is customary(convention not a rule) to not access 
the protected out the class body.

Note: The __init__ method is a constructor and runs as soon as an object of a class is instantiated.  

'''
# Python program to
# demonstrate protected members

# Creating a base class
class Base:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)



# Output:

'''
Calling protected member of base class:  2
Calling modified protected member outside class:  3
Accessing protected member of obj1:  3
Accessing protected member of obj2:  2
'''

# Private members

'''
Private members are similar to protected members, the difference is that the class members 
declared private should neither be accessed outside the class nor by any base class. 
In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.

However, to define a private member prefix the member name with double underscore “__”.

Note: Python’s private and protected members can be accessed outside the class through python name mangling. 
'''

# Python program to
# demonstrate private members

# Creating a Base class


class Base:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"
	def base_fun(self):
		print("private members can be accessed only inside the class :", self.__c)

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)
obj1.base_fun()
# print(obj1.c)


# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AttributeError as
# private member of base class
# is called inside derived class

# obj2 = Derived()
