# String Functions

# convert first character of a string to upper character
x = "the sea is calm today"
print(x.capitalize())
# OUTPUT : The sea is calm today

# entire string is converted in to upper case
x = "the sea is calm today"
print(x.upper())
# OUTPUT : THE SEA IS CALM TODAY

# entire string is converted in to lower case
z = "CONSISTENCY"
print(z.lower())
# OUTPUT : consistency

# will return true if all the characters are upper case
# will return false if any one of the character is lower case
z = "CONSISTENCY"
print(z.isupper())
# OUTPUT : True

x = "The Sea is calm TODAY"
print(x.isupper())
# OUTPUT : False

# will return true if all the characters are lower case
# will return false if any one of the character is upper case
x = "the sea is calm today"
print(x.islower())
# OUTPUT : True


# position the string in the center
pi = " PRIME-INTUIT "
print(pi.center(20, "%"))
# OUTPUT : %%% PRIME INTUIT %%%

# return true if sting contain only alfabet and numeric without space
box1 = "god77"
print(box1.isalnum())
# OUTPUT : True

box2 = "cat@#98"
print(box2.isalnum())
# OUTPUT : False

box2 = "cat 88"
print(box2.isalnum())
# OUTPUT : False

# return true if sting contain only numeric without space
num = "012345679"
print(num.isdigit())
# OUTPUT : True

num1 = "47ABC"
print(num1.isdigit())
# OUTPUT : False

# return true if sting contain only alfabet without space
box2 = "cat"
print(box2.isalpha())
# OUTPUT : True

box = "cat and dog"
print(box.isalpha())
# OUTPUT : False

# return true if sting contain only numeric without space
num = "012345679"
print(num.isdigit())
# OUTPUT : True

num1 = "67 23"
print(num1.isdigit())
# OUTPUT : False

# returns the number of times a specified value occurs in the string
a = 'Today is good day'
print(a.count('o'))
# OUTPUT : 3

fruits = "i love apples, apples are my favorite fruit"
print(fruits.count("apple"))
# OUTPUT : 2

# returns the encoded version of the string
a = "today is sunday"
print(a.encode())
# OUTPUT : b'today is sunday'

# returns true if string ends with specified value
x = "the sea is calm today"
print(a.endswith("y"))
# OUTPUT : True

# search the string for the specified value and returns position of where it was found
y = "Nothing is Impossible"
print(y.find("I"))
# OUTPUT : 11

y = "Nothing Is Impossible"
# Give the result of the first occurrence
print(y.find("I"))
# OUTPUT : 8

# format method return the formatted string
txt1 = "for only {price:.2f} dollars!"
print(txt1.format(price=49))
# OUTPUT : for only 49.00 dollars!

print("My name is %s and I weigh %d" % ("Chandan", 7))
# OUTPUT : My name is Chandan and I weigh 7

# returns true if all the character s in the string are decimal
box3 = "9177"
print(box3.isdecimal())
# OUTPUT : True

box4 = "91.77"
print(box4.isdecimal())
# OUTPUT : False

# returns true if all the character s in the string are numeric
box5 = "9177"
print(box5.isnumeric())
# OUTPUT : True

box6 = "91.77"
print(box6.isnumeric())
# OUTPUT : False

# returns true if string contain only white space
box4 = "  "
print(box4.isspace())
# OUTPUT : True

box5 = "cat dog"
print(box5.isspace())
# OUTPUT : False

# join the elements of the iterable to the end of the string
myTuple = ("apple", "mango", "grapes")
print("&".join(myTuple))
# OUTPUT : apple&mango&grapes

list1 = ["one", "two", "three", "four", "five"]
print("_".join(list1))
# OUTPUT : one_two_three_four_five

list1 = ["one", "two", "three", "four", "five"]
print("_".join(list1[:3]))
# OUTPUT : one_two_three

# returns the left trim version of a string
a = "   today is sunday"
print(a.lstrip())
# OUTPUT : today is sunday

# remove white spaces before strings
a = "     today is sunday"
print(a.strip())
# OUTPUT : today is sunday

# Split the string at the specified separator and returns a list
txt = "welcome to the jungle"
l1 = txt.split()
print(l1)
# OUTPUT : ['welcome', 'to', 'the', 'jungle']

txt1 = "Prime-Intuit-The-Finishing-School"
l2 = txt1.split('-')
print(l2)
# OUTPUT : ['Prime', 'Intuit', 'The', 'Finishing', 'School']

# List Functions

# length function : returns the length of the list
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
l2 = ["ab", "cd", "ef", "gh"]
l3 = ["cat", "dog", "cow", 5, 6, 7]
print(len(l1))
print(len(l2))
print(len(l3))

# OUTPUT : 8
# OUTPUT : 4
# OUTPUT : 6

# max : returns the maximum value in the list
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
l2 = ["ab", "cd", "ef", "gh"]

print(max(l1))
print(max(l2))

# OUTPUT : 80
# OUTPUT : gh

# min : returns the minimum value in the list
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
l2 = ["ab", "cd", "ef", "gh"]

print(min(l1))
print(min(l2))

# OUTPUT : 10
# OUTPUT : ab

# pop function : delete the value at the index and returns the value
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
y = l1.pop(2)
print(y)
print(l1)

# OUTPUT : 30
# OUTPUT : [10, 20, 40, 50, 60, 70, 80]

l2 = ["ab", "cd", "ef", "gh"]
y = l2.pop(2)
print(y)
print(l2)

# OUTPUT : ef
# OUTPUT : ['ab', 'cd', 'gh']

