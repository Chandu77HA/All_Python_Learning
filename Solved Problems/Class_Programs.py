# 1) Swap the values of the first and last item

# Using while loop

length = int(input("Enter the length of the list : "))
l3 = []
x = 1
while(x <= length):
    y = int(input("Enter the list element : "))
    l3.append(y)
    x = x + 1
print(l3)
a = l3[0]
l3[0] = l3[length-1]
l3[length-1] = a
print(l3)

# Using for loop

len_of_list = int(input("Enter the length of the list : "))
number_list = []
for i in range(len_of_list):
    list_item = int(input(f"Enter the list Element {i+1} : "))
    number_list.append(list_item)
print("List before Swapping : ", number_list)

swap_item = number_list[0]
number_list[0] = number_list[len_of_list-1]
number_list[len_of_list-1] = swap_item
print("List after Swapping : ", number_list)

# 2) Find the second highest in the list

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


# Bubble sor method
number_list = [23, 97, 23, 123, 76, 88]
for index in range(0, len(number_list)):
    for position in range(index+1, len(number_list)):
        if number_list[position] < number_list[index]:
            move_item = number_list[position]
            number_list[position] = number_list[index]
            number_list[index] = move_item
print("The sorted list is : ", number_list)
print("The second largest index is : ", len(number_list)-2)
print("The second largest element in the list is : ", number_list[len(number_list)-2])

# Looping and keeping the track

'''
In the find_second_highest function, the line highest = second_highest = float('-inf') initializes two variables, highest and second_highest, both to negative infinity (float('-inf')). Here's what this does:

It sets both highest and second_highest to a value that is lower than any real number you would typically find in a list of numbers. This ensures that any value encountered in the list will be greater than or equal to these initial values during the loop.

The reason for initializing both variables to the same value is to ensure that they are both initially the same. As we iterate through the list, we will update these variables accordingly to track the highest and second highest values.

Here's how it works in the loop:

If we encounter a number greater than the current highest, we update second_highest to the current value of highest and then update highest to the new number.

If we encounter a number that is greater than the current second_highest but less than highest, we update second_highest to the new number.

By initializing both variables to negative infinity, we ensure that even if the list contains negative numbers, the algorithm will correctly find the second highest positive number (or the second lowest negative number) in the list.'''

def find_second_highest(numbers):
    if len(numbers) < 2:
        return "List must have at least two elements"
    
    highest = second_highest = float('-inf')
    
    for num in numbers:
        if num > highest:
            second_highest = highest
            highest = num
            print(f"If - The loop of {num} the second_highest = {second_highest}, highest = {highest}")
        elif num > second_highest and num < highest:
            second_highest = num
            print(f"Elif - The loop of {num} the second_highest = {second_highest}")
    
    return second_highest

# Example usage1:
my_list = [10, 5, 8, 20, 15]
result = find_second_highest(my_list)
print("Second highest element:", result)


# Example usage2:
my_list = [12, 25, 34, 54, 97, 54, 43, 86, 14]
result = find_second_highest(my_list)
print("Second highest element:", result)

# 3) Find the second highest in the list and its index without using max function


length = int(input("Enter the length of the list : "))
l4 = []
x = 1
while x <= length:
    y = int(input("Enter the list element : "))
    l4.append(y)
    x = x + 1
print(l4)
print(len(l4))

max1 = l4[0]
x = 1
ind = 0
while x < len(l4):
    if max1 < l4[x]:
        max1 = l4[x]
        ind = x
    x = x + 1
print(max1, ind)

del(l4[ind])
print(l4)

max1 = l4[0]
x = 1
ind = 0
while x < len(l4):
    if max1 < l4[x]:
        max1 = l4[x]
        ind = x
    x = x + 1
print(max1, ind)

# Method - 2

my_list = [12, 25, 34, 54, 97, 54, 43, 86, 14]
first_max = second_max = my_list[0]
for num in my_list:
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max and num < first_max:
        second_max = num

print("first_max = ", first_max)
print("second_max = ", second_max)

# 4) Swapping two Numbers Based on Multiple assignment(Method -1)

a, b = 4, 8
a, b = b, a
print(a,b)

# 5) Swapping two Numbers using third variable (Method -2)

a, b = 10, 23
c = a
a = b
b = c
print(a,b)

# 6) Swapping two Numbers using addition (Method -3)

