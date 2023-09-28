

name = "Chandan HA"
phrase = "Chandan is from Hadya "

# Print entire string
print(name)

# finding length of the string
print(len(name))

# indexing individual character
print(name[3])

# slicing a string to required index
print(name[8:10])

# slicing a string : indicates from start of the string ie Oth index and end at range 7 ie 6th index
print(name[:7])

# slicing a string 8 indicates start from 7th index and : indicates up to the last index of the string
print(name[8:])

# Print from starting to end index of the string
print(name[::])

# Printing the indivisual index of the string
print(name[0], name[8], name[9])


place = "Nanjangud Mysuru"

print(place[8:11])

print(place[8], place[10])

# indicates from start and end
print(place[::])

# print the string in reverse order
print(place[::-1])

# print the string in reverse order skip one index after printing one index
print(place[::-2])

# print the string in reverse order skip two indexs after printing one index
print(place[::-3])


a = "Hello !"
b = "Prime Intuit"
c = "one of the Finest Finishing School"
print(a[::])
print(a[::-1])
print(a[::+2])

# concatenation using two string
d = a+" "+b 
print(d)

# concatenation using two string with indexing
e = a+" "+b+" "+c[11:] 
print(e)


# multiply operator

word = "Courage "
print(word*3)
print("Tiger "*7)

# Some membership operators (in and not in)

courage = "Courage that Build the Confidence to do good things"

# one string and one variable
print("Confidence" in courage)

print("Fear" in courage)


print("good" and "things" in courage)

print("2" in "XF54236RF258") # two string

f = "that"
print(f in courage)

# not in
print("Build" not in courage)
print("Lion" not in courage)


# new line \n
print("Our Perception is our Reality \nWhat We Think we Become \nYadbavam Tadbavathi")


# Formating, %, Format - perform string formating
print("My name is %s and I weigh %d"%("Chandan", 71))

name = "Chandan"
cgpi = 8.77
print("The certificate is issued to \n" "Mr %s \nHe has scored CGPI of %2f "%(name, cgpi))
print("The certificate is issued to " "Mr %s \nHe has scored CGPI of %2f "%(name, cgpi))

# Formating using f string
var_1 = "Major"
var_2 = "You"
print(f"The {var_1} Key to Your Better Future is {var_2}")



# String Functions

a = "   today is sunday"
x = "the sea is calm today"
y = "Wild and free also means mad and unpredictable"
fruits = "i love apples and apples are my favorite fruits"
z = "CONSISTENCY"
pi = " PRIME INTUIT "
num = "012345679"
num1 = "345 4 5"
box1 = "df5db48"
box2 = "dfbdb"
box3 = "ajnf97c js9"
box4 = "as df sv"
list1 = ["one", "two", "three", "four", "five"]
list2 = ["six", "seven", "eight"]
box6 = "8 9 7"

# convert first character of a string to upper character
print(x.capitalize())

# entire string is converted in to upper case
print(x.upper())

# entire string is converted in to lower case
print(z.lower())

# will return true if all the characters are upper case
print(z.isupper())

# will return true if all the characters are lower case
print(x.islower())

# will return false if any one of the character is upper case
print(y.islower())

# position the string in the center
print(len(pi))
print(pi.center(20,"%"))

# return true if sting contain only alfabet and neumaric without space
print(box1.isalnum())
print(box3.isalnum())

# return true if sting contain only alfabet without space
print(box2.isalpha())
print(box4.isalpha())

# return true if sting contain only numeric without space
print(num.isdigit())
print(num1.isdigit())

# returns the number of times a specified value occurs in the string
print(fruits.count("apple"))

# returns the encoded version of the string
print(x.encode())

# returns true if string ends with specified value
print(a.endswith("y"))

# search the string for the specified value and returns starting index position of where it was found
print(y.find("free"))
print(fruits.find("a"))

# return true if sting contain only alfabet without space
print(box2.isalpha())
print(box4.isalpha())

# return true if sting contain only numeric without space
print(num.isdigit())
print(num1.isdigit())

# returns the number of times a specified value occurs in the string
print(fruits.count("apple"))

# returns the encoded version of the string
print(x.encode())

# returns true if string ends with specified value
print(a.endswith("y"))

# search the string for the specified value and returns starting index position of where it was found
print(y.find("free"))
print(fruits.find("a"))
print(fruits.find("and"))

# format specified value in a string and place it inside the string placeholder
txt1 = "for only {price:.2f} dollars!"
print(txt1.format(price = 49))

# search the string for the specified value and returns the position of where it was found
print(fruits.index("are"))

box5 = "919498"
box6 = "8 9 7"
box7 = "sdv343j34"

# returns true if all the character s in the string are decimal
print(box5.isdecimal())
print(box6.isdecimal())
print(box7.isdecimal())

# returns true if all the character s in the string are numeric
print(box5.isnumeric())
print(box6.isnumeric())
print(box7.isnumeric())


# returns true if string contain only white space
box8 = "  "
print(box8.isspace()) 
print(box6.isspace())


# returns the left trim version of a string
print(a)
print(a.lstrip())

# joins the elements of the iterable with specified character to form a string
myTuple = ("apple", "mango", "grapes")
print("&".join(myTuple))


abc = "   today is sunday    "
print(abc.strip())

# count the number of times in a character occurring in string
print(x.count("a"))

# count the number of times in substring occurring in string
print(y.count("free"))
print(y.count("apples"))
print(fruits.count("apples"))

# return true if string contains only spaces
print("   ".isspace()) 


list1 = ["one", "two", "three", "four", "five"]
list2 = ["six", "seven", "eight"]

# joins the elements of the iterable with specified character to form a string
print("_".join(list1))
print(" ".join(list1))
print("&".join(list1[:3]))


# String indexing another example

myName = 'Chandan Nanjangud'
print(myName)
print(myName[0], myName[12])
print(myName[0:5])
print(myName[:5])
print(myName[3:17])
print(myName[::])
print(myName[:])
print(myName[::2])
print(myName[::3])
print(myName[::-1])
print(myName[::-2])
print(myName[5:])
print(myName[-2:-3])
print(myName[4:7:-1])
print(myName[4:-1:2])
print(myName[4:2:3])
print(len(myName))
