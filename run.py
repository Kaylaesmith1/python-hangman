import random
from words import words

#!!ADD COLORS, ADD LEVELS (BASED ON NUMBER OF LIVES LEFT OR BASED ON WORD LENGTH?)


def get_word(words):
    """ 
    Choose random word from 'words.py' file
    skip 'invalid' words (hyphenated or spaced)
    """
    word = random.choice(words)

    while ' ' in word or '-' in word: #keeps looking if word has hyphen or space
        word = random.choice(words)

    return word.upper()

def hangman_game():
    word = get_word(words)
    letters_needed = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    letters_guessed = set() #letters user guesses

    #get user input
    user_guess = input('Guess a letter: ').upper()
    if user_guess in alphabet - letters_guessed:
        letters_guessed.add(user_guess)
        if user_guess in word - letters_needed:
            letters_needed.remove(user_guess)
    
    elif user_guess in letters_guessed:
        print("You've guessed this letter already. Please try again.")
    
    else: 
        print('Error. Please type in a valid letter.')

user_input = input('Please type a letter: ')
print(user_input)