a, b = 12, 14
a = a + b #26
b = a - b #12
a = a - b #14
print(a, b)

# 7) Swapping two Numbers using multiplication and division (Method -4)

a, b = 10, 5
a = a * b #50
b = a / b #10
a = a / b #5
print(a, b)

# 8) Swapping two Numbers using multiplication and division (Method -5)

a, b = 100, 50
a = a / b #2
b = a * b #100
a = b / a #50
print(int(a), int(b))

# 9) Print maximum of three numbers

a = int(input("Enter number1 : "))
b = int(input("Enter number2 : "))
c = int(input("Enter number3 : "))

if a >= b and a >= c:
    print("Max number is : ", a)
elif b >= a and b >= c:
    print("Max number is : ", b)
else:
    print("Max number is : ", c)

# 10) maximum of three numbers and in descending order

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


# 11) Maximum of three numbers

a = int(input("Enter number1 : "))
b = int(input("Enter number2 : "))
c = int(input("Enter number3 : "))

# Case1 : a = b  = c

if a == b == c:
    print("all three numbers are same")

# Case2 : a = b  or b = c or c = a
elif a == b:
    if a > c:
        print("Max number is a, b ", a)
    else:
        print("Max number is c", c)
elif b == c:
    if b > a:
        print("Max number is b, c ", b)
    else:
        print("Max number is a", a)
elif c == a:
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

# 12) program to check prime number or not

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

# 13) program to check prime number or not

pi = 3.142
r = float(input("enter the radius is cms : "))
# area of the circle:
area = pi*r**2
print("area of the circle is : ", r, "is", area)
# perimeter of the circle:
per = 2 * pi * r
print("perimeter of the circle is : ", r, "is", per)
# volume of the sphere:
vol = (4/3)*(pi*r**3)
print("volume of the sphere is : ", r, "is", vol)
surf = 4 * pi * r**2
print("surface area of the circle is : ", r, "is", surf)




# 15) To Check Prime number or not with while loop method

num2 = int(input("enter a number: "))
if num2 == 1:
    print(num2, "Is a prime Number")
else:
    n = 2
    flag = 0
    while n < num2:q
        if num2 % n == 0:
            flag = 1
        n += 1
    if flag == 0:
        print(num2, "Is a prime Number")
    else:
        print(num2, "Is a not a prime Number")

# 16) Program to print a prime number from a list of a number

length = int(input("Enter the length of the list : "))
l3 = []
x = 1
while(x <= length):
    y = int(input("Enter the list element : "))
    l3.append(y)
    x = x + 1
print(l3)
flag1 = 0 # not a prime number
for i in l3:
    n = 2
    flag = 0
    while n < i:
        if i % n == 0:
            flag = 1
        n += 1
    if flag == 0:
        print(i, end = " ")
        flag1 = 1
print(' ')
if flag1 == 0:
    print("List does not contain Prime Number")

# Bubble Sort Chatgpt code ascending order

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize the algorithm by stopping early if no swaps are made
        swapped = False
        print(f"{i} cycle of outer loop")
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # If the element found is greater than the next element, swap them
            print(f"the {j} index and element = {arr[j]}")
            if arr[j] > arr[j+1]:
                print(f"swapping of {arr[j]} and {arr[j+1]}")
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
                print(arr)
                swapped = True
                
        
        # If no two elements were swapped in the inner loop, the list is already sorted
        if not swapped:
            print("yes break")
            break

# Example usage 1:
my_list = [64, 25, 12, 22, 11]
bubble_sort(my_list)
print("Sorted list:", my_list)

# Example usage 1:
L1 = [13, 24, 35, 97, 47]
bubble_sort(L1)
print("Sorted list:", L1)


# Bubble Sort Chatgpt code descending order

