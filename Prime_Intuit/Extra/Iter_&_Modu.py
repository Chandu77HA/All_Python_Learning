
# CONTENTS

# 1) ITERATOR
# 2) MODULES

#  =====>>>>> 1) ITERATOR
print()
print("==>> 1) Create Iteration to returns the Number")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a+=1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print()
print("==>> 2) Create Iteration to returns the Numbers and Stop Iteration")

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 7:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


#  =====>>>>> 2) MODULES

def greeting(name):
    print("Hello, " + name)
def fromwhere(place):
    print("Iam from " + place)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

#  =====>>>>> 3) DATE AND TIME

 x = datetime.datetime(2022-9-13 0:0:01.224898)

 print()
import datetime
y = datetime.datetime.now()

print(y)
print()
print(y.strftime("%a"))
print(y.strftime("%A"))
print(y.strftime("%w"))
print(y.strftime("%d"))
print(y.strftime("%b"))
print(y.strftime("%B"))
print(y.strftime("%m"))
print(y.strftime("%y"))
print(y.strftime("%Y"))
print(y.strftime("%H"))
print(y.strftime("%I"))
print(y.strftime("%p"))
print(y.strftime("%M"))
print(y.strftime("%S"))
print(y.strftime("%f"))
print(y.strftime("%j"))
print(y.strftime("%U"))
print(y.strftime("%W"))
print(y.strftime("%c"))
print(y.strftime("%C"))
print(y.strftime("%x"))
print(y.strftime("%X"))
print(y.strftime("%G"))
print(y.strftime("%u"))
print(y.strftime("%V"))

#  =====>>>>> 3) MATH


print()
import math

pqr = math.sqrt(64)

print(pqr)

abc = math.ceil(1.2)
ghi = math.floor(1.8)

print(abc)
print(ghi)

lmn = math.pi
print(lmn)

#  =====>>>>> 4) Json


print()
import json

abc = '{ "name":"Smith", "age":30, "city":"Sydney"}'

efg = json.loads(abc)

print(efg["name"])
print(efg["age"])
print(efg["city"])

import json

hij = {
    "name": "Smith",
    "age": 30,
    "city": "Sydney"
}

klm = json.dumps(hij)

print(klm)


import json

print(json.dumps({ "name":"Smith", "age":30, "city":"Sydney"}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(25.236))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))




import json

abc = {
    "name": "Messi",
    "age": "34",
    "married": True,
    "divorced": False,
    "children": ("Tiago", "Mateo"),
    "pets": None,
    "cars": [
        {"model": "bmw 230", "mlg": 8.32},
        {"model": "audi q7", "mlg": 7.47},
    ]
}

cde = json.dumps(abc, indent=4)
print(cde)





import json

abc = {
    "name": "Messi",
    "age": "34",
    "married": True,
    "divorced": False,
    "children": ("Tiago", "Mateo"),
    "pets": None,
    "cars": [
        {"model": "bmw 230", "mlg": 8.32},
        {"model": "audi q7", "mlg": 7.47},
    ]
}

cde = json.dumps(abc, indent=4, separators=(".", "="))
print(cde)





import json

abc = {
    "name": "Messi",
    "age": "34",
    "married": True,
    "divorced": False,
    "children": ("Tiago", "Mateo"),
    "pets": None,
    "cars": [
        {"model": "bmw 230", "mlg": 8.32},
        {"model": "audi q7", "mlg": 7.47},
    ]
}

cde = json.dumps(abc, indent=4, separators=(".", "="), sort_keys=True)
print(cde)


