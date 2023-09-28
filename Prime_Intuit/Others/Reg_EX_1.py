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

# split function is used to split the string based on given pattern
e = re.split(" ", str)
print(e)
f = re.split("-", str)
print(f)

# sub / substitute function is used to replace a pattern with a given string
# count is a optional argument to tell how many replacement we want

g = re.sub("-", "**", str)
print(g)
h = re.sub("-", "**", str, 2)
print(h)

# the real application and what makes regular expressions powerful
i = re.findall("\d{10}",str)
print(i)

j = re.findall("[\d{10}]",str)
print(j)

# Meta Characters
# [] - Returns a match if string contains patterns / characters specified (even if one character is matching)
k = re.findall("[PI]", str)
print(k)

# ^ - Return a match if string starts with given pattern
l = re.findall("^P", str)
print(l)
n = re.findall("^I", str) # Returns empty since string doesn't start with I
print(n)

# $ - Return a match if string ends with given pattern
m = re.findall("s$", str)
print(m)
o = re.findall("a$", str) # Returns empty since string doesn't end with a
print(o)

# . - Returns a match for any characters except new line
p = re.findall("^P....", str)
print(p)

q = re.findall("...s$", str)
print(q)

# * - Returns a match if zero or more occurrences
t = re.findall("n*", str)
print(t)
r = re.findall("m*n*", str)
print(r)

# + - Returns a match if one or more occurrences
s = re.findall("n+", str)
print(s)

# ? - Returns a match if zero or one occurrences
s = re.findall("n?", str)
print(s)

# {} - Returns a match if specified number of occurrences
str1 = "A friend is need is a friend indeed"
u = re.findall("e{2}", str1)
print(u)

# \ - special sequences(eg : d for digits)
v = re.findall("\d{10}", str)
print(v)

ab = re.findall("\d{2}d...", str)
print(ab)

# ?
# Causes the resulting RE to match 0 or 1
# repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.  (see problem 4)

# \d - Return match if given string is having digits (0-9)
# same example as above v and ab
# \D - Return match if given string does not have digits
ab = re.findall("\D", str)
print(ab)
# \w - Return match if given string is having characters (a-z, A-Z,0-9)
ac = re.findall("\w", str)
print(ac)
# \W - Return match if given string does not have characters
ad = re.findall("\W", str)
print(ad)
# \s - Return match if given string is having spaces
ae = re.findall("\s", str)
print(ae)
# \S - Return match if given string does not have spaces
af = re.findall("\S", str)
print(af)
# \Z - Return match if given string ends with a specified character
ag = re.findall("s\Z", str)
print(ag)

# Sets
# [abc] - Returns match if string contains any one of the specified characters
ah = re.findall("[PI]", str)
print(ah)

# [a-z] - Returns match if string contains any characters between specified characters
ai = re.findall("[a-z]", str)
print(ai)

ak = re.findall("[0-9]", str)
print(ak)

al = re.findall("[0-9][a-z]", str)
print(al)

# [^abc] - Returns match if string contains characters except specified
aj = re.findall("[^aiern]", str)
print(aj)

str1 = "Prime @ Intuit - Niranjan * Mahesh - 7204251901 - 90days"
ak = re.findall("[^@*-]+", str1)
print(ak)
al = ''.join(ak)
print(al)
# [5678] - Returns match if string contains any numbers that is specified
am = re.findall("[72]", str)
print(am)
# [1-100] - Returns match if string contains any numbers specified by range
an = re.findall("[0-9]", str)
print(an)

# [0-9][0-9] - Returns match if string contains 2 dig number 00 to 99
ao = re.findall("[0-9][0-9]", str)
print(ao)

# [a-z][a-z] - Returns match if string contains continuous characters
ao = re.findall("[a-z][a-z]", str)
print(ao)


# Problems for Regex
# 1) Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9).
# 2) Write a Python program that matches a string that has an 'a' followed by zero or more b's
str2 = "There was one a Bee by the name abb, it is used to sing a song, a, ab, abb, abbb ab_"
ap = re.findall('ab*', str2)
print(ap)
# 3) Write a Python program that matches a string that has an 'a' followed by one or more b's
aq = re.findall('ab+', str2)
print(aq)
# 4) Write a Python program that matches a string that has an 'a' followed by zero or one 'b'
ar = re.findall('ab?', str2)
print(ar)
# 5) Write a Python program that matches a string that has an 'a' followed by three 'b'
at = re.findall('ab{3}', str2)
print(at)
# 6) Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
au = re.findall('ab{2,3}', str2)
print(au)
# 7) Write a Python program to find sequences of lowercase letters joined with a underscore.
aw = re.findall('[a-z]+_[a-z]*', str2)
print(aw)
# 8) Write a Python program to find the sequences of one upper case letter followed by lower case letters.
az = re.findall('[A-Z][a-z]+', str2)
print(az)
# 9) Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# 10) Write a Python program that matches a word at the beginning of a string.
# 11) Write a Python program that matches a word at the end of string, with optional punctuation.
# 12) Write a Python program that matches a word containing 'z'
