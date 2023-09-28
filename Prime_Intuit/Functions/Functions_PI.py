
# Introduction to functions:

x = int(input("Enter the num 1: "))
y = int(input("Enter the num 2: "))

z = x + y
print("Sum = ", z)

xa = int(input("Enter the num 3: "))
ya = int(input("Enter the num 4: "))

za = xa + ya
print("Sum = ", za)

xb = int(input("Enter the num 5: "))
yb = int(input("Enter the num 6: "))

zb = xb + yb
print("Sum = ", zb)

# Instead of writing a addition formula everytime write function once and use as many time that you want.

def addition(a, b):
    c = a + b
    return("addition", c)

z = addition(x, y)
print("Z = ", z)
print()
print("Sum = ", addition(x, y))
print("Sum = ", addition(xa, ya))
print("Sum = ", addition(xb, yb))

# Another example

x = int(input("Enter the num 1: "))
y = int(input("Enter the num 2: "))
z = int(input("Enter the num 3: "))

def addition(a, b):
    c = a + b
    return(c)

def subtraction(a, b):
    return (a - b)

def multiplication(a, b):
    return (a * b)

def division(a, b):
    return (a / b)

print("Addition of 2 Num : ", addition(x, y))
print("Subtraction of 2 Num : ", subtraction(x, y))
print("Multiplication of 2 Num : ", multiplication(x, y))
print("Division of 2 Num : ", division(x, y))

# Using functions smartly
print("Addition of 3 Num : ", addition(addition(x, y),z))
print("Subtraction of 3 Num : ", subtraction(subtraction(x, y),z))
print("multiplication of 3 Num : ", multiplication(multiplication(x, y),z))
print("division of 3 Num : ", division(division(x, y),z))


# Another example

def arithmatic_oper(a, b):
    add = a + b
    sub = a - b
    div = a / b
    mul = a * b
    return add, sub, div, mul

add_two, sub_two, mul_two, div_two = arithmatic_oper(10, 5)
print(add_two)
print(sub_two)
print(mul_two)
print(div_two)

print("Arithmatic Operations: ", arithmatic_oper(33, 12))
print("Type of Multiple return values: ", type(arithmatic_oper(33, 12)))

# Another example

x = int(input("Enter the num 1: "))
y = int(input("Enter the num 2: "))
z = int(input("Enter the num 3: "))
n = int(input("Enter the num 4: "))

def maximum1(a, b):
    if a > b:
        return a
    else:
        return b

def maximum2(a, b, c):
    if a > b > c:
        return a
    elif b > a > c:
        return b
    else:
        return c

print("Maximum of 2 num : ", maximum1(x, y))
print("Maximum of 3 num : ", maximum1(maximum1(x, y),z))
print("Maximum of 3 num : ", maximum2(x, y, z))
print("Maximum of 4 num : ", maximum1(maximum1(x, y),maximum1(z, n)))


# Another example

num1 = int(input("Enter a number 1 : "))
num2 = int(input("Enter a number 2 : "))

def function_2(a_number):
    mul = a_number*2
    return mul

# Calling function inside another function
def function_1(num):
    prod = num * num
    ano_ope = function_2(prod)
    return ano_ope

print("Result : ", function_2(num1))
print("Result : ", function_2(num2))
print("Result : ", function_1(num1))
print("Result : ", function_1(num2))


# Another example

def even_odd(ab):
    if ab % 2 == 0:
        print("even number")
        return ab
    else:
        print("odd number")
        return ab

print(even_odd(25))
print(even_odd(30))


# Another example

def odd_even_list(list_name):
    odd_list = []
    even_list = []
    for num in list_name:
        if num % 2 == 0:
            odd_list.append(num)
        else:
            even_list.append(num)
    return odd_list, even_list

num_list_L1 = [23, 34, 54, 45, 65, 56, 75, 6, 34, 55, 67, 89]

print(odd_even_list(num_list_L1))
ODD_NUM, EVEN_NUM = odd_even_list(num_list_L1)
print("ODD_NUM :", ODD_NUM)
print("EVEN_NUM :", EVEN_NUM)


