# Learning *args and **kwargs in Python from Geeks for Geeks

'''
In this article, we will cover what ** (double star/asterisk) and * (star/asterisk) 
do for parameters in Python,  Here, we will also cover args and kwargs examples in Python. 
We can pass a variable number of arguments to a function using special symbols. 

There are two special symbols:

Special Symbols Used for passing arguments in Python:

*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)

Note: “We use the “wildcard” or “*” notation like this – 
*args OR **kwargs – as our function’s argument when we have 
doubts about the number of arguments we should pass in a function.” 
'''


'''
What is Python *args?
The special syntax *args in function definitions in Python is used to pass a variable 
number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list. 

The syntax is to use the symbol * to take in a variable number of arguments; 
by convention, it is often used with the word args.

What *args allows you to do is take in more arguments than the number of formal 
arguments that you previously defined. With *args, any number of extra arguments 
can be tacked on to your current formal parameters (including zero extra arguments).
For example, we want to make a multiply function that takes any number of arguments 
and is able to multiply them all together. It can be done using *args.

Using the *, the variable that we associate with the * becomes iterable meaning 
you can do things like iterate over it, run some higher-order functions such as map and filter, etc.

'''

# Example 1:

# Python program to illustrate *args for a variable number of arguments

def myFun(*argv):
	for arg in argv:
		print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Example 2:

# Python program to illustrate *args with a first extra argument

def myFun(arg1, *argv):
	print("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


'''
What is Python **kwargs?
The special syntax **kwargs in function definitions in Python is used to pass 
a keyworded, variable-length argument list. We use the name kwargs with the double star. 
The reason is that the double star allows us to pass through keyword arguments (and any number of them).

A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that 
we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any 
order in which they were printed out.

'''

'''
Example 1: 

Python program to illustrate *kwargs for a variable number of keyword arguments. 
Here **kwargs accept keyworded variable-length argument passed by the function call. 
for first=’Geeks’ first is key and ‘Geeks’ is a value. in simple words, what we assign is value, 
and to whom we assign is key. 
'''

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

'''
Example 2:

Python program to illustrate  **kwargs for a variable number of keyword 
arguments with one extra argument. All the same, but one change is we 
passing non-keyword argument which acceptable by positional argument(arg1 in myFun). 
and keyword arguments we passing are acceptable by **kwargs. simple right?
'''

def myFun(arg1, **kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))
	return print("At Final Printing extra argument = ", arg1)


# Driver code
myFun("Hi", first='Geeks', mid='for', last='Geeks')

# Using both *args and **kwargs in Python to call a function
# Example 1:

'''
Here, we are passing *args and **kwargs as an argument in the myFun function. 
Passing *args to myFun simply means that we pass the positional and variable-length 
arguments which are contained by args. so, “Geeks” pass to the arg1 , “for” pass to the arg2, 
and “Geeks” pass to the arg3. When we pass **kwargs as an argument to the myFun it means that 
it accepts keyword arguments. Here, “arg1” is key and the value is “Geeks” which is passed to arg1, 
and just like that “for” and “Geeks” pass to arg2 and arg3 respectively. After passing all the 
data we are printing all the data in lines.

'''


def myFun(arg1, arg2, arg3):
    print("arg one:", arg1)
    print("arg two:", arg2)
    print("arg three:", arg3)
 
 
# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)
 
kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)

# Example 2:

'''
Here, we are passing *args and **kwargs as an argument in the myFun function. 
where ‘geeks’, ‘for’, ‘geeks’ is passed as *args, and first=”Geeks”, mid=”for”, 
last=”Geeks”  is passed as **kwargs and printing in the same line.
'''

def myFun(*args, **kwargs):
	print("args: ", args)
	print("Type of arge :",type(args))
	print("kwargs: ", kwargs)
	print("Type of kwargs :",type(kwargs))


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")


'''
Using *args and **kwargs in Python to set values of object
*args receives arguments as a tuple.
**kwargs receives arguments as a dictionary.
'''

# Example 1: using Python *args

# defining car class
class car():
	# args receives unlimited no. of arguments as an array
	def __init__(self, *args):
		# access args index like array does
		self.speed = args[0]
		self.color = args[1]


# creating objects of car class
audi = car(200, 'red')
bmw = car(250, 'black')
mb = car(190, 'white')

# printing the color and speed of the cars
print(audi.color)
print(bmw.speed)

# Example 2: using Python **kwargs

# defining car class
class car():
	# args receives unlimited no. of arguments as an array
	def __init__(self, **kwargs):
		# access args index like array does
		self.speed = kwargs['s']
		self.color = kwargs['c']


# creating objects of car class
audi = car(s=200, c='red')
bmw = car(s=250, c='black')
mb = car(s=190, c='white')

# printing the color and speed of cars
print(audi.color)
print(bmw.speed)
