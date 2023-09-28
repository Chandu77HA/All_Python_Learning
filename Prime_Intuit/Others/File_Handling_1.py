# File handling in python

# 1) Reading
frt = open('fruits.txt', 'r')
print("Output of read file\n")
print(frt.read())
print()
print("Output of read line ") # No output because end of file reached
print(frt.readline())


frt = open('fruits.txt', 'r')
print("Output of read line1")
print(frt.readline())
print("Output of read line2")
print(frt.readline())
print("Output of read line3")
print(frt.readline())
# After last line is reached it will print none
print("Output of read line4")
print(frt.readline())

frt = open('fruits.txt', 'r')
print("Output of read lines")
print(frt.readlines())


frt = open('fruits.txt', 'r')
print("Output of read line in characters")
print(frt.readline(5))

frt = open('fruits.txt', 'r')
print("Output of read multiple lines in characters")
print(frt.readlines(20))


frt = open('fruits.txt', 'r')
cat = frt.readline()
print("Output of read cat \n", cat)
dog = frt.readline()
print("Output of read dog \n", dog)


# Use for loop to read the line
frt = open('fruits.txt', 'r')
print("using for loop")
for i in frt:
    print(i)
print()


# File attributes
print("File mode : ", frt.mode)
print("File name : ", frt.name)
print("File close check : ", frt.closed) # Check if the file is closed or not
frt.close()
print("File close check : ", frt.closed) # Check if the file is closed or not


# 2) Reading and Writing
frt = open('fruits.txt', 'r+')
print("\nOutput of read plus file")
print(frt.read())
print()
print("Output of read line") # No output because end of file reached
print(frt.readline())
frt.write('\nPomegranate')


# File attributes
print("File mode : ", frt.mode)
print("File name : ", frt.name)
print("File close check : ", frt.closed) # Check if the file is closed or not
frt.close()
print("File close check : ", frt.closed) # Check if the file is closed or not


# 3) Append
# How to use the Append Function (a)
frt = open("fruits.txt", 'a')
frt.write('\nJackfruit\nGuava')
# print(frt.read()) # It will give an error since read mode not possible in append mode

# File attributes
print("File mode : ", frt.mode)
print("File name : ", frt.name)
print("File close check : ", frt.closed) # Check if the file is closed or not
frt.close()
print("File close check : ", frt.closed) # Check if the file is closed or not

# 4) Append and reading
# How to use the Append Function (a+)
frt = open("fruits.txt", 'a+')
print(frt.read()) # Since cursor is at last line it will print none
frt.write('\nPlums')
print(frt.read()) # Since cursor is at last line it will print none
# It will not give an error since read mode is possible in append plus mode

# File attributes
print("File mode : ", frt.mode)
print("File name : ", frt.name)
print("File close check : ", frt.closed) # Check if the file is closed or not
frt.close()
print("File close check : ", frt.closed) # Check if the file is closed or not

# 5) Write Mode
# How to use write mode
frt = open('fruits.txt', 'w')
# Once we open file in write(w) mode existing file will be rewritten(delete old file contents)
frt.write('Apple\nBanana\nMango')
# print(frt.read()) # It will give an error since read mode not possible in write mode
frt.close()

# How to use write mode
# It will create a new file if the file does not exist
frt = open('color.txt', 'w')
# Once we open file in write(w) mode existing file will be rewritten(delete old file contents)
frt.write('Red\nGreen\nWhite')

# File attributes
print("File mode : ", frt.mode)
print("File name : ", frt.name)
print("File close check : ", frt.closed) # Check if the file is closed or not
frt.close()
print("File close check : ", frt.closed) # Check if the file is closed or not

# 6) Write and Read Mode
# How to use Write and Read mode
frt = open('fruits.txt', 'w+')
# Once we open file in write(w) mode existing file will be rewritten(delete old file contents)
frt.write('Apple\nBanana\nMango')
print(frt.read())
# It will not give an error since read mode is possible in write plus mode
# Since cursor is at last line it will print none
frt.close()

