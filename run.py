import random
from words import words
from hangedman import lives_left
import string


class colors:
    blue = '\033[38;5;159m'
    green = '\033[92m'
    red = '\033[91m'
    white = '\033[0m'
    bold = '\033[1m'


def get_word(words):
    """
    Choose random word from 'words.py' file
    skip 'invalid' words (hyphenated or spaced)
    """
    word = random.choice(words)

    while ' ' in word or '-' in word:  # still look if word has hyphen / space
        word = random.choice(words)

    return word.upper()


def hangman_game():
    hangman_logo()
    word = get_word(words)
    lett_needed = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    lett_guessed = set()  # letters user guesses

    lives = 1

    # get user input
    while len(lett_needed) > 0 and lives > 0:
        print("\nYou've used these letters: ", ' '.join(lett_guessed))
        print('\nLives left:', lives, )

        word_guess = [lett if lett in lett_guessed else '_' for lett in word]
        print(colors.red + lives_left[lives] + colors.white)
        print('Current word: ', ' '.join(word_guess))
        print('\n----------------------------------------')

        user_guess = input('\nPlease guess a letter: ').upper()
        
        if user_guess in alphabet - lett_guessed:
            lett_guessed.add(user_guess)
            if user_guess in lett_needed:
                lett_needed.remove(user_guess)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nSorry,', user_guess, 'is not in the word.')

        elif user_guess in lett_guessed:
            print("\nYou've guessed this letter already. Please try again.")

        else:
            print('Error. Please type in a valid letter.')

    # player is hanged
    if lives == 0:
        print(colors.red + lives_left[lives] + colors.white)
        print(colors.red + "You've been hanged! The word was", word)
        print()
    else:
        print("Congrats! You're right, the word was", word, '!')

def hangman_logo():
    print(colors.green +
        """
         _   _                                           _                                         
        | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __   | |
        | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\  | |
        |  _  | (_| | | | | (_| | | | | | | (_| | | | | |_| 
        |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_| (_)
                            |___/                       
        """
    + colors.white)


hangman_game()