# Arbitrary Arguments
# When we don't know how many arguments we give then we use * while passing parameters to the function
# * before the parameter When python doesn't know how may value user enter

def nk_total(*num):
    length_numbers = len(num)
    k = 0
    total_sum = 0
    while k < length_numbers:
        total_sum = total_sum + num[k]
        k = k + 1
    return total_sum

print("Sum of Values Entered 1 = ", nk_total(2, 2, 2))
print("Sum of Values Entered 2 = ", nk_total(2, 4, 6, 8, 10))
print("Sum of Values Entered 3 = ", nk_total(7, 10 , 12, 16, 17))
print("Sum of Values Entered 4 = ", nk_total(77, 77))

the_sum =  nk_total(23, 45, 65, 78, 43)
print("The sum of the the_sum Variable = ", the_sum)

# Default Parameter Value =
# when user define a function and pass the parameter with variable = some name or number.
# And when the function is called without passing the parameter it will use the default parameter when function is defined.

def nk_color(c = "blue"):
    print("Colour = ", c)

nk_color("red")
nk_color("white")

# Function called without parameter so it will use default parameter value c = "blue" from the function where it is called
nk_color()

def nk_trans(a, x, c=0):
    newX = x*a+c
    return newX
print("km to meters = ", nk_trans(1000, 3))

# Calculate fahrenheit using degree Celsius
# Formula ==> Fahrenheit = (Celsius*(9/5))+32

# In the below function a and b are default parameters
def deg_to_far(cel, a=(9/5), b=32):
    far = a*cel + b
    return far
print("Celsius to fahrenheit = ", deg_to_far(25))
print("Celsius to fahrenheit = ", deg_to_far(30))
print("Celsius to fahrenheit = ", deg_to_far(34))

# Calculate Celsius using Fahrenheit
# Formula ==> Celsius = (Fahrenheit-32)*5 / 9

# In the below function x, y, z are default parameters
def far_to_cel(far, x = 32, y = 5, z = 9):
    cel = (far-x)*y / z
    return cel

print("Fahrenheit to Celsius = ", far_to_cel(77))
print("Fahrenheit to Celsius = ", far_to_cel(86))
print("Fahrenheit to Celsius = ", far_to_cel(97))

# Factorial of a number

entered_num = int(input("Enter a Number : "))
fact = 1
for i in range(1, entered_num+1):
    fact = fact*i
print(f"Factorial of a Number {entered_num} = ", fact)

# recursion
# Calling the function inside the same function
def fact(m):
    if m == 1 or m == 0:
        return 1
    else:
        return m * fact(m-1)
    
# Example usage:
print("Factorial of 5 = ", fact(5))
print("Factorial of 0 = ", fact(0))
print("Factorial of 7 = ", fact(7))
print("Factorial of 8 = ", fact(8))


# Function to find the total sum of numbers from zero to number passed using recursion
# Example - 0+1+2+3+4+5+6 = 21 for number 6

def total_sum(num):
    if num == 0:
        return 0
    else:
        sum_of_num = num + total_sum(num-1)
    return sum_of_num

print(total_sum(5))
print(total_sum(6))

# Generator Function
# Generator Function are simple way of creating a iterators
# Use yield statement instead of return statement
# It does not return a single value instead it returns an iterator object with a sequence of value
# The output of the function should be stored in iterator like list, set, tuple

def power_value(the_list, power):
    for num in the_list:
        result = num**power
        yield(result)

l1 = [2, 4, 6, 8]
l2 = list(power_value(l1, 3))
print("Cube of Numbers in the List using Generator", l2)

l3 = [10, 20, 30, 40, 50]
l4 = list(power_value(l3, 2))
print("Square of Numbers in the List using Generator", l4)

num_list_L3 = [7, 8, 9, 12, 14, 24, 56]
print("Fourth power of Numbers in the List using Generator and stored in Tuple", tuple(power_value(num_list_L3, 4)))


'''
a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
 The simplest is the series 1, 1, 2, 3, 5, 8, etc.

The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers.
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, … Mathematically we can describe 
this as: xn= xn-1 + xn-2.

'''

# Fibonacci series with terms:
# Example if 10 is passed it will give first 10 Fibonacci Numbers