# How to use Write and Read mode
# It will create a new file if the file does not exist
frt = open('cricket.txt', 'w+')
# Once we open file in write(w) mode existing file will be rewritten(delete old file contents)
frt.write('Maxwell\nSmith\nWarner')

# File attributes
print("File mode : ", frt.mode)
print("File name : ", frt.name)
print("File close check : ", frt.closed) # Check if the file is closed or not
frt.close()
print("File close check : ", frt.closed) # Check if the file is closed or not

# Using Context management
# It will automatically close the file - explicit declaration to close the file is not required

# when we use context management it will automatically close the file
# we don't need to give the file.close to close the file

# 1) Reading
with open('fruits.txt', 'r') as frt:
    print("Context mode\n")
    print(frt.read())
print("File close check : ", frt.closed) # Check if the file is closed or not

# 2) Reading and writing
with open('fruits.txt', 'r+') as frt:
    print("Context mode\n")
    print(frt.read())
    frt.write('\nCoconut')
    print(frt.read())
print("File close check : ", frt.closed) # Check if the file is closed or not

# 3) Append
# If the file does not exist it will create new file
with open('fruits.txt', 'a') as frt:
    print("Context mode\n")
    frt.write('\nJackfruit\nGuava')
print("File close check : ", frt.closed) # Check if the file is closed or not

# 4) Append and Reading
# If the file does not exist it will create new file
with open('fruits.txt', 'a+') as frt:
    print("Context mode\n")
    frt.write('\nPlums')
    print(frt.read())  # Since cursor is at last line it will print none
    # It will not give an error since read mode is possible in append plus mode
print("File close check : ", frt.closed) # Check if the file is closed or not

# 5) Writing
# If the file does not exist it will create new file
with open('fruits.txt', 'w') as frt:
    print("Context mode\n")
    frt.write('Apple\nBanana\nMango')
print("File close check : ", frt.closed) # Check if the file is closed or not

# 6) Writing and Reading
# If the file does not exist it will create new file
with open('fruits.txt', 'w+') as frt:
    print("Context mode\n")
    frt.write('Apple\nBanana\nMango')
    print(frt.read())  # Since cursor is at last line it will print none
    # It will not give an error since read mode is possible in append plus mode
print("File close check : ", frt.closed) # Check if the file is closed or not

with open('animals.txt', 'w+') as frt:
    # If the file does not exist it will create new file
    print("Context mode\n")
    frt.write('Cow\nDog\nCat\nHorse\nSheep')
    print(frt.read())  # Since cursor is at last line it will print none
    # It will not give an error since read mode is possible in append plus mode

# File attributes
print("File mode : ", frt.mode)
print("File name : ", frt.name)
print("File close check : ", frt.closed) # Check if the file is closed or not

# FLUSH function
# Python automatically flushes the file before closing them. but you
# may want to flush the data before closing any file, then we use flush function.
with open('fruits.txt', 'r') as frt:
    print("read lines", frt.readlines())
    frt.flush() # just flushes the internal buffer memory from the heep space and name space

# SEEK and TEll
# Tell function will return a number where the cursor was in.
# The method tell() returns the current position of the file read/write pointer within the file.
# With seek Function it will tell and move the cursor where to start the reading of the file

with open('fruits.txt', 'a+') as frt:
    str = "\ngrapes \npear \npeach \nwatermelon"
    print("write lines", frt.read())
    # since we use append cursor in last position, so it has nothing to read so this
    # print statement doesn't give output so move the cursor to starting position
    frt.writelines(str)
    print(frt.tell())
    frt.seek(0)
    print("write lines\n", frt.read())
    # The above read line will give the output since we have moved the cursor using seek function

# Delete the file

import os
os.remove("animals.txt")

# Check if file exist before deleting the file to avoid getting an error

import os
if os.path.exists("animals.txt"):
    os.remove("animals.txt")
else:
    print("The file does not exist")