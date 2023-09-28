
# Regular expression or RegEx module is used to
# access information in the string or to clean
# RegEx is used to check if a string contain specific search pattern or not
# RegEx is a sequence of characters that contain a search pattern

import re
str = "Prime Intuit - Niranjan * Mahesh - 7204251901-90days"

# find all function takes 2 arguments ("Pattern", String)
# and returns all occurrence of the pattern as a list, in case of no match returns empty list
a = re.findall("i", str) # Match
print(a)
b = re.findall("z", str) # No-Match
print(b)
# Output:
# ['i', 'i', 'i']
# []

# Search function takes 2 arguments ("Pattern", String)
# Search Function returns a search object for first instance of the pattern,
# which can be used along with functions
# start, span and string
# search instance will give the first instance
c = re.search("-", str)
print("Start function returns starting index", c.start())
print("Span function returns starting and ending index", c.span())
d = re.search("Ni", str)
print("Span function returns starting and ending index", d.span())
print("String function returns entire string : ", c.string)

# Output:
# Start function returns starting index 13
# Span function returns starting and ending index (13, 14)
# Span function returns starting and ending index (15, 17)
# String function returns entire string :  Prime Intuit - Niranjan * Mahesh - 7204251901-90days


# split function is used to split the string based on given pattern
e = re.split(" ", str)
print(e)
f = re.split("-", str)
print(f)

# Output:
# ['Prime', 'Intuit', '-', 'Niranjan', '*', 'Mahesh', '-', '7204251901-90days']
# ['Prime Intuit ', ' Niranjan * Mahesh ', ' 7204251901', '90days']

# sub / substitute function is used to replace a pattern with a given string
# count is a optional argument to tell how many replacement we want

g = re.sub("-", "**", str)
print(g)
h = re.sub("-", "**", str, 2)
print(h)

# Output:
# Prime Intuit ** Niranjan * Mahesh ** 7204251901**90days
# Prime Intuit ** Niranjan * Mahesh ** 7204251901-90days

# Python raw string is created by prefixing a string literal with 'r' or 'R'.
# Python raw string treats backslash (\) as a literal character

print("name5")
print("\t name5")
print(r"\t name5")

# Output:
# name5
# 	 name5
# \t name5

# Meta Characters (Need to be escaped):
# . ^ $ * + ? {} [] \ | ()

# .(Dot)
# Any Characters Except new Line

s1 = "abc.com 25-65-64 77   "
a1 = re.findall(r".", s1)
print(a1)

# Tab is considered as three spaces
# Output:['a', 'b', 'c', '.', 'c', 'o', 'm', ' ', '2', '5', '-', '6', '5', '-', '6', '4', ' ', '7', '7', ' ', ' ', ' ']

s111 = '''abc.com
dog.5
cat.8'''
a111 = re.findall(r".", s111)
print(a111)

# Here new line is not considered
# Output:['a', 'b', 'c', '.', 'c', 'o', 'm', 'd', 'o', 'g', '.', '5', 'c', 'a', 't', '.', '8']

# \d
# Returns digit(0-9)
a1 = re.findall(r"\d", s1)
print(a1)

# Output:['2', '5', '6', '5', '6', '4', '7', '7']

a111 = re.findall(r"\d{2}", s1)
print(a111)

# Output:['25', '65', '64', '77']

str = "Prime Intuit - Niranjan * Mahesh - 7204251901-90days"
ab = re.findall("\d{2}d...", str)
print(ab)

ac = re.findall("\d{2}", str)
print(ac)

ad = re.findall("\d{5}", str)
print(ad)

# Output:
# ['90days']
# ['72', '04', '25', '19', '01', '90']
# ['72042', '51901']

# \D
# Returns every characters except digit (0-9)
s2 = "abc  abc.com ah#$^ 986-987-546"
a2 = re.findall(r"\D", s2)
print(a2)

# Output:['a', '', 'c', ' ', ' ', 'a', 'b', 'c', '.', 'c', 'o', 'm', ' ', 'a', 'h', '#', '$', '^', ' ', '-', '-']

s202 = '''The Lion785 is the King of Jungle2658 But the Tiger$&% is786 more Stronger256 and powerful'''
a202 = re.findall(r"\D{8}", s202)
print(a202)

# Output:['The Lion', ' is the ', 'King of ', ' But the', ' Tiger$&', ' more St', ' and pow']

# \w
# Returns Word Character (a-z, A-Z, 0-9, _)
# It Neglects special character except underscore

s3 = "abc A_J_DL546@#$ 98-98-677-777"
a3 = re.findall(r"\w", s3)
print(a3)

# Output:['a', 'b', 'c', 'A', '_', 'J', '_', 'D', 'L', '5', '4', '6', '9', '8', '9', '8', '6', '7', '7', '7', '7', '7']

# \W
# Returns Not Word Character, all other than (a-z, A-Z, 0-9, _)