def fibo_terms(terms):
    num_1, num_2, incr = 0, 1, 1
    while incr <= terms:
        yield num_1
        next_last = num_1 + num_2
        num_1, num_2, incr = num_2, next_last, incr+1


# Fibonacci series with value limit:
# Example if 85 is passed it will Fibonacci Numbers with in 85

def fibo_limit(limit):
    num_1, num_2 = 0, 1
    while num_1 < limit:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2
        

# create a generator object for limits
ay = list(fibo_terms(6))
print("Fibonacci sequence for terms = ", ay)

az = list(fibo_terms(15))
print("Fibonacci sequence for terms = ", az)

# create a generator object for value
ax = list(fibo_limit(11))
print("Fibonacci sequence for limit = ", ax)

bz = list(fibo_limit(85))
print("Fibonacci sequence for limit = ", bz)




# lambda function is small anonymous function.
# lambda function can take any number of arguments, but can only have one expression

# lambda function to multiply 2 numbers
y = lambda a, b: a*b
print("Lambda Multiply", y(2, 3))

# lambda function to create a power of a number
p = lambda a, b: a**b
print("Lambda power", p(2, 3))

# lambda function to convert degree to fahrenheit
convert = lambda c, b = (9/5), a = 32 : c*b + a
print("Degree to fahrenheit =", convert(25))
print("Degree to fahrenheit =", convert(28.45))
print("Degree to fahrenheit =", convert(35))
print("Degree to fahrenheit =", convert(40))

# lambda function to convert fahrenheit to degree
fahr_to_deg = lambda far, x = 32, y = 5, z = 9: (far-x)*y / z
print("Fahrenheit to Degree =", fahr_to_deg(87))
print("Fahrenheit to Degree =", fahr_to_deg(98))

# lambda function to find odd and even numbers
even_odd = lambda a: "Even" if (a%2 == 0) else "Odd"
print("If 2 is even or Odd :", even_odd(2))
print("If 5 is even or Odd :", even_odd(5))

# lambda function to find odd and even numbers
even = lambda a: a % 2 == 0
print("If 2 is even :", even(2))
print("If 5 is even :", even(5))


# find if a given number is multiple of 7
div10 = lambda b: "True" if b % 7 == 0 else "False"
num_one = 49
num_two = 51
print(f"If {num_one} is Divisible by seven = ", div10(num_one))
print(f"If {num_two} is Divisible by seven = ", div10(num_two))

# making lambda more powerful by using it within a function
def pow_of_num(i):
    return lambda j: j**i

sqr = pow_of_num(2)
cube = pow_of_num(3)
fourth_pow = pow_of_num(4)

print("square of 3 =", sqr(3))
print("square of 5 =", sqr(5))
print("square of 7 =", sqr(7))

print("cube of 3 =", cube(3))
print("cube of 5 =", cube(5))
print("cube of 7 =", cube(7))

print("Fourth power of 5 =", fourth_pow(5))
print("Fourth power of 7 =", fourth_pow(7))

def times(c):
    return lambda d: c*d
double = times(2)
triple = times(3)
print("double of 4 :", double(4))
print("double of 10 :", double(10))
print("double of 23 :", double(23))

print("triple of 5 :", triple(5))
print("triple of 7 :", triple(7))
print("triple of 9 :", triple(9))


# sort sub lists

sort_list = lambda the_list:(sorted(inner_list) for inner_list in the_list)

l5 = [[2, 3, 1], [4, 5, 6], [9, 7, 8]]
print("sorted l5 :", list(sort_list(l5)))
l10 = [[30, 25, 20, 15, 10], [10, 5, 2, 7, 9], [15, 12, 8, 17, 19], [17, 13, 5, 26, 76, 26, 76]]
print("sorted l10 :", list(sort_list(l10)))

# Find second largest element in the inner list
second_large = lambda the_list, order: (i[-2] for i in order(the_list))
print("Second highest = ", list(second_large(l5, sort_list)))
print("Second highest = ", list(second_large(l10, sort_list)))

# Resolving probelm is above function by modifying it using CHATGPT

second_large = lambda the_list, order: (next(x for x in reversed(i) if x != max(i)) for i in order(the_list))

