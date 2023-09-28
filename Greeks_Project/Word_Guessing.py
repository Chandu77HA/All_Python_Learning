# Python program for word guessing game

'''
Python is a powerful multi-purpose programming language used by multiple giant companies. 
It has simple and easy-to-use syntax making it the perfect language for someone trying to 
learn computer programming for the first time. It is a high-level programming language, and 
its core design philosophy is all about code readability and syntax that allows programmers 
to express concepts in a few lines of code.

In this article, we will use the random module to make a word-guessing game. This game is 
for beginners learning to code in python and to give them a little brief about using strings, 
loops, and conditional(If, else) statements.

random module: Sometimes we want the computer to pick a random number in a given range, 
pick a random element from a list, pick a random card from a deck, flip a coin, etc. The 
random module provides access to functions that support these types of operations. One 
such operation is random.choice() method (returns a random item from a list, tuple, or string.) 
that we are going to use in order to select one random word from a list of words that we’ve created.

Example 1: Word guessing game

In this game, there is a list of words present, out of which our interpreter will choose 1 random word. 
The user first has to input their names and then, will be asked to guess any alphabet. If the random 
word contains that alphabet, it will be shown as the output(with correct placement) else the program 
will ask you to guess another alphabet. The user will be given 12 turns(which can be changed accordingly) 
to guess the complete word.

Below is the python implementation: 
'''
import random
# library that we use in order to choose
# on random words from a list of words

name = input("What is your name? : ")

# Here the user is asked to enter the name first

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words)


print("Guess the characters")

guesses = ''

# any number of turns can be used here
turns = 12


while turns > 0:

	# counts the number of times a user fails
	failed = 0

	# all characters from the input
	# word taking one at a time.
	for char in word:

		# comparing that character with
		# the character in guesses
		if char in guesses:
			print(char)

		else:
			print("_")

			# for every failure 1 will be
			# incremented in failure
			failed += 1

	if failed == 0:
		# user will win the game if failure is 0
		# and 'You Win' will be given as output
		print("\nYou Win")

		# this print the correct word
		print("The word is: ", word)
		break

	# if user has input the wrong alphabet then
	# it will ask user to enter another alphabet
	print()
	guess = input("guess a character:")

	# every input character will be stored in guesses
	guesses += guess

	# check input with the character in word
	if guess not in word:

		turns -= 1

		# if the character doesn’t match the word
		# then “Wrong” will be given as output
		print("Wrong")

		# this will print the number of
		# turns left for the user
		print("You have", + turns, 'more guesses')

		if turns == 0:
			print("You Loose")


'''The code starts by asking the user to enter their name.
The code then prints a message saying “Good Luck!”
and sets a variable called name to the inputted name.
Next, the code creates a list of words using the built-in function word().
This function takes in an input string and returns a list of strings.
In this case, the list will contain five strings: rainbow, computer, science, programming, and python.
The next part of the code is where the randomness happens.
The code will randomly choose one string from the list of words and store it in word variable.
Then it will print out that word along with a space at the end.
After printing out each word, the code checks to see if any user has entered an incorrect letter by comparing each character in guess with those in word .
If they don’t match up then guess is set to “Wrong” and turns is decreased by 1 .
If there are no more letters left in guess , then Guess You Lose is printed .
Otherwise turn s is increased by 1 and loop continues until either Guess You Win or Wrong is printed .
Finally , if turn s equals 0 , then you have won !
Otherwise Wrong will be
The code will randomly choose one word from a list of words.
The user is then asked to enter the characters for that word.
Once the user enters all of the characters, the code checks to see if those characters are in the word that was chosen.
If they are not, it prints out “Wrong” and decreases the number of turns left for the user by 1.
If all turns have been used, then the code will print “You Lose.

'''

# Modified Code

'''
import random

def is_valid_input(user_input):
    # Check if the input is a single character
    return len(user_input) == 1 and user_input.isalpha()

name = input("\nWhat is your name: ")
print("\nGood Luck, ", name)
words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']
word = random.choice(words).lower()
print("\nGuess the characters:\n")
guesses = ''
turns = 12

while turns > 0:
    failed = 0
    print("\nPreviously gussed words are :", end = ' ')
    for item in guesses:
        print(item, end = ', ')
    print("\n")
    print("The word with gussed characters :", end = ' ')
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed += 1
    if failed == 0:
        print("\n\nYou Win...! with", turns, 'more guesses left')
        print("\nThe word is:", word)
        break
    print("\n")
    try:
        guess = input("Enter a character: ").lower()
        if not is_valid_input(guess):
            print("\nYou have", turns, 'more guesses left')  # Display remaining guesses here
            raise ValueError("\nInvalid input. Please enter a single character only..!")
        if guess in guesses:
            print("\nYou already guessed that character.")
            print("\nYou have", turns, 'more guesses')  # Display remaining guesses here
            continue
        guesses += guess
        if guess not in word:
            turns -= 1
            print("\nWrong")
        print("\nYou have", turns, 'more guesses left')  # Display remaining guesses here
        if turns == 0:
            print("You Lose")
    except ValueError as e:
        print(e)

'''