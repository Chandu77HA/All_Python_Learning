

# Decorators concept in python
# PI Class learning

def dev(a, b):
    return (a/b)

print(dev(5 ,10))

def sub(a, b):
    return (a-b)

print(sub(15 ,20))

def deco(func):
    def inner(x, y):
        if x < y:
            x, y = y, x
            return func(x, y)
    return inner

var_1 = deco(dev)
print("Modified division", var_1(5, 10))

var_2 = deco(sub)
print("Modified subtraction", var_2(15, 20))

# Second Highest

def sort2(pass_list):
    pass_list.sort()
    return pass_list

l4 = [80, 90, 10, 40, 60, 50, 20]
print("sorted l4 list :", sort2(l4))

def deco_sec_high(value):
    def sec_high(the_list):
        return value(the_list)[-2]
    return sec_high

find_sec_high = deco_sec_high(sort2)
l6 = [88, 44, 66, 99, 77, 22, 11]
print("sorted L2_num_list list :", sort2(l6 ))
print("second highest with sorted list l6 :", find_sec_high(l6))

# LEARNING - 1

def plus_one(number):
    return number + 1

# Calling Function Type - 1
add_one = plus_one(5)
print(add_one)

# Calling Function Type - 2
add_1 = plus_one
print(add_1(76))

# Calling Function Type - 3
print(plus_one(27))

# LEARNING - 2

def plus_one(number):
    def add_one(number):
        return number + 1

    result = add_one(number)
    return result

# Calling Function Type - 1
print(plus_one(45))

# Calling Function Type - 2
ac = plus_one(76)
print(ac)

# LEARNING - 3

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

def function_call_2(function):
    number_to_add_2 = 76
    return function(number_to_add_2)

print(function_call(plus_one))
print(function_call_2(plus_one))

# LEARNING - 4

def hello_function(some_func):
    def say_hi():
	    print("This is say hi function")
	    some_func()
	    print("Learning decorators completed")
    return say_hi

def text_fun():
	print("This is text_fun function")
	
    
the_call = hello_function(text_fun)
the_call()

# LEARNING - 5

def print_message(message):
    "Enclosing Function"
    def message_sender():
        "Nested Function"
        print(message)
    message_sender()

print_message("Some random message")

# Greeks for Greeks Learning

'''
Decorators are a very powerful and useful tool in Python since it allows programmers to 
modify the behaviour of a function or class. Decorators allow us to wrap another function 
in order to extend the behaviour of the wrapped function, without permanently modifying it. 
But before diving deep into decorators let us understand some concepts that will come in 
handy in learning the decorators.

First Class Objects
In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.
Properties of first class functions:
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
Consider the below examples for better understanding.

'''

# Example 1: Treating the functions as objects.

# Python program to illustrate functions
# can be treated as objects
def shout(text):
	return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))

'''
In the above example, we have assigned the function shout to a variable.
This will not call the function instead it takes the function object 
referenced by a shout and creates a second name pointing to it, yell.

'''

# Example 2: Passing the function as an argument

# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	# return keyword is optional here
	print (greeting)

greet(shout)
greet(whisper)

'''
In the above example, the greet function takes another 
function as a parameter (shout and whisper in this case). 
The function passed as an argument is then called inside the function greet.'''

# Example 3: Returning functions from another function.

# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print(add_15)
print(add_15(10))


'''
In the above example, we have created a function inside of another
function and then have returned the function created inside.
The above three examples depict the important concepts that 
are needed to understand decorators. After going through them let us now dive deep into decorators.'''


# Decorators

'''
As stated above the decorators are used to modify the behaviour of function or class. 
In Decorators, functions are taken as the argument into another function and then called 
inside the wrapper function.
'''

# Syntax for Decorator:
'''

@gfg_decorator
def hello_decorator():
    print("Gfg")

Above code is equivalent to -

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)'''

'''
In the above code, gfg_decorator is a callable function, 
that will add some code on the top of some another callable function, 
hello_decorator function and return the wrapper function.'''

# Decorator can modify the behaviour:

# defining a decorator
def hello_decorator(func):

	# inner1 is a Wrapper function in
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# Can be used like this also
call_fun = hello_decorator(function_to_be_used)
call_fun()

print()

# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)
 

'''
Let’s jump to another example where we can easily find out the execution time of a function using a decorator.
'''

# calling the function
function_to_be_used()


# importing libraries
import time
import math
 
# decorator to calculate duration
# taken by any function.
def calculate_time(func):
     
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
 
        # storing time before function execution
        begin = time.time()
         
        func(*args, **kwargs)
 
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
 
    return inner1
 
# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
 
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))
 
# calling the function.
factorial(10)

print()

'''
What if a function returns something or an argument is passed to the function?
In all the above examples the functions didn’t return anything so there wasn’t 
an issue, but one may need the returned value.

'''

def hello_decorator(func):
	def inner1(*args, **kwargs):
		
		print("before Execution")
		
		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1


# adding decorator to the function
@hello_decorator
def sum_of_numbers(a, b, c):
	print("Inside the function")
	return a + b + c

num_one, num_two, num_three= 5, 10, 15

# getting the value through return of the function
print("Sum of numbers=", sum_of_numbers(num_one, num_two, num_three))

'''
In the above example, you may notice a keen difference in the parameters of the inner function. 
The inner function takes the argument as *args and **kwargs which means that a tuple of positional 
arguments or a dictionary of keyword arguments can be passed of any length. This makes it a general 
decorator that can decorate a function having any number of arguments.

'''

# Another Example

def multiplication_decorator(func):
	def inner_func(*args, **kwargs):
		print("Befor Execution")
		returned_value = func(*args, **kwargs)
		print("After Execution")
		return returned_value
	return inner_func

# adding decorator to the function
@multiplication_decorator
def mul_of_numbers(a, b, c):
	print("Inside the function")
	return a * b * c

ab, bc, cd= 4, 5, 6

# getting the value through return of the function
print("Multiplication of numbers = ", mul_of_numbers(ab, bc, cd))


# Chaining Decorators
# In simpler terms chaining decorators means decorating a function with multiple decorators.

# code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner

@decor1
@decor
def num():
	return 10

@decor
@decor1
def num2():
	return 10

print(num())
print(num2())

'''
The above example is similar to calling the function as –

decor1(decor(num))
decor(decor1(num2))

'''
