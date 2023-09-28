print()
print("# 1)Adding new value to the dictionary")
print()
bike = {
    "brand": "honda",
    "model": "unicorn",
    "year": 2020
}
print()

show1 = bike.values()
print(show1)

bike["year"] = 2022
print(show1)
print()

print("# 2)Accessing items of a dictionary")
print()
bike = {
    "brand": "honda",
    "model": "unicorn",
    "year": 2020
}
show3 = bike["year"]
print(show3)
print()

print("# 3)Get keys ")
print()
bike = {
    "brand": "honda",
    "model": "unicorn",
    "year": 2020
}
show2 = bike.keys()
print(show2)
print()

print("# 4)Get values ")
print()
bike = {
    "brand": "honda",
    "model": "unicorn",
    "year": 2020
}
show4 = bike.values()
print(show4)
print()

print()
print("# 5)Make changes in the original Dictionary ")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": 2019
}
show5 = bike.values()
print(show5)

bike["year"] = 2021
print(show5)
print()

print("# 6)Get items in the Dictionary as a tuple in the list")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": 2019
}
show6 = bike.items()
print(show6)
print()

print("# 7)Adding Making a changes in the original dictionary and see that a item list is updated as well")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": 1997
}
show7 = bike.items()
print(show7)

bike["colour"] = "gray"
bike["year"] = "2021"
bike["price"] = "97000"

print(show7)
print()

print("# 8)if statement and in to determine the key is present in the dictionary")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
if "price" in bike:
    print("yes, the price is present in the bike")
else:
    print("yes, the price is not present in the bike")

show8 = bike["price"]
print(show8)

print()
print("# 9)Change values")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}

bike["year"] = 2018
bike["model"] = "starcity"
print(bike)
print()

print("# 9)Change values")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
print(bike)
bike["year"] = 2018
bike["model"] = "starcity"
bike["price"] = "101000"
print(bike)
print()

print("# 10)Update Dictionary")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
print(bike)
bike.update({"year": 2022})
print(bike)
print()

print("# 12)Removing Items (last item)")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
print(bike)
bike.pop("year")
print(bike)

print("# 13)Removing Items (last item)")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
print(bike)
bike.popitem()
print(bike)
print()

print("# 14)Removing Items using del keyword")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
print(bike)
del bike["model"]
print(bike)
print()

print("# 15)del keyword to delete dictionary itself")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
print(bike)
del bike
print(bike)
print()

print("# 16)Clear Method empties the Dictionary:")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
print(bike)
bike.clear()
print(bike)
print()

print()
print("# 17)Loop through dictionary using for loop (Print all key names)")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
for n in bike:
    print(n)
print()

print("# 18)Loop through dictionary using for loop (Print all Values)")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
for n in bike:
    print(bike[n])
print()

print("# 19)values method to return values of dictionary")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
for n in bike.values():
    print(n)
print()

print("# 20)keys method to return keys of dictionary")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
for n in bike.keys():
    print(n)
print()

print("# 20)Loop through both keys and values using items")
print()
bike = {
    "brand": "tvs",
    "model": "jupiter",
    "year": "2017",
    "price": "97000"
}
for m, n in bike.items():
    print(m, n)
print()

print("# 21)Copy of the dictionary with copy method")
print()
bike1 = {
    "brand": "hero honda",
    "model": "passion",
    "year": "2008",
    "price": "55000"
}
bike2 = bike1.copy()
print(bike2)
print()

print("# 21)Copy of the dictionary with dict function")
print()
bike1 = {
    "brand": "hero honda",
    "model": "passion",
    "year": "2008",
    "price": "55000"
}
print(bike1)
bike2 = dict(bike1)
print(bike2)
print()

print("# 21)Nested Dictionaries")
print()

autofamily = {
"bike1" : {
    "brand": "hero honda",
    "model": "passion",
    "year": "2008"
},
"bike2" : {
    "brand": "honda",
    "model": "unicorn",
    "year": "2020"
},
"car1" : {
    "brand": "bmw",
    "model": "7 series",
    "year": "2025"
}
}
print(autofamily)
print()

print("# 22)Create 3 Dictionaries and create 1 Dictionary that contain other 3 Dictionary")
print()

bike1 = {
    "brand": "hero honda",
    "model": "passion",
    "year": "2008"
}
bike2 = {
    "brand": "honda",
    "model": "unicorn",
    "year": "2020"
}
car1 = {
    "brand": "bmw",
    "model": "7 series",
    "year": "2025"
}

autofamily = {
    "tiger1" : bike1,
    "tiger2" : bike2,
    "tiger3" : car1
}

print(autofamily)

"
menu = {
"esspresso": 20,
"capici_full_green": 30,
"capici_toned": 40,
"capici_skimmed":50,
"falt_white_full_cream":20,
"falt_white_full_toned":30,
"falt_white_full_skimmed":40,
"lemmon" : 30,
"regular_full_green": 20,
"regular_full_tonned": 30,
"regular_full_skimmed": 40,
"masala_full_green": 20,
"masala_full_tonned": 30,
"masal_full_skimmed":40,
"toast":10,
"muffin": 30,
"samaosa": 50,
"volls":40
}
"""
print(menu(""))
# Coffe
menu = {
    "esspresso": 20
    "capici_full_green":30
    "capici_toned" = 40
    "capici_skimmed" = 50
    "falt_white_full_cream" = 20
    "falt_white_full_toned" = 30
    falt_white_full_skimmed" = 40
    #tea
    lemmon = 30
    regular_full_green = 20
    regular_full_tonned = 30
    regular_full_skimmed = 40
    masala_full_green = 20
    masala_full_tonned = 20
    masal_full_skimmed = 20
    #tea
    toast = 10
    muffin = 30
    samaosa = 50
    volls = 40
}

menu = {
    "coffee":50,
    "green_coffee":60,
    "tea":40,
    "green_tea":50,
    "toast":70,
    "samosa":80
}
"""

"