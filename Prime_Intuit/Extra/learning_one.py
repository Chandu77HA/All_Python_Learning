
'''
The Python all() function returns true if all the elements of a given iterable
(List, Dictionary, Tuple, set, etc.) are True otherwise it returns False. 
It also returns True if the iterable object is empty. Sometimes while 
working on some code if we want to ensure that user has not entered a False 
value then we use the all() function.d3 = {1: 'a', 2: 'b'}
'''

# Example 1: Working of all() with Lists

print(all([True, True, False]))


# All elements of list are true
l = [4, 5, 1]
print(all(l))
 
# All elements of list are false
l = [0, 0, False]
print(all(l))
 
# Some elements of list are
# true while others are false
l = [1, 0, 6, 7, False]
print(all(l))
 
# Empty List
l = []
print(all(l))
 
# all() with condition - to check if all elements are greater than 0
l = [1,-3,0,2,4]
print(all(ele > 0 for ele in l))

# Example 2: Working of all() with Tuples

# All elements of tuple are true
t = (2, 4, 6)
print(all(t))
 
# All elements of tuple are false
t = (0, False, False)
print(all(t))
 
# Some elements of tuple
# are true while others are false
t = (5, 0, 3, 1, False)
print(all(t))
 
# Empty tuple
t = ()
print(all(t))
 
# all() with condition - to check if all elements are even
l = (2,4,6,8,10)
print(all(ele % 2 == 0 for ele in l))

a = -5
print(abs(a))

# Example 3: Working of all() with Sets

# All elements of set are true
s = {1, 1, 3}
print(all(s))
 
# All elements of set are false
s = {0, 0, False}
print(all(s))
 
# Some elements of set
# are true while others are false
s = {1, 2, 0, 8, False}
print(all(s))
 
# Empty set
s = {}
print(all(s))
 
# all() with condition - to check if absolute of all elements is greater than 2
l = {-4,-3,6,-5,4}
print(all(abs(ele) > 2 for ele in l))

# Example 4: Working of all() with Dictionaries

# All elements of dictionary are true
d = {1: "Hello", 2: "Hi"}
print(all(d))
 
# All elements of dictionary are false
d = {0: "Hello", False: "Hi"}
print(all(d))
 
# Some elements of dictionary
# are true while others are false
d = {0: "Salut", 1: "Hello", 2: "Hi"}
print(all(d))
 
# Empty dictionary
d = {}
print(all(d))
 
# all() with condition - to check if all letters of word 'time' are there
l = {"t":1, "i":1, "m":2, "e":0}
print(all(ele > 0 for ele in l.values()))


# Example 4: Working of all() with Dictionaries

# All elements of dictionary are true
d = {1: "Hello", 2: "Hi"}
print(all(d))
 
# All elements of dictionary are false
d = {0: "Hello", False: "Hi"}
print(all(d))
 
# Some elements of dictionary
# are true while others are false
d = {0: "Salut", 1: "Hello", 2: "Hi"}
print(all(d))
 
# Empty dictionary
d = {}
print(all(d))
 
# all() with condition - to check if all letters of word 'time' are there
l = {"t":1, "i":4, "m":7, "e":0}
print(all(ele > 0 for ele in l.values()))

# Example 5: Working of all() with Strings


# Non-Empty String
s = "Hi There!"
print(all(s))
 
# Non-Empty String
s = "000"
print(all(s))
 
# Empty string
s = ""
print(all(s))# Working of next in python
# Create an iterator
my_iter = iter([1, 2, 3, 4, 5])
print(type(my_iter))

# Retrieve the next item using next()
item1 = next(my_iter)
print(item1)  # Output: 1

# Retrieve the next item again
item2 = next(my_iter)
print(item2)  # Output: 2

# Retrieve the next item multiple times
item3 = next(my_iter)
item4 = next(my_iter)
item5 = next(my_iter)
print(item3, item4, item5)  # Output: 3 4 5

# Attempt to retrieve the next item, but there are no more items in the iterator
item6 = next(my_iter, "No more items")
print(item6)  # Output: "No more items"

'''
In Python, an iterator is an object that represents a stream of data and allows you to 
iterate (loop) over that data, one item at a time. Iterators are used to efficiently 
process large collections of data without the need to load the entire collection into memory. 
They are a fundamental part of Python's iteration protocol and are used extensively in for loops, 
list comprehensions, and other iteration constructs.

To create an iterator in Python, you need to define two methods:

__iter__(): This method returns the iterator object itself. It's called when you create an iterator 
for an iterable (an object that can be looped over).

__next__(): This method returns the next value from the iterator. It's called when you request the 
next item in the iteration.

Here's a simple example of creating and using an iterator:
'''

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Create an instance of the iterator
my_iter = MyIterator(1, 5)

# Iterate over the values using a for loop
for item in my_iter:
    print(item)


'''
In this example:

We define a custom iterator class MyIterator that takes a start and end value.

The __iter__ method returns the iterator object itself (i.e., self).

The __next__ method defines the logic to generate the next value in the iteration. 
When it reaches the end, it raises a StopIteration exception to signal the end of the iteration.

We create an instance of the iterator and use it in a for loop to print values from 1 to 4.

Python also provides several built-in iterable objects (e.g., lists, tuples, dictionaries) 
that can be iterated over using iterators. For example:
'''

my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

# Print the next value from the iterator
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2


'''
In this case, the iter() function is used to create an iterator from a list, and the next() 
function retrieves the next value from the iterator.
'''

