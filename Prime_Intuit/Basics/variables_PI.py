
print("There was a small boy named soma")
print("He used to sell flowers after his school")
print("Every day after 5 PM he used to go to market on his bicycle")
print("And sell flowers until it returned dark")
print("Today he made a profit of RS 250.58")

name = "Sidharth"
product = "Painting"
time = "4"
gain = "350"


print("There was a small boy named", name)
print("He used to sell", product, "after his school")
print("Every day after", time, "PM he used to go to market on his bicycle")
print("And sell", product, "until it returned dark")
print("Today he made a profit of RS", gain)

a = 10
b = 10

# print statement showing memory address
print("a is ", type(a), id(a))
print("b is", type(b), id(b)) 
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

d = 77
e = 10
c = d + e
print("Addition + ==>", c)
c = d - e
print("Subtraction - ==>", c)
c = d * e
print("Multiplication * ==>", c)
c = d / e
print("Division / ==>", c)
c = d % e
print("Modulus % ==>", c)
c = d // e
print("Floor division // ==>", c)

# Defining Multiple variables
d, e ,f = 10, 12, 14 
print(d, e, f)


# Swapping two Numbers Based on Multiple assignment(Method -1)

a, b = 10, 5
a, b = b, a
print(a,b)

# Swapping two Numbers using third variable (Method -2)

a, b = 10, 23
c = a
a = b
b = c
print(a,b)

# Swapping two Numbers using addition (Method -3)

a, b = 12, 14
a = a + b #26
b = a - b #12
a = a - b #14
print(a, b)

# Swapping two Numbers using multiplication and division (Method -4)

a, b = 10, 5
a = a * b #50
b = a / b #10
a = a / b #5
print(a, b)

# Swapping two Numbers using multiplication and division (Method -5)

a, b = 20, 10
a = a / b
b = a * b
a = b / a
print(int(a), int(b))

# Find Max of two numbers

a = 25
b = 30
if a > b:
    print("Max Number is : ", a)
else:
    a < b
    print("Max Number is : ", b)

# Learning input function

a = input("Enter number-1 : ")
print(a, type(a))

# Change Variable type from float to int by applying int cast

a = input("Enter number-1 : ")
a = int(a)
print(a, type(a))

# Change Variable type from float to int by applying int cast

a = int(input("Enter number-1 : "))
print(a, type(a))

# Print maximum of three numbers

a = int(input("Enter number1 : "))
b = int(input("Enter number2 : "))
c = int(input("Enter number3 : "))

if a >= b and a >= c:
    print("Max number is : ", a)
elif b >= a and b >= c:
    print("Max number is : ", b)
else:
    print("Max number is : ", c)

# maximum of three numbers and in descending order

a = int(input("Enter number1 : "))
b = int(input("Enter number2 : "))
c = int(input("Enter number3 : "))
if a > b and a > c:
    if b > c:
        print("Descending order of the numbers is : ", a, b, c)
    else:
        print("Descending order of the numbers is : ", a, c, b)
elif b > a and b > c:
    if a > c:
        print("Descending order of the numbers is : ", b, a, c)
    else:
        print("Descending order of the numbers is : ", b, c, a)
elif a > b:
    print("Descending order of the numbers is : ", c, a, b)
else:
    print("Descending order of the numbers is : ", c, b, a)





# maximum of three numbers

a = int(input("Enter number1 : "))
b = int(input("Enter number2 : "))
c = int(input("Enter number3 : "))

# Case1 : a = b  = c

if a == b == c:
    print("all three numbers are same")

# Case2 : a = b  or b = c or c = a

elif (a == b):
    if a > c:
        print("Max number is a, b ", a)
    else:
        print("Max number is c", c)
elif (b == c):
    if b > a:
        print("Max number is b, c ", b)
    else:
        print("Max number is a", a)
elif (c == a):
    if c > b:
        print("Max number is c, a ", a)
    else:
        print("Max number is b", b)

# Case3 : a != b != c

elif a > b and a > c:
    print("Max number is a : ", a)
elif b > a and b > c:
    print("Max number is b: ", b)
else:
    print("Max number is c: ", c)

# program for area and perimeter of circle, volume and surface area of sphere

repeat = int(input("enter the number of intervals : "))
for i in range(repeat):
    pi = 3.142
    r = float(input("enter the radius is cms : "))
    # area of the circle:
    area = pi*r**2
    print("area of the circle with radius: ", r, "is", area)
    # perimeter of the circle:
    per = 2 * pi * r
    print("perimeter of the circle with radius: ", r, "is", per)
    # volume of the sphere:
    vol = (4/3)*(pi*r**3)
    print("volume of the sphere with radius: ", r, "is", vol)
    surf = 4 * pi * r**2
    print("surface of the circle with radius: ", r, "is", surf)
a = (2, 3, 4, 5)
b = [6, 7, 8, 9]

c = {
    'a' : 10,
    'b' : 20,
    'c' : 30,
    }

d = {"apple", "banana", "cherry"}

print(type(a))
print(type(b))
print(type(c))
print(type(d))

name = "Prime-Intuit"
Phrase = "Prime-Intuit is one of the finest Finishing School "
print(name[2])
print(name[0], name[6])
print(Phrase[0:12])
print(len(name))
print(len(Phrase))
print(Phrase[34:50])