l10 = [[30, 25, 20, 15, 10], [10, 5, 2, 7, 9], [15, 12, 8, 17, 19], [17, 13, 5, 26, 76, 26, 76]]

# Find unique second largest element in the inner list
second_large = lambda the_list, order: (next(x for x in reversed(i) if x != max(i)) for i in order(the_list))

second_largest_l10 = list(second_large(l10, sort_list))
print("Unique Second highest in l10:", second_largest_l10)

# map, filters, reduce
# map function takes 2 items as arguments (function, iterable) and
# applies the function to each element in the iterable
# It returns a map object that need to be encapsulate inside an iterable

# Example usage - 1:
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sqr2 = lambda num : num**2
print("squares, map function :", list(map(sqr2, l1)))

# Example usage - 2:
Celsius_Tuple = (34, 24, 46, 28, 39, 20)
cel_to_farh = lambda cel, a=(9/5), b=32: a*cel + b
Fahrenheit_Tuple = tuple(map(cel_to_farh, Celsius_Tuple))
print("Celsius to Fahrenheit Using Lambda Function in Fahrenheit_Tuple :", Fahrenheit_Tuple)

# Example usage - 3:
T1 = (23, 42, 45, 52, 67)
Far = map(cel_to_farh, T1)
print(Far)
print(type(Far))
Far_tuple = tuple(Far)
print(type(Far_tuple))
print("Second tuple:", Far_tuple)


# filter function takes 2 items as arguments(function, iterable) it applies the function to each
# element in the iterable and returns only values of those element which satisfies
# the condition in the function

even = lambda x : x % 2 == 0
print("even number, filter function", list(filter(even,l1)))
print("odd number, filter function", list(filter(lambda x : x % 2 != 0, l1)))

# reduce is an in built function python function belongs to functools module
# Takes two items as an arguments function and a iterable
# this performs the repetative opertion over a pair of iterable and return a reduced result
import functools

list6 =[10, 20, 30, 40]
add1 = lambda x, y : x + y
print("output using reduce function :", functools.reduce(add1, list6))

list10 =[12, 17, 23, 28, 32, 37, 45]
beam = lambda x, y : (y - x) + 5
value = functools.reduce(beam, list10)
print(type(value))
print("output using reduce function :", value)



'''
The reduce(fun,seq) function is used to apply a particular function passed in its argument
 to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working :  

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just
 succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.
'''
# python code to demonstrate working of reduce()
  
# importing functools for reduce()
import functools
  
# initializing list
lis = [1, 3, 5, 6, 2]
  
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))
  
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# python code to demonstrate working of reduce()
# using operator functions

# importing functools for reduce()
import functools

# importing operator for operator functions
import operator

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))

'''
reduce() vs accumulate() 

Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. 
But there are differences in the implementation aspects in both of these.  

reduce() is defined in “functools” module, accumulate() in “itertools” module.
reduce() stores the intermediate result and only returns the final summation value. 
Whereas, accumulate() returns a iterator containing the intermediate results. 
The last number of the iterator returned is summation value of the list.
reduce(fun, seq) takes function as 1st and sequence as 2nd argument. 
In contrast accumulate(seq, fun) takes sequence as 1st argument and function as 2nd argument.
'''

# python code to demonstrate summation
# using reduce() and accumulate()
  
# importing itertools for accumulate()
import itertools
  
# importing functools for reduce()
import functools
  
# initializing list
lis = [1, 3, 4, 10, 4]
  
# printing summation using accumulate()
print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x+y)))
  
# printing summation using reduce()
print("The summation of list using reduce is :", end="")
print(functools.reduce(lambda x, y: x+y, lis))

# Python program to  illustrate sum of two numbers.

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
  
# Note that the initializer, when not None, is used as the first value instead of the first value from iterable,
# and after the whole iterable.
tup = (2,1,0,2,2,0,0,2)
print(reduce(lambda x, y: x+y, tup,6))

tup_two = (3, 5, 7, 9, 11)
print(reduce(lambda x, y: x+y, tup_two))
  
tup_two = (3, 5, 7, 9, 11)
print(reduce(lambda x, y: x+y, tup_two, 50))


