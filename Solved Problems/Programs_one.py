
# 1) Write a program to check whether a year is leap year or not.

year = int(input("Enter the year: "))
if (year % 400) == 0:
    print("The year is leap year")
elif year % 4 == 0 and year % 100 != 0:
    print('The year is leap year')
else:
    print("Given year is not leap year")

# 2) Prime Number using for loop

num = int(input("Enter a Number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not A Prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")


# 3) Prime Number using while loop

num = int(input("enter a number: "))
n = 2
flag = 0
# assume the number is prime
while n < num:
    if num % n == 0:
        flag = 1
    n += 1
if flag == 0:
    print(num, "Is a prime Number")
else:
    print(num, "Is a not a prime Number")

# 4) Program to print a prime number from a list of a number and to check if the list contain prime numbers or not

length = int(input("Enter The Length Of the List : "))
x = 1
l3 = []
while x <= length:
    y = int(input("Enter the element of the list : "))
    l3.append(y)
    x += 1
print(l3)
flag1 = 1
# Assume The list Doesn't contain prime number
for num in l3:
    n = 2
    flag = 0
    # The num is prime number
    while n < num:
        if num % n == 0:
            flag = 1
        n = n + 1
    if flag == 0:
        print(num, end=' ')
        flag1 = 0
print()
if flag1 == 0:
    print('The list contain prime number')
else:
    print('The list does not contain prime number')


# 5) Check number of vowels and consonants

name = input("Enter any String : ")
vowels = 0
consonants = 0
for n in name:
    if n in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        vowels += 1
    elif n.isalpha():
        consonants += 1
print("Number of Vowels are : ", vowels, "Number of Consonants are", consonants)

# 6) Fibonacci number

n = int(input("Enter a number : "))
a, b, i = 0, 1, 1
while i <= n:
    print(a, end=' ')
    a, b, i = b, a+b, i + 1

# 6) Fibonacci number using functions

def fibo(n):
    a, b, i = 0, 1, 1
    while i <= n:
        yield a
        a, b, i = b, a + b, i + 1

# 6) Fibonacci number limit

lim = int(input("Enter a number : "))
n1, n2 = 0, 1
while a <= lim:
    print(a, end=' ')
    n1, n2 = n2, n1 + n2
# 6) Fibonacci number limit using functions

def fibo(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

y = list(fibo(20))
print(y)

# 7) Check List items are prime number or not

l3 = [5, 7, 10]

count = 0
for i in l3:
    for j in range(2, i):
        if i % j == 0:
            count = count + 1
    if count == 1:
        print(i, end = '')
if count == 0:
    print("All the List items are prime number")
else:
    print("All the List items are not prime number")

# 8) Check a number is palindrome or not.

n = 767
m = n
sum_n = 0
while m != 0:
    d = m % 10
    sum_n = sum_n * 10 + d
    m = m // 10
if sum_n == n:
    print("Yes the Number is Palindrome")
else:
    print("The Number is not a Palindrome")

# 9) To check the number of Vowels and Consonants

name = input("Enter any String : ")
vowels = 0
consonants = 0
for n in name:
    if n in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        vowels += 1
    elif n.isalpha():
        consonants += 1
print("Number of Vowels are : ", vowels, "Number of Consonants are", consonants)


# 11) Find the second highest in the list

length = int(input("Enter the length of the list : "))
l4 = []
x = 1
while(x <= length):
    y = int(input("Enter the list element : "))
    l4.append(y)
    x = x + 1
print(l4)
l4.remove(max(l4))
print(l4)
print(max(l4))

# 11) Find the second highest in the list - using sort method

l4 = [52, 35, 46, 54, 45, 77, 45, 99]
l4.sort()
print(l4)
print(len(l4))
print(l4[len(l4) - 2])
print(l4[-2])
# 12) Find the second highest in the list without using max function

length = int(input("Enter the length of the list : "))
l4 = []
x = 1
while(x <= length):
    y = int(input("Enter the list element : "))
    l4.append(y)
    x = x + 1
print(l4)
print(len(l4))

max = l4[0]
x = 1
ind = 0
while x < len(l4):
    if max < l4[x]:
        max = l4[x]
        ind = x
    x = x + 1
print(max, ind)

del(l4[ind])
print(l4)

max = l4[0]
x = 1
ind = 0
while x < len(l4):
    if max < l4[x]:
        max = l4[x]
        ind = x
    x = x + 1
print(max, ind)

# 13) Given a List Create a list of all even numbers and create a list of all odd numbers using List Comprehension

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
even = [x for x in l1 if x % 2 == 0]
odd = [x for x in l1 if x % 2 != 0]
print(even)
print(odd)

# 14) Create Multiplication tables

y = int(input("Enter a number :"))
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mul = [x*y for x in l1]
print(mul)

y = int(input("Enter a number :"))
for x in range(1, 11):
    print(y*x,' ', end='')

# 15) Swapping two Numbers Based on Multiple assignment(Method -1)

a, b = 10, 5
a, b = b, a
print(a,b)

# 16) Swapping two Numbers using third variable (Method -2)

a, b = 10, 23
c = a
a = b
b = c
print(a,b)

# 17) Swapping two Numbers using multiplication and division (Method -4)

a, b = 10, 5
a = a * b
# 50
b = a / b
# 10
a = a / b
# 5
print(a, b)

# 18) Find Max of two numbers

ab = 25
bb = 30
if ab > bb:
    print("Max Number is : ", a)
else:
    ab < bb
    print("Max Number is : ", b)

# 19) Print maximum of three numbers

a = int(input("Enter number1 : "))
b = int(input("Enter number2 : "))
c = int(input("Enter number3 : "))

if a >= b and a >= c:
    print("Max number is : ", a)
elif b >= a and b >= c:
    print("Max number is : ", b)
else:
    print("Max number is : ", c)

# 20) maximum of three numbers and in descending order

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


# 21) Given a String Write a program to print the second characters of 1, 3, 5, 7 etc Continue...

txt = "Prime Intuit The Finishing Best School"
b = txt.split()
print(b)
a = b[0::2]
print(a)
for i in a:
    print(i[1])

# OR

txt = "Prime Intuit The Finishing Best School"
b = txt.split()
print(b)
i = 0
while i < len(b):
    c = b[i]
    print(c[1])
    i = i + 2

# Count vowels

name = input("Enter any String : ")
vowels = 0
consonants = 0
l1 = []
for n in name:
    if n not in l1:
        if n in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            vowels += 1
            l1.append(n)
print(vowels)

# Reverse the string

a = "Data is Vital"
l1 = a.split()
print(l1)
l1.reverse()
print(l1)
print(" ".join(l1))




L2 = [24, 10, 35, 65, 77, 41, 2, 21, 14, 9, 41]

print("Before Sorting The Array Elements : ")
for i in L2:
    print(i, end=" ")
print()
print(len(L2))

# During every loop the lowest element is moved to left position of the list
# During First loop first lowest element is moved to the left position of the list
# During Second loop first lowest element is moved to the left position of the list

for i in range(0, len(L2)):
    print(f"Loop Starting With {i}th Element {L2[i]} of the List")
    for j in range(i+1, len(L2)):
        if L2[j] < L2[i]:
            temp = L2[j]
            L2[j] = L2[i]
            L2[i] = temp
        print("During loop", L2)
print()
print("After Sorting The Array Elements : ")
for i in L2:
    print(i, end=" ")



def bubble_sort(array):
    print("Before Sorting The Array Elements : ")
    for i in array:
        print(i, end=" ")
    print()

    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    print()

    print("After Sorting The Array Elements : ")
    for i in array:
        print(i, end=" ")
    print()


L2 = [24, 35, 65, 77, 41, 21, 14, 41]
bubble_sort(L2)

print()

L3 = [12, 34, 45, 32, 65, 76, 43, 56, 4]
for i in range(0, len(L3)):
    for j in range(i+1, len(L3)):
        if L3[j] < L3[i]:
            temp = L3[j]
            L3[j] = L3[i]
            L3[i] = temp

print("The sorted list", L3)