def bubble_sort_descending(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize the algorithm by stopping early if no swaps are made
        swapped = False
        print(f"{i} cycle of outer loop")
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # If the element found is less than the next element, swap them
            print(f"the {j} index and element = {arr[j]}")
            if arr[j] < arr[j+1]:  # Change the comparison to less than
                print(f"swapping of {arr[j]} and {arr[j+1]}")
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
                print(arr)
                swapped = True
                
        
        # If no two elements were swapped in the inner loop, the list is already sorted
        if not swapped:
            print("yes break")
            break

# Example usage:
my_list = [64, 25, 12, 22, 11]
bubble_sort_descending(my_list)
print("Sorted list (descending order):", my_list)


# Check the number is prime number or not method- 1

def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # The number is divisible by 'i', so it's not prime
    
    return True  # If no divisors were found, the number is prime

# Example usage:
num = 17  # Replace this with the number you want to check
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Check the number is prime number or not method- 2

def prime_check(number):
    if number <= 1:
        return False # Numbers less than or equal to 1 are not prime
    
    for i in range(2, number):
        if number % i == 0:
            return False # The number is divisible by 'i', so it's not prime
        
    return True  # If no divisors were found, the number is prime
    
# Example usage:
num = 2  # Replace this with the number you want to check
if prime_check(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Program to print a prime number from a list of a number and seperate prime and not-prime to another list

length = int(input("Enter the length of the list: "))
Numbers_List = []
x = 1
while x <= length:
    list_item = int(input("Enter the list element: "))
    Numbers_List.append(list_item)
    x = x + 1
print(Numbers_List)

Prime_Numbers_List = []
Non_Prime_Numbers_List = []

for row in Numbers_List:
    divisor_check = 2
    flag = 1  # Assume the number is prime
    while divisor_check <= row ** 0.5:  # Optimize the divisor range
        if row % divisor_check == 0:
            flag = 0
            Non_Prime_Numbers_List.append(row)
            break
        divisor_check += 1
    if flag == 1:
        Prime_Numbers_List.append(row)

if not Prime_Numbers_List:
    print("List does not contain Prime Numbers")
else:
    print("List contains Prime Numbers")

if Prime_Numbers_List:
    print("Sorted prime numbers list:", Prime_Numbers_List)

print("Sorted non-prime numbers list:", Non_Prime_Numbers_List)



# program to check number of vowels using sets in given string

str1 = "Only desired action produces results"
vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0
for i in str1.lower():
    if i in vowels:
        count = count+1
print("The number of Vowels in String = ", count)

# program to check number of vowels using sets in given string

str1 = "Deep Knowledge Group"
vowels = {'a', 'e', 'i', 'o', 'u'}
count_v = 0
count_c = 0
for i in str1.lower():
    if i in vowels:
        count_v = count_v + 1
    else:
        count_c = count_c + 1
print("The number of Vowels in String =", count_v)
print("The number of Vowels in String =", count_c)




# Python Program to Give Concatenated string with uncommon characters in 2 strings

# Method -1

str2 = "words only have power"
str3 = "when turned in to action"
print("slyvptuic")
all2 = list(set(str2) & set(str3))
all1 = list(set(str2).intersection(set(str3)))
print(all2)
print(all1)

str4 = str2 + str3
print(str4)
res = []
for x in str4:
    if x not in all1:
        if x not in res:
            res.append(x)
print("The Uncommon words are ="," ".join(res))

# Method -2
print(set(str2).symmetric_difference(set(str3)))
un_com_set =set(str2).symmetric_difference(set(str3))
un_com_list = list(un_com_set)
print(un_com_set)
print(un_com_list)
joined_string = ''.join(un_com_list)
print("The Uncommon words are =",joined_string)



#1) ==>> To check the single character is Vowel or Consonant

xyz = input("Enter a Character to Check Vowel or Consonant : ")

if (xyz == 'a' or xyz == 'e' or xyz == 'i' or xyz == 'o' or xyz == 'u' or xyz == 'A' or xyz == 'E' or xyz == 'I' or xyz == 'O' or xyz == 'U'):
    print("Given Character ", xyz , "is vowel")
# To reduce the length of a program all consonants are not mentioned inside elseif
elif (xyz == 'c' or xyz == 'd' or xyz == 'h' or xyz == 'f' or xyz == 'g'):
    print("Given Character ", xyz, "is consonant")
else:
    print(xyz, "Is not a valid character")




#2) ==>> Missing Number in the list

xyz = [1, 4, 2, 6, 8, 9, 10]
abc = [x for x in range(max(xyz)) if x not in xyz]
print(abc)


#3) ==>> Max of three numbers(Method-1)

n1 = 35
n2 = 25
n3 = 44
num = max(n1, n2, n3)
print(num)


#4) ==>> Sorting without sort function
box = [4, 3]
for i in range(0, len(box)):
    for j in range(0, len(box)):
        if box[i] < box[j]:
            box[i], box[j] = box[j], box[i]
print(box)
