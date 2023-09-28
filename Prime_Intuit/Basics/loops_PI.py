

# For loop

# Example - 1
box1 = ["apple", "banana", "grapes", "jackfruit", "mango", "orange"]
for fruits in box1:
    print(fruits)
print()

# Example - 2
box2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in box2:
    if num % 2 == 0:
        print(num)
print()

# Example - 3
box2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in box2:
    if num % 2 != 0:
        print(num, end = " ") # Here we use end to give space after printing a number and don't go for next line
print()

# Example - 4
len = int(input("Enter the length of the list : "))
l4 = []
for num in range(len):
    item = int(input("Enter the list element : "))
    l4.append(item)
print(l4)

# Example - 5
box2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = []
l2 = []
for num in box2:
    if num % 2 == 0:
        l1.append(num)
    else:
        l2.append(num)
print("Even number", l1)
print("Odd number", l2)

# Example - 6
num2 = int(input("enter a number: "))
if num2 > 1:
    for i in range(2, num2):
        if num2 % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

# While loop

# initializing x as 1
length = int(input("Enter the length of the list : "))
l3 = []
x = 1
while(x <= length):
    item = int(input("Enter the list element : "))
    l3.append(item)
    x = x + 1
print(l3)

# initializing x as 0
length = int(input("Enter the length of the list : "))
l3 = []
x = 0
while(x < length):
    item = int(input("Enter the list element : "))
    l3.append(item)
    x = x + 1
print(l3)

# Check number is prime or not using while loop method - 1

num2 = int(input("enter a number: "))
n = 2
flag = 0 # Asuming the number is prime
while n < num2:
    if num2 % n == 0:
        flag = 1
    n += 1
if flag == 0 and num2 != 0 and num2 != 1:
    print(num2, "Is a prime Number")
else:
    print(num2, "Is not a prime Number")


# Check number is prime or not using while loop method - 2

check_number = int(input("enter a number: "))
n = 2
is_prime = True
while n < check_number:
    if check_number % n == 0:
        is_prime = False
        # comes out for the loop if check_number is divisible by 2 or divisible by any numbers between 2 and check_number
        break
    n += 1
if check_number <= 1:
    print(f"{check_number} Is is not a prime Number")
elif is_prime:
    print(f"{check_number} Is a prime Number")
else:
    print(f"{check_number} Is is not a prime Number")


num = 7536
num = str(num)
num1 = num[::-1]
print(num1)
for i in num1:
    print(int(i), end = " ")

print()

box1 = [2,4,6,8,10]
box2 = [22,44,66,88,100]

a = box2[4]
print(a)
x = box1.index(10)
print(x)
z = box2[box1.index(6)]
print(z)