# remove : delete the value from the list
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
y = l1.remove(30)
print(l1)
print(y)

# OUTPUT : [10, 20, 40, 50, 60, 70, 80]
# OUTPUT : None

l4 = [45, 35, 74, 64, 87, 77]
l4.remove(35)
print(l4)
# OUTPUT : [45, 74, 64, 87, 77]

# reverse : reverse the list
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
l1.reverse()
print(l1)
# OUTPUT : [80, 70, 60, 50, 40, 30, 20, 10]

# sort : sort the data within the list in ascending order
l5 = [5, 7, 2, 6, 8, 0]
l5.sort()
print(l5)
# OUTPUT : [0, 2, 5, 6, 7, 8]

# insert : insert the data element in the index value specified
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
l1.insert(2, 25)
print(l1)
# OUTPUT : [10, 20, 25, 30, 40, 50, 60, 70, 80]

# append : add the data element in to the end of the list
l4 = [45, 35, 74, 64, 87, 77]
l4.append(77)
print(l4)
# OUTPUT : [45, 35, 74, 64, 87, 77, 77]

# clear : clear all the value in the list
l4 = [45, 35, 74, 64, 87, 77]
l4.clear()
print(l4)
# OUTPUT : []

# count : count the number of times specified value occurs in the list
l4 = [45, 35, 74, 64, 87, 77, 77]
a = l4.count(77)
print(a)
# OUTPUT : 2

# index : returns the index position of the element
l4 = [45, 35, 74, 64, 87, 77, 77]
a = l4.index(87)
print(a)
# OUTPUT : 4

# copy : make a copy of a list
l4 = [45, 35, 74, 64, 87, 77, 77]
# Shallow copy
l5 = l4
print(l4)
print(l5)

# OUTPUT : [45, 35, 74, 64, 87, 77, 77]
# OUTPUT : [45, 35, 74, 64, 87, 77, 77]

l1 = [10, 20, 30, 40, 50, 60, 70, 80]
# Deep copy
l2 = l1.copy()
print(l1)
print(l2)

# OUTPUT : [10, 20, 30, 40, 50, 60, 70, 80]
# OUTPUT : [10, 20, 30, 40, 50, 60, 70, 80]

# add elements of one list to another
l4 = [45, 35, 74, 64, 87, 74]
l5 = [75, 76, 77]
l4.extend(l5)
print(l4)
# OUTPUT : [45, 35, 74, 64, 87, 74, 75, 76, 77]

# delete an element of list
l4 = [45, 35, 74, 64, 87, 74]
del(l4[0])
print(l4)
# OUTPUT : [35, 74, 64, 87, 74]

# delete the entire list
l1 = [10, 20, 30, 40, 50, 60, 70, 80]
del(l1)

# Dict functions

# Creating dictionary using zip function and list

l3 = [5, 6, 7, 8, 9, 10]
l4 = [45, 35, 74, 77]
d1 = dict(zip(l3, l4))
print(d1)
# OUTPUT : {5: 45, 6: 35, 7: 74, 8: 77}

l3 = [5, 6, 7, 8, 9, 10]
l4 = [45, 35, 74, 77, 77, 77]
d1 = dict(zip(l3, l4))
print(d1)
# OUTPUT : {5: 45, 6: 35, 7: 74, 8: 77, 9: 77, 10: 77}

# Retrieving all the keys
d2 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77}
x = list(d2.keys())
print(x)
# OUTPUT : [5, 6, 7, 8, 9, 10]

# Retrieving all the values
d2 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77}
x = list(d2.values())
print(x)
# OUTPUT : [45, 35, 74, 64, 87, 77]

# Retrieving all the items
d2 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77}
x = list(d2.items())
print(x)
# OUTPUT : [(5, 45), (6, 35), (7, 74), (8, 64), (9, 87), (10, 77)]

# From keys - creating a dic with other iterables
l4 = [45, 35, 74, 77, 77, 77]
t1 = (100, 200)
d3 = {}
d3 = d3.fromkeys(l4, t1)
print(d3)
# OUTPUT : {45: (100, 200), 35: (100, 200), 74: (100, 200), 77: (100, 200)}

# update - update the dictionary with specified item
d2 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 74}
d2.update({12:77})
print(d2)
# OUTPUT : {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 74, 12: 77}

# pop - remove the items with specified key name
d2 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}
d2.pop(5)
print(d2)
# OUTPUT : {6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}

# popitem - remove last item
d2 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}
d2.popitem()
print(d2)
# OUTPUT : {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77}

# copy - copy a dict
d2 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}
d3 = d2.copy()
print(d2)
print(d3)
# OUTPUT : {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}
# OUTPUT : {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}

# update - update one dictionary items to another
d2 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}
d3 = {}
d3.update(d2)
print(d3)
# OUTPUT : {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}

d2 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}
d3 = {200: 300, 5: 50}
d3.update(d2)
print(d3)
# OUTPUT : {200: 300, 5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}

# get - returns the value of the specific key
d2 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}
value = d2.get(10)
print(value)
# OUTPUT : 77

# clear - clear the dic items
d3 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}
d3.clear()
print(d3)
# OUTPUT : {}

# setdefault - set default value if key does not exist
d3 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}
d3.setdefault(14, 77)
print(d3)
# OUTPUT : {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85, 14: 77}

d3 = {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85}
d3.setdefault(5, 77)
print(d3)
# OUTPUT : {5: 45, 6: 35, 7: 74, 8: 64, 9: 87, 10: 77, 12: 85, 14: 77}

