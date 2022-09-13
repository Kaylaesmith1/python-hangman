import random
from words import words


def get_word(words):
    """ 
    Choose random word from 'words.py' file
    skip 'invalid' words (hyphenated or spaced)
    """
    word = random.choice(words)

    while ' ' in word or '-' in word: #keeps looking if word has hypen or space
        word = random.choice(words)

    return word.upper()

def hangman_game():
    word = get_word(words)
    letters_needed = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    letters_guessed = set() #letters user guesses

    #get user input
    user_guess = input('Guess a letter: ').upper()

user_input = input('Please type a letter: ')
print(user_input)

