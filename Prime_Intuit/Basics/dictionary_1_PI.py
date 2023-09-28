# Creating an empty dictionary
dict12 = {}

# Adding values to the dictionary
dict12["Name"] = "Chandan"
dict12["Age"] = 26
dict12["Weight"] = 71
print(dict12)

# Accessing a values from a dictionary
print(dict12["Name"])

# creating dictionary with values
d1 = {'AMS':'afbs', 'MAHS':'dfbb', 'MNXA':'csdfb', 'NBVJ':'dsds', 'MAAJ':'esdb'}
print(d1['MAHS'])

# creating dictionary with other iterables
l1 = [4, 6, 7, 8, 9]
l2 = [x**2 for x in l1]
d2 = {}
d2 = d2.fromkeys(l1, 'a')
print(d2)
d6 = {}
d6 = d6.fromkeys(l1, l2)
print(d6)

# Using list for both keys and values
L3 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
L4 = ['Apple', 'Mango', 'Grapes', 'Guva', 'Orange', 'Coko', 'Nuts']

d3 = dict(zip(L3, L4))
print(d3)


# Zip function can be also used to create a list that contain tuples from 2 iterables
l1 = [4, 6, 7, 8, 9]
l2 = [16, 36, 49, 64, 81]
l3 = (34, 45, 64, 87, 97)
l4 = list(zip(l1, l2, l3))
print(l4)

# Zip function for uneven length of iterables (length of zip obj = len of shortest iterables)
box2 = [4, 7, 8]
box3 = ['abc', 'def', 'ghi', 'jkl', 'mno']
box5 = list(zip(box2, box3))
print(box5)

# Retrieving all the keys
l1 = list(d1.keys())
print(l1)

# Retrieving all the values
l2 = list(d1.values())
print(l2)

print("d1 is = ", d1)

print(d1)
for i in d1:
    print(i, end=' ') # to fetch keys
print()

for i in d1:
    print(d1[i], end=' ') # to fetch values
print()

# Looping example

d2 = {1: 'a', 2: 'a', 3: 'a', 4: 'a', 5: 'a'}
l2 = [1, 4, 9, 16, 25]

print("The d2 is =", d2)

for i in d2:
    print(i, end = ' ')
    print(d2[i])
    d2[i] = l2[i - 1]

print("The updated d2 is =", d2)


# Another Example

l3 = ['a', 'b', 'c']
l4 = ['rock', 'paper', 'scissor']
d6 = {}
d6 = d6.fromkeys(l3, 'mirror')
print(d6)

for i in d6:
    print(i, end=' ')
print()

for i in d6:
    print(d6[i], end=' ')
print()

x = 0
for i in d6:
    d6[i] = l4[x]
    x = x + 1
print(d6)

# zip used to create dictionary using two sets
d7 = dict(zip(l3, l4))
print(d7)


# Dictionary built-in function
# min, max

l1 = [5, 7, 8, 10, 12]
l2 = [x**2 for x in l1]
d10 = dict(zip(l1, l2))
print("d10 is", d10)
print(min(d10))
print(max(d10))

#  get, returns the value of the keys that we pass

Dict_11 = {
  "brand": "Ford",
  "model": "Mustang",
  "country": "Germany",
  "type": "Petrol"
}
print(Dict_11.get("brand"))
print(Dict_11.get("model"))

Dict_12 = {5: 25, 7: 49, 8: 64, 10: 100, 12: 144}
print(Dict_12.get(max(Dict_12)))

# items returns a list of all the item in the dictionary with
# each key value pair inside a tuple

print(Dict_11.items())
l7 = list(Dict_11.items())

# Multilevel - indexing
print(l7[2][0])
print(l7[3][1])

# List Multilevel indexing 
l8 = [[1, 2], [3, 4, [5, 6]], 7, [8, 9]]
print(l8[1][2][1])

# length function
print(len(Dict_11))

# update all items of dictionary d10 to d11

print()
l9 = [4, 7, 8]
l10 = [x**2 for x in l1]
d10 = dict(zip(l9, l10))

l11 = [10, 12, 15]
l12 = [x**2 for x in l11]
d11 = dict(zip(l11, l12))

print("d11 is", d11)
print("d10 is", d10)

d10.update(d11)
print("Updated d10 is", d10)
print(d10[12])

# Set a default value if a key doesnt exist

Dict_24 = {4: 25, 7: 49, 12: 144, 15: 225}
Dict_24.setdefault(18, 324)
print(Dict_24)
print(Dict_24[18])

# pop - remove the key value pair from the dictionary with passe key

print("Dict_24 after pop", Dict_24)
print(Dict_24.pop(7))
print("Dict_24 after pop", Dict_24)

# pop item - remove any random item from the dictionary
print(Dict_24.popitem())
print("Dict_24 after popitem", Dict_24)

Dict_32 ={1: 'Python', 2: 'Java', 3: 'Ruby', 4: 'Scala'}
print("Dict_32 before clear", Dict_32)
Dict_32.clear()
print("Dict_32 after clear", Dict_32)


# Joining Two dictionary using **

d3 = {1: 'a', 2: 'b'}
d4 = {3: 'c', 4: 'e'}
d6 = d3
print("The d6", d6)
print("The d3", d3)


d3.update(d4)
print("Updated d3 = ", d3)
print("Updated d6 = ", d6)

# Copy - Copy Dictionary d1 into d3
d5 = d3.copy()
print("The d5", d5)

# Use of Copy function - Shallow copy
d6[2] = 'z'
print("The d3",d3)
print("The d6",d6)

# Use of Copy function - Deep copy

d5[3] = 'y'
print("The d3", d3)
print("The d5", d5)