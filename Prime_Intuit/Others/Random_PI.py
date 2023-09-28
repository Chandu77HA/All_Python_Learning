import random
# Random functions
# random.seed(100)
# Seed method is used to initialize the random number generator
# Seed function is used to save the state of the current random function

# Random : Returns random float number between 0 to 1
rand = random.random()
print("Random", rand)

# Uniform : Returns random float number between a to b
lion = random.uniform(2, 8)
print("Uniform", lion)

# Randint : Returns random integer number between a to b
tiger = random.randint(1, 6)
print("Randint", tiger)

# Getrandbits : Returns the Integer number from the min decimal value and max decimal
# value that a given bits k can take Takes bits as an input and returns the random
# integer number that the bits can store

deer = random.getrandbits(5)
print("Getrandbits", deer)

# Choice : Returns random number from the sequence passed
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
beer = random.choice(l1)
print("Choice", beer)

# Choices : Returns multiple random number from the sequence passed
l3 = [65, 47, 25, 35, 48, 98, 77, 55, 67, 54, 22, 38]
rand, rand1 = random.choices(l3, k=2)
print("Choices", rand, rand1)

l2 = [54, 74, 36, 47, 85, 14, 23, 58, 99]
ball, bat, wicket = random.choices(l2, k=3)
print("Choices in Cricket", ball, bat, wicket)

# Will generate random number from start to stop in step of steps
deer = random.randrange(0, 100, 10)
print("Randrange", deer)

# Randbelow :
# Will generate random number Integer value below the number specified
import secrets
dog = secrets.randbelow(7)
print("Randbelow", dog)
# Shuffle
random.shuffle(l1)
print(l1)