s4 = "abc A_J_DL546@#$ 98-98-677-777"
a4 = re.findall(r"\W", s4)
print(a4)

# Output:[' ', '@', '#', '$', ' ', '-', '-', '-']

# \s
# Returns Whitespace (space, tab, newline)

s5 = '''ac 6@$ 77-77
ad
54gg'''
a5 = re.findall(r"\s", s5)
print(a5)

# Output:[' ', ' ', '\n', '\n']

# \S
# Returns other than Whitespace (space, tab, newline)

s6 = '''ac 6@$ 77-77
ad
54gg'''
a6 = re.findall(r"\S", s6)
print(a6)

# Output:['a', 'c', '6', '@', '$', '7', '7', '-', '7', '7', 'a', 'd', '5', '4', 'g', 'g']

# \b
# Word Boundary
s7 = "abc abc abc "
a7 = re.findall(r"\babc", s7)
print(a7)

# Output:['abc', 'abc', 'abc']

s8 = "abc abc58abc"
a8 = re.findall(r"\babc", s8)
print(a8)

# Output:['abc', 'abc']

s9 = "abc56 5abc665ab77"
a9 = re.findall(r"\babc", s9)
print(a8)

# Output:['abc', 'abc']

# ^
# Beginning of the string
# ^ - Return a match if string starts with given pattern

s10 = "abc56 5abc665ab77"
a10 = re.findall(r"^abc", s10)
print(a10)
# Output:['abc']

s10 = "Prime Intuit"
a10 = re.findall(r"^ABD", s10)
print(a10)
# Output:[]

s10 = "Finishing School"
a10 = re.findall(r"^Fi", s10)
print(a10)
# Output:['Fi']

# $
# End of the string
# $ - Return a match if string ends with given pattern

s11 = "abc56 5abc665ab77"
a11 = re.findall(r"7$", s11)
print(a11)
# Output:['7']

s12 = "Prime Intuit"
a12 = re.findall(r"it$", s12)
print(a12)
# Output:['it']

s13 = "Finishing School"
a13 = re.findall(r"U$", s13)
print(a13)
# Output:[]

# []
# Matches the Characters in the brackets
# [] - Returns a match if string contains patterns / characters specified (even if one character is matching)

s14 = "Prime Intuit"
a14 = re.findall("[PIx]", s14)
print(a14)
# Output:['P', 'I']

s15 = '''958-987-3254
         398_875_8452
         745*856*3256
         '''
a15 = re.findall(r"\d\d\d[_*]\d\d\d[_*]\d\d\d\d", s15)
print(a15)
# Output:['398_875_8452', '745*856*3256']

a16 = re.findall(r"\d\d\d[^_*]\d\d\d[^_*]\d\d\d\d", s15)
print(a16)
# Output:['958-987-3254']

s17 = "Prime Intuit"
a17 = re.findall("[jl]", s17)
print(a17)
# Output:[]

# {min, max}
# Range of numbers (min, max)

s19 = '''958-987-3254
         398_875_8452
         745*856*3256
         '''
a19 = re.findall(r"\d{4,5}", s19)
print(a19)
# Output:['3254', '8452', '3256']

a20 = re.findall(r"\d{3}", s19)
print(a20)
# Output:['958', '987', '325', '398', '875', '845', '745', '856', '325']

a21 = re.findall(r"\d{3,4}.\d{3,4}.\d{4,5}", s19)
print(a21)
# Output:['958-987-3254', '398_875_8452', '745*856*3256']

# ?
# Matches 0 or 1 characters
str1 = "Prime Intuit"
t2 = re.findall("n?", str1)
print(t2)
# Output:['', '', '', '', '', '', '', 'n', '', '', '', '', '']

t2 = re.findall("na?", str1)
print(t2)
# Output:['n']

# *
# Matches 0 or more characters
str1 = "Prime Intuit"
t = re.findall("n*", str1)
print(t)
# Output:['', '', '', '', '', '', '', 'n', '', '', '', '', '']

r = re.findall("m*n*", str1)
print(r)
# Output:['', '', '', 'm', '', '', '', 'n', '', '', '', '', '']

# +
# Matches 1 or more characters
str2 = "bhavana meghana lalana"
s = re.findall("na+", str2)
print(s)
# Output:['na', 'na', 'na']


s25 = ''' Mr.Sachin
          Mr Smith
          Mr Divya
          Mrs. Robinson
          Mr. T'''
a25 = re.findall(r"Mr\.?\s[A-Z]\w*", s25)
print(a25)
# Output:['Mr Smith', 'Mr Divya', 'Mr. T']

s26 = ''' Mr.Sachin
          Mr Smith
          Mr Divya
          Mrs. Robinson
          Mr. T'''
a26 = re.findall(r"M[a-z]+\.?\s[A-Z]\w*", s26)
print(a26)
# Output:['Mr Smith', 'Mr Divya', 'Mrs. Robinson', 'Mr. T']