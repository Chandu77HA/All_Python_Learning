
# File handling in python

frt = open('fruits.txt', 'r')
print("Output of read file \n", frt.read())
print("Output of read line \n", frt.readline()) # No output because end of file reached
frt = open('fruits.txt', 'r')
print("Output of read line1 \n", frt.readline())
print("Output of read line2 \n", frt.readline())
cat = frt.readline()
print("Output of read cat \n", cat)
dog = frt.readline()
print("Output of read dog \n", dog)

# Use for loop to read the line
print("using for loop")
for i in frt:
    print(i)
print()

# File attributes
print("File mode : ", frt.mode)
print("File name : ", frt.name)
print("File close : ", frt.closed) # Check if the file is closed or not
frt.close()

# How to use the Append Function
frt = open("fruits.txt", 'a')
frt.write('\nJackfruit\nGuava')
frt.close()

# How to use the Append Function
frt = open("fruits.txt", 'a+')
frt.write('\nPlums')
print(frt.read())
frt.close()

# How to use write mode
frt = open('fruits.txt', 'w')
# Once we open file in write(w) mode existing file will be rewritten(delete old file contents)
frt.write('\nApple\nBanana\nMango')
frt.close()

# Using Context management

with open('fruits.txt', 'r') as frt:
    print("context mode", frt.read())

# when we use context management it will automatically close the file
# we don't need to give the file.close to close the file
print(frt.closed) # Check whether file is closed or not

# using read lines

with open('fruits.txt', 'r') as frt:
    print("read lines", frt.readlines(1))
    frt.flush() # just flushes the internal buffer memory from the heep space and name space

with open('fruits.txt', 'a+') as frt:
    str = "\ngrapes \npear \npeach \nwatermelon"
    print("write lines", frt.read())
    # since we use append cursor in last position so it has nothing to read so
    # this print statement doesn't give output
    # so move the cursor to starting position
    frt.writelines(str)
    print(frt.tell())
    frt.seek(9)
    print("write lines", frt.read())
    #since we use append cursor in last position so it has nothing to read so
    # this print statement doesn't give output

# Reading from file other than default directory
with open('C:\\CHAN_MI\\PRIME_INTUIT_CLASS\\game.txt', 'r+') as game:
    text = game.read()
    print(text)

import os
print(os.getcwd()) # Present working directory
os.chdir('C:\\Users\\SHIVA PRASAD\\PycharmProjects') # change working directory
os.mkdir('C:\\Users\\SHIVA PRASAD\\PycharmProjects\\prime_intuit') # make new directory
os.remove('C:\\Users\\SHIVA PRASAD\\PycharmProjects\\prime_intuit\\game123.txt') # remove file from directory


