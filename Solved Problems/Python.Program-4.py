
print()
print("PYTHON COLLECTION ARRAYS")
print()
print("There are four collection data types in the python programing language")
print()
print("-> LIST - is a collection which is ordered and changeable. allows duplicate members.")
print("-> TUPLE - is a collection which is ordered and unchangeable. allows duplicate members.")
print("-> SET - is a collection which is unordered, unchangeable and unindexed. no duplicate members.")
print("-> SET - is a collection which is ordered and changeable. no duplicate members.")

#1) ==>> Break Continue Pass Example

# Break

for i in range(1, 5):
    if i == 3:
        break
    print(i)

RESULT:
1
2

for i in range(1, 5):
    print(i)
    if i == 3:
        break

RESULT:
1
2
3

# Continue

for i in range(1, 5):
    if i == 3:
        continue
    print(i)

RESULT:
1
2
4

# Pass

for i in range(1, 5):
    pass

RESULT: (NO RESULT)

for i in range(1, 10):
    if i % 2 == 0:
        pass
    else:
        print(i, end=' ')

RESULT:
1 3 5 7 9

#2) ==>> Palindrome or Not


x = int(input("Enter a Number : "))
x = str(x)
y = int(x[::-1])
x = int(x)
if y == x:
    print("The entered number", x, "is palindrome", type(x))
else:
    print("The entered number", x, "is not palindrome", type(x))

#3) ==>> # Creating a list from input and Entering the Elements in List and sort
         # them in to another 2 list which are prime numbers and not prime numbers.


length = int(input("Enter the length of the list : "))
l3 = []
x = 1
while(x <= length):
    y = int(input("Enter the list element : "))
    l3.append(y)
    x = x + 1
print(l3)
l4 = []
l5 = []
l6 = []
for i in l3:
    if i == 1:
        l6.append(1)
    elif i > 1:
        for j in range(2, i):
            if i % j == 0:
                l4.append(i)
                break
        else:
            l5.append(i)
    else:
        l4.append(i)
print(l4, "are not prime numbers")
print(l5, "are prime numbers")
print(l6, "1 is Neither prime nor Composite")

# 4) Extract Each Digit of an integer in reverse order

num1 = int(input("Enter a Number : "))
while num1 > 0:
    d = num1 % 10
    num1 = num1 // 10
    print(d, end =" ")
print()

# 5) 5 Star Pattern

num = 5
for i in range(num):
    for j in range(0, num-i):
        print("*", end=" ")
    print()

# 6) Multiplication table from 1 to 10

for num in range(1, 21):
    print("Multiplication Table for", num)
    for i in range(1, 11):
        product = num * i
        print(num, 'X', i, '=', product)
    print()

# 7) Mean Median Mode From Given data set (Method - 1)


import math
# Calculating measures of centrality
data = [19, 28, 34, 36, 37, 43, 44, 44, 46, 47, 48, 51, 52, 54, 55, 55, 56, 59, 60, 62, 62, 65, 66, 68]
n = len(data)
print(n)
sum = 0
x = 0
while x < n:
    sum = data[x] + sum
    x += 1
mean = sum / n
print("Mean = ", mean)

# finding median of the data :

if n % 2 == 0:
    p = int(n/2)
    x = data[p-1]
    y = data[p]
    median = (x+y)/2
    print("Median = ", median)
else:
    p = int((n-1)/2)
    median = data[p-1]
    print("Median = ", median)

# Find Mode :

data = [19, 28, 34, 36, 37, 43, 44, 44, 46, 47, 48, 51, 52, 54, 55, 55, 56, 59, 60, 62, 62, 65, 66, 68]
count = []
sort = []
for x in data:
    c = 0
    if x in sort:
        continue
    for y in data:
        if x == y:
            c += 1
    count.append(c)
    sort.append(x)
print("Count ", count)
print("mode ", sort)
mode = []
for g in range(len(count)):
    if count[g] == max(count):
        mode.append(sort[g])
print("Mode = ",mode)

# 8) Mode From PI class method (Method - 2)

count = []
mode = []
for x in data:
    c = 0
    for y in data:
        if x == y:
            c += 1
            count.append(c)
            mode.append(x)
