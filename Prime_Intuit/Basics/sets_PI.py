# Sets are unordered collection of data
# Sets are not editable and do not contain duplicates
# If contain duplicate it will remove duplicates
# Sets can contain any immutable data elements like int, string, tuples

# Creating a set

s1 = {1, 2, 3, 4, 5}
s2 = {"Mysuru", "Bengaluru", "Mandya", "Mangalore", "Mandya"}
print(s1)
print(s2)

# Creating a sets using a sets construction

l1 = [2, 4, 5, 6, 8, 10, 10]
str1 = "Prime intuit"
t1 = (1, 3, 5, 7, 9, 3, 5)
d1 = {"red": "rose", "white": "lilly", "purple": "lavender"}

# Converting a list into a set to get rid of duplicates
s3 = set(l1)
print(l1)
print(s3)
l1 = list(s3)
print(l1)

# Concise way
l1 = list(set(l1))
print(l1)

# Converting a string in to set
s4 = set(str1)
print(str1)
print(s4)

# Converting tuple in to a set
s5 = set(t1)
print(t1)
print(s5)

# Converting a dict into a set
s6 = set(d1)
print(d1)
print(s6)

# Adding an element in to a set
myset = {"Geeks", "for", "Geeks"}
myset.add(12)
print(myset)
myset.add("Learning")
print(myset)

# Removing an element from the set()
myset.remove("Learning")
print(myset)

# discard v/s remove, discard will not give me an error if data element is not found
myset.discard(4)
myset.discard(64) # This will not give error, although 64 is not in myset
print(myset)

# But remove will raise an error if element not found
# myset.remove(64)
# print(myset)


# Understanding pop function
# Remove random item from the set
Set_1 = {"Geeks", "for", 10, 52.7, True}
item = Set_1.pop()
print(Set_1, "Pop item is: ", item)
item_2 = Set_1.pop()
print(Set_1, "Pop item is: ", item_2)

# Example-2
box1 = {54, 75, 25, 41, 32, 84, 66, 77}
item = box1.pop()
print(box1, "Popped item: ", item)
box2 = {"white", "black", "orange", "red", "blue"}
item2 = box2.pop()
print(box2, "Popped item: ", item2)

# Mathematical operations / set operations

s7 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
s8 = {0, 2, 4, 6, 8, 10}

# Union
print("Union of s7 and s8 = ", s7.union(s8))
print("Union of s8 and s7 = ", s8.union(s7))

# Intersection
print("Intersection of s7 , s8 = ", s7.intersection(s8))
print("Intersection of s8 , s7 = ", s8.intersection(s7))

# Difference
print("Difference of s7 from s8 = (s7-s8) = ", s7.difference(s8))
print("Difference of s8 from s7 = (s8-s7) = ", s8.difference(s7))

# Symmetric Difference
print("Symmetric Difference of s7 from s8 = (s7-s8) & (s8-s7)= ", s7.symmetric_difference(s8))
print("Symmetric Difference of s8 from s7 = (s8-s7) & (s7-s8)= ", s8.symmetric_difference(s7))


s9 = {1, 2, 3}
s10 = {4, 5, 6}

# Disjoint
print("is s7 disjoint of s8 :", s7.isdisjoint(s8))
print("is s9 disjoint of s10 :", s9.isdisjoint(s10))

# Subset
print("is s9 a subset of s7 : ", s9.issubset(s7))
print("is s8 a subset of s7 : ", s8.issubset(s7))

# Superset
print("is s7 a superset of s9 : ", s7.issuperset(s9))
print("is s7 a superset of s8 : ", s7.issuperset(s8))

# Membership Operators (in, notin)

print("is value 1 present in s9 :", 1.in(s9))
print("is value 10 present in s9 :", 10.in(s9))
print("is value 4 not present in s9 :", 4.not in(s9))
print("is value 2 not present in s9 :", 2.not in(s9))

# frozen sets

