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
