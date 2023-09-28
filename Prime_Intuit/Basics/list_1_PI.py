# All List Functions

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
l2 = ['a','b','c','d','e', 'abc', 'xyz', 'B', 'G', 'R']

# length function : returns the length of the list
print(len(l1))
print(len(l2))

# max : returns the maximum value in the list
print(max(l1))
print(max(l2))

# min : returns the minimum value in the list
print(min(l1))
print(min(l2))

# list function : convert the tuple/sequence in to the list
t1 = (2, 4, 6)
l3 = list(t1)
print(l3)
print(type(l3))

# pop function : delete the value at the index and returns the value
l3 = [23, 45, 65, 76]
pick = l3.pop(2)
print(pick)
print(l3)

# remove : delete the value from the list
l4 = [34, 65, 96, 54, 76, 73, 34]
l4.remove(34)
rem_item = l4.remove(96)
print("The Removed item =",rem_item)
print(l4)

# reverse : reverse the list
l5 = [34, 65, 96, 54, 76, 73]
l5.reverse()
print(l5)

# sort : sort the data within the list in ascending order
l6 = [34, 53, 23, 12, 30, 23, 65, 77, 88]
l6.sort()
print(l6)

# insert : insert the data element in the index value specified
l6 = [23, 53, 23, 12, 30, 55, 65, 77, 88]
l6.insert(2, 77)
print(l6)

# append : add the data element in to the end of the list
L7 = ['DS', 'AS', 'ER', 'SX', 'QS', 'CV', 'WS']
L7.append('HA')
print(L7)

# clear : clear all the value in the list
L8 = ['AFS', 'AAA', 'KSG', 'JAG']
L8.clear()
print(L8)

# copy : copy the list
L9 = ['AFS', 'AAA', 'KSG', 'JAG', 'VGHV', 'JVHA']
L10 = L9
L11 = L9.copy()
print(L9)
print(L10)
print(L11)
l1 = [23, 34, 54, 67, 87, 95, 76]

# Indexing in List

print(l1[:4])
print(l1[2:4])
print(l1[:])
print(l1[2:])
print(l1[::-1])

# Replacing a element in the string

l1[6] = 77
print(l1)

# Adding an element to the end of the list
l1.append(52)
print(l1)

box1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Using step to create odd number
print(box1[1::2])

# Using step to create even number
print(box1[0::2])

# Using step to create even number
print(box1[::2])

# Length function
print(len(box1))

# Conatinating two list
box2 = [14, 15, 16, 17, 18, 19, 20]

print(box1 + box2)

box1.append(13)

new_box = box1 + box2
print(new_box)

box1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(len(box1))
print("Printing all indivisual list items below")
for i in box1:
    print(i, end=" ")
print()

# Swap the values of the first nd last item

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

# Find the second highest in the list

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


# Find the second highest in the list Without using max function

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

# List comprehension, Concise way of creating a new list using existing iterable

l1 = [2, 4, 6, 8]
l2 = [x**2 for x in l1] # List Comprehension using l1 to create a list l2 of square values
print(l1,'\n',l2) # \n indicates that the subsequent part of the print statement


# Mean, Variance, Standard Deviation

import math
m = 5 # Mean of the l1

l3 = [(x-m)**2 for x in l1]
print(l3)
var = (1/(len(l1)-1)) * (sum(l3))
print("Variance", var)
print("Standard Deviation = ", math.sqrt(var))
