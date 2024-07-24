# Creating a Tuple
t1 = (1, 2, "three", "four", 5.5)
t2 = t1[:1]
print(t1)
print(t2)

# Joining 2 tuples
print(t1+t2)

# Joining 2 tuples to create a new tuple
t3 = (t1+t2)
print(t3)
# tuple in Python is immutable.

# Not Supported function
# t3[1] = 3 # Error : updating a tuple is not possible
# t3.append(4) # Error : appending a tuple is not possible
# t3.remove(3) # Error : tuple object has no attribute return or pop
# del(t3[0]) # tuple does not support item deletion

# if a tuple contains mutable elements like lists, the mutable elements themselves can be changed.

nested_tuple = (1, 2, [3, 4])
nested_tuple[2][0] = 30  # This is allowed
print(nested_tuple)  # Output: (1, 2, [30, 4])

del(t3)

# will print the length of the object
print(len(t1))

# membership operator will return ture if item present in th etuple
print(2 in t1)

t4 = (3, 5, 7, 11, 21, 9)
# will return the minimum of tuple
print(max(t4))

# will return the maximum of tuple
print(min(t4))

for i in t4:
    print(i**2, end=' ')
print()

for i in t1:
    print(i , end=' ')
print()

# printing a tuple multiple times
print(t4*2)

# Creating a tuple using range function with increment
t5 = tuple(range(0, 20, 2))
print(t5)

t6 = tuple(range(0, 31, 3))
print(t6)