print("count", count)
print("mode", mode)
print(max(count))

ind = 0 # track index of values in count
res = []
for i in count:
    if i == max(count): # if value in count is max then fetch the value from mode
        z = mode[ind]
        if z not in res:
            res.append(z)
        ind += 1
    else:
        ind += 1
print(res)

# 9) Sai Bhargav

data = [19, 28, 34, 36, 37, 43, 44, 44, 46, 47, 48, 51, 52, 54, 55, 55, 56, 59, 60, 62, 62, 65, 66, 68]
n = len(data)
#finding the mode
Count = []
mode = []
x=0
#to get an list with count of values
while x<n:
     y=data[x]
     u=data.count(y)
     Count.append(u)
     x+=1
print(Count)
max = max(Count)
x=0
mode_temp = []
#to get an array with all corresponding index values from 'data'
while x<n:
    if max==Count[x]:
        mode_temp.append(data[x])
        x += 1
    else:
        x += 1
        continue
print(mode_temp)
# To print mode without repeated values only once

for x in mode_temp:
    if x in mode:
        continue
    else:
        mode.append(x)
print(mode)

# 10) Flight ticket 100 for each of the passengers except for age less than or equal 3 find total Total flight charge for all

group = [1, 2, 3, 5, 17, 23, 37, 43]
pay = []
none = []
total = 0
for i in group:
    if i <= 3:
        none.append(i)
    else:
        pay.append(i)
        total = total + 100
print("List of people with age more than 3 = ", pay)
print("List of people with age less than or equal to 3 = ", none)
print("Total flight Charge (100 RS each) = ", total)

# 11)  Given a list l1 = [10, 20, 30, 40, 50, 60], create an another list and print as [20, 30, 40, 50, 60, 10]

l1 = [10, 20, 30, 40, 50, 60]
box1 = []
a = 1
while a <= len(l1):
    if a == len(l1):
        box1.append(l1[0])
    else:
        box1.append(l1[a])
    a = a + 1
print(box1)

# 12) Insert and Pop to Change the Index position on the list

# Example1

l1 = [10, 20, 30, 40, 50, 60]
l1.insert(0, l1.pop(2))
print(l1)

RESULT:
[30, 10, 20, 40, 50, 60]

# Example2

l1 = [10, 20, 30, 40, 50, 60]
l1.insert(0, l1.pop(4))
print(l1)

RESULT:
[50, 10, 20, 30, 40, 60]

# Example3

l1 = [10, 20, 30, 40, 50, 60]
l1.insert(3, l1.pop(5))
print(l1)

RESULT:
[10, 20, 30, 60, 40, 50]


# 12) Tiles and Box problem


roomfloar = 6*5 # In  Sq feet
eastwall = 6*5 # In  Sq feet
westwall = 6*5 # In  Sq feet
northtwall = 5*5 # In  Sq feet
door = 8*3 # In sq feet
doortail = 5*3 # In sq feet
southwall = 5*5 - doortail # In Sq feet
tailsize = 1.5*1 # In sq feet
box = 6*tailsize # In sq feet
totalarea = roomfloar+eastwall+westwall+northtwall+southwall # In sq feet
tails = totalarea/tailsize
totalbox = totalarea/box
print("Tiles size in Sq Feet = ",tailsize)
print("box of tails in Sq Feet = ",box)
print("Total area of tiles in Sq Feet = ",totalarea)
print("Total Number of box required = ",round(totalbox))
print("Total Number of tails required = ",tails)


# 12) Tiles and Box problem with all inputs

