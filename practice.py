# Creating a Tuple
t1 = (1, 2, "three", "four", 5.5)
t2 = t1[:1]

t4 = (3, 5, 7, 11, 21, 9)


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