l11 = [5, 10, 15, 20]
f1 = frozenset(l11)
print(f1)
print("Frozen set :",type(f1))
print("Set :",type(s9))

# frozen sets are immutable we cannot add or remove an element from frozen sets

# f1.add(25) # will give an exception error
# f1.remove(20) # will give an exception error

s14 = {22, 33, 44, 55, 66, 88, 99}
print("Set :",type(s14))
s14.add(77)
print(s14)
s14.remove(55)
print(s14)

# frozen sets are immutable we cannot add or remove an element from frozen sets
s11 = {25, 33, 46, 58, 77}
f2 = frozenset(s11)
print(s11)
print("Frozen set :",type(f2))

# f2.add(88) # will give an exception error
# f2.remove(20) # will give an exception error

# Some common functions between sets and list

sa = {1, 2, 3, 4, 5}
sb = {6, 7, 8, 9}

print(len(sa))

sa.update(sb)
print(sa)

print(min(sa), max(sa))


# Some common functions between sets and list

sa = {1, 2, 3, 4, 5}
sb = {6, 7, 8, 9}

print(len(sa))

sa.update(sb)
print(sa)

print(min(sa), max(sa))

# Practice Problems:

a = {1, 2, 3, 4, 5, 6}
b = {5, 6, 7, 8, 9}

# Return a new set having identical items from 2 sets
c = a.intersection(b)
print(c)

# Common elements between 2 sets
# Get only unique items from two sets
a5 = {1, 2, 3, 4, 5, 6}
b5 = {5, 6, 7, 8, 9}
print(a5.union(b5))


print(a5.difference(b5))
print(a5)

# Update the first set with items that doest not exist in the second set
a6 = {1, 2, 3, 4, 5, 6}
b6 = {5, 6, 7, 8, 9}
a6.difference_update(b6)
print(a6)

# Remove items from the set at once
sx = {1, 2, 3, 4, 5, 6, 7, 8}
sx.difference_update({6, 7, 8})
print(sx)

# Return a set of elements present in set A or B, but not in both
a22 = {1, 2, 3, 4, 5, 6}
b22 = {5, 6, 7, 8, 9}
a22.symmetric_difference(b22)
print(a22.symmetric_difference(b22))


# Check if two sets have any elements in common
# Display the common elemenst
d = {1, 2, 3, 4, 5, 6}
e = {5, 6, 7, 8, 9}
if (d.isdisjoint(e)):
    print("No common Elements")
else:
    print(d.intersection(e))

# Update s1 by adding items from set2 except common items

f = {1, 2, 3, 4, 5, 6}
g = {5, 6, 7, 8, 9}
f.symmetric_difference_update(g)
print(f)

# Remove items from set1 that are not common to both set1 and set2
g = {1, 2, 3, 4, 5, 6}
h = {5, 6, 7, 8, 9}
print(g.intersection(h))

# Or
g.intersection_update(h)
print(g)


# Python - Check if two lists have at-least one element common
s9 = {1, 2, 3, 4, 5, 6}
s10 = {5, 6, 7, 8, 9}
print(not(set(s9).isdisjoint(set(s10))))
# If disjoint is false that means element are common between 2 sets since
# s9 and s10 have elements in common we need to print true use not operation


# Program to find common elements in three lists using lists

a3 = [1, 2, 3, 4, 5, 6]
b3 = [5, 6, 7, 8, 9]
c3 = [5, 8, 7, 11]
print(set(a3).intersection(set(b3)).intersection(set(c3)))



# Python Program to Find missing and additional values in two lists

ls1 = [1, 2, 3, 4, 5, 6]
ls2 = [4, 5, 6, 7, 8]
print(set(ls1).symmetric_difference(ls2))

# Python Program to Find difference between two list

print(set(ls1).difference(set(ls2)))

# Use set difference to find lost element from a duplicated array
l1 = [1, 4, 5, 7, 9]
l2 = [4, 5, 7, 9]
print(set(l1).difference(set(l2)))