l = int(input("Enter the length of floor in feet = "))
w = int(input("Enter the width of floor in feet = "))
h = int(input("Enter the height for which tail is required= "))
h1 = int(input("Enter the height of the door in feet = "))
hd1 = h1-(h1-h)
print("Door Height for which tail is removed = ", hd1)
wd2 = int(input("Enter the width of the door in feet = "))
tl = int(input("Enter the tail length in inch = "))
tw = int(input("Enter the tail width in inch = "))
tlf = tl/12
print("Tail length in feet = ", tlf)
twf = tw/12
print("Tail width in feet = ", twf)
num1 = int(input("How many tails contained in box = "))
roomfloor = l*w # Area In  Sq feet
eastwall = l*h # Area In  Sq feet
westwall = l*h # Area In  Sq feet
northtwall = w*h # Area In  Sq feet
southwall = w*h # Area In  Sq feet
door = hd1*wd2 # Area In  Sq feet
tailsize = tlf*twf # Area In  Sq feet
box = num1*tailsize # Area In  Sq feet
totalarea = roomfloor+eastwall+westwall+northtwall+southwall-door # Total area of tails in sq feet
tails = totalarea/tailsize
totalbox = totalarea/box
print("Tiles size in Sq Feet = ",tailsize)
print("box of tails in Sq Feet = ",box)
print("Total area of tiles in Sq Feet = ",totalarea)
print(totalbox)
print("Total Number of box required = ",round(totalbox))
print("Total Number of tails required = ",tails)



l1 = [10, 20, 30, 40, 50, 60]
box1 = []
a = 1
while a <= len(l1):
    if a == len(l1):
        box1.append(l1[0])
    else:
        box1.append(l1[a])
    a = a + 1
print(box1)

q1 = [44, 55, 66, 77, 88, 99]
box2 = []
n = len(q1)
while n <= 5:
    if n == len(q1):
        box2.append(q1[n])
    else:
        box2.append(q1[len(q1)-n])
    n = n - 1
print(q1)


l2 = [7, 10, 12, 15]
l2.insert(0, l2.pop())
print(l2)



#13) ==>> Fibonacci Series (Method-1)

x = int(input("Enter a Numer : "))
y = 2
n1 = 0
n2 = 1
if x == 0:
    pass
else:
    print("Fibonacci Series : ", n1, end= '')
    while y <= x:
        n3 = n1 + n2
        print(',', n2, end= ' ')
        n1 = n2
        n2 = n3
        y = y+1
print()

#14) ==>> Fibonacci Series (Method-2)

x = int(input("Enter a Numer : "))
n1, n2, y = 0, 1, 2
print("Fibonacci Series : ", n1, end=' ')
while(y <= x):
    n3 = n2 + n1
    print(',', n2, end = ' ')
    n1, n2 = n2, n3
    y = y+1
print()

#15) ==>> Fibonacci Series (Method-3)

x = int(input("Enter a Numer : "))
n1, n2, y = 0, 1, 2
fs = []
print("Fibonacci Series : ", n1, end=' ')
fs.append(n1)
while(y <= x):
    n3 = n2 + n1
    print(',', n2, end = ' ')
    n1, n2 = n2, n3
    y = y+1
print()
print(fs)



#16) ==>> Given a List Create a list of all even numbers and create a list of all odd numbers using for loop

l1 = [10,15,20,25,30,35,40,50]
even = []
odd = []
for i in l1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#17) ==>> Given a List Create a list of all even numbers and create a list of all odd numbers using while loop

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
even = []
odd = []
ln = len(l1)
n = 0
while n < ln:
    if l1[n] % 2 == 0:
        even.append(l1[n])
    else:
        odd.append(l1[n])
    n = n + 1
print(even)
print(odd)


#18) ==>> Given a List Create a list of all even numbers and create a list of all odd numbers using List Comprehension

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
even = [x for x in l1 if x % 2 == 0]
odd = [x for x in l1 if x % 2 != 0]
print(even)
print(odd)

#19) Create Multiplication tables
y = int(input("Enter a Number : "))
l1 = [1,2,3,4,5,6,7,8,9,10]
mul = [x*y for x in l1]
print(mul)


num1 = 5
for i in range(num1):
    print(i)

l1 = [44, 55, 66, 77, 88, 99]
for k in l1:
    print(k)


xi = [8, 12, 16, 20, 32]
for n in xi:
    print(n+1)

#20) Palindrome

a = int(input("Enter a Number : "))
b = a
rev = 0
while b > 0:
    d = b % 10
    rev = rev*10 + d
    b = b // 10
print("The reverse of the number is : ", rev)
if rev == a:
    print("The number", a, "is palindrome")
else:
    print("The number ", a, "is not a palindrome :")

