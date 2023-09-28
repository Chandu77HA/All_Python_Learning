# Understanding how memory works on lists

# Bytes will return the amount of memory used
# ID - Will return address of memory location

lst1 = [2, 4, 6, 8, 10]
print(lst1)
print("id of list lst1", id(lst1))
# Memory address of the values within a list lst1
print("id of list items lst1", id(lst1[0]), id(lst1[1]), id(lst1[2]), id(lst1[3]))

# What happens when we do a shallow copy
lst2 = lst1
print(lst2)
print("id of list lst2", id(lst2))
# Memory address of the values within a list lst1
print("id of list items lst2", id(lst2[0]), id(lst2[1]), id(lst2[2]), id(lst2[3]))
# The conclusion is lst1 and lst2 memory location and there items memory locations are same

# what happens when we do a deep copy

lst3 = lst1.copy()
print(lst3)
print("id of list lst3", id(lst3))
# Memory address of the values within a list lst1
print("id of list items lst3", id(lst3[0]), id(lst3[1]), id(lst3[2]), id(lst3[3]))
# The conclusion is lst3 memory location is different from lst1 but lst3 items memory location are same as lst1

# Change the value in list lst2
lst3[0] = 3
print("id of list items lst3", id(lst3[0]), id(lst3[1]), id(lst3[2]), id(lst3[3]))
print("id of list items lst1", id(lst1[0]), id(lst1[1]), id(lst1[2]), id(lst1[3]))
# The conclusion is since we changed lst3 first element it will change only the lst3 first element id location
# but remaining id location are same as lst1 because lst3 is copy of lst1


lst2[0] = 12
print("id of list items lst2", id(lst2[0]), id(lst2[1]), id(lst2[2]), id(lst2[3]))
print("id of list items lst1", id(lst1[0]), id(lst1[1]), id(lst1[2]), id(lst1[3]))
print("id of list items lst3", id(lst3[0]), id(lst3[1]), id(lst3[2]), id(lst3[3]))
# The conclusion is since we changed lst2 first element it will change both lst2 and lst1 frst element id location
# because we defined lst1 and lst2 are equal