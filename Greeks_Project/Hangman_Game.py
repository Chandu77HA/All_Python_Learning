# Hangman Game in Python

'''
Hangman Wiki:

The origins of Hangman are obscure meaning not discovered, but it seems to have arisen in Victorian times,
 ” says Tony Augarde, author of The Oxford Guide to Word Games. The game is mentioned in Alice Bertha Gomme’s
   “Traditional Games” in 1894 under the name “Birds, Beasts and Fishes.” The rules are simple; a player writes
     down the first and last letters of a word and another player guesses the letters in between. In other sources,
       [where?] the game is called “Gallows”, “The Game of Hangin”, or “Hanger”. 

Implementation:

This is a simple Hangman game using Python programming language. Beginners can use this as a small 
project to boost their programming skills and understanding logic.


The Hangman program randomly selects a secret word from a list of secret words. The random module will 
provide this ability, so line 1 in program imports it.
The Game: Here, a random word (a fruit name) is picked up from our collection and the player gets 
limited chances to win the game.
When a letter in that word is guessed correctly, that letter position in the word is made visible. 
In this way, all letters of the word are to be guessed before all the chances are over. 
For convenience, we have given length of word + 5 chances. For example, word to be guessed is mango, 
then user gets 5 + 5 = 10 chances, as mango is a five-letter word.

'''


# Python Program to illustrate
# Hangman Game
import random
from collections import Counter

someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
print(someWords)
print(type(someWords))
# randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords)
print(word)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()

    playing = True
    # list for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 5
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0: # flag is updated when the word is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                print(k)
                for _ in range(k):
                    letterGuessed += guess # The guess letter is added as many times as it occurs

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct word is guessed fully,
                elif (Counter(letterGuessed) == Counter(word)):
                    # the game ends, even if chances remain
                    print('The word is:', end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break # To break out of the for loop
                    break # To break out of the while loop
                else:
                    print('_', end=' ')

        # If the user has used all of his chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()


'''
Code Explanation:

The code starts by importing the random module.
This module provides a way to generate random numbers.
Next, the code creates someWords, which is a list of fruit names.
The list is split into spaces using the string ‘ ‘, and then each space is replaced with a letter.
Next, the code randomly selects a secret word from our someWords list.
This word will be used as the input for the game later on.
The next part of the code checks to see if the user has entered an alpha character (a letter that appears in front of other letters).
If not, then they are asked to enter only a letter.
If they enter an alpha character, then it’s assumed that they want to guess at another letter in word .
So, this part of the code checks to see if guess matches one of the letters in word .
If it does, then chances is updated and flag is set to 1 .
Otherwise, chances is decreased by 1 and flag remains at 0 .
The next part of the code tries to guess at another letter in word .
If guess isn’t valid (i.e., it doesn’t match any of the letters in word ), then print() prints out all empty spaces for letters in word , and
The code starts by importing the random module.
This module provides us with a number of useful functions, one of which is the choice function.
This function allows us to randomly choose a secret word from our list of words.
Next, we create some variables which will be used throughout the program.
These include someWords , word and letterGuessed .
letterGuessed will store the letter guessed by the player, while chances will store the number of times that the player has correctly guessed the word so far.
correct will keep track of how many letters have been guessed so far and flag will indicate whether or not the player has guessed the word correctly.
We then start looping through our list of words and randomly choosing a secret word from it.
'''