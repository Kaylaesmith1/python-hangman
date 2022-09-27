import random
from words import words
from hangedman import lives_left
import string


class colors:  # source: https://www.delftstack.com/howto/python/python-bold-text/#:~:text=text%20in%20Python.-,Print%20Bold%20Text%20in%20Python%20Using%20the%20ANSI%20Escape%20Sequence,%3A%20'%5C033%5B1m'%20.
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    orange = '\033[33m'
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
    welcome_rules()
    choose_level()
    word = get_word(words)
    lett_needed = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    lett_guessed = set()  # letters user guesses

    lives = 10

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
        print(colors.bold + "You've been hanged! The word was" + colors.cyan , word)
        print()
    else:
        print("Congrats! You're right, the word was", word, '!')

def hangman_logo():
    print(colors.purple +
        """
         _   _                                           _                                         
        | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __   | |
        | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\  | |
        |  _  | (_| | | | | (_| | | | | | | (_| | | | | |_| 
        |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_| (_)
                            |___/                       
        """
    + colors.white)

def welcome_rules():
    """
    Welcome user to the game
    Give rules of the game
    Choose a level (easy, medium, hard)
    """
    print('Welcome to Hangman! \n')
    print('Try to guess the random word before you get hung. \n')
    print('Follow the instructions to choose a level: easy, medium or hard.\n')
    print('If you want to play again, click XX. Good luck! \n')
    print('\n----------------------------------------')

def choose_level():
    """
    Click 1, 2 or 3 to choose a level:
    easy (10 lives), medium (7 lives), hard (5 lives).
    """
    print('Choose' + colors.green, 'E' + colors.white, 'for easy and \n')
    print("you'll get" + colors.green, "10 lives. \n" + colors.white)
    print('Choose' + colors.orange, 'M' + colors.white, 'for medium and \n')
    print("you'll get" + colors.orange, "7 lives. \n" + colors.white)
    print('Choose' + colors.red, 'H' + colors.white, 'for hard and \n')
    print("you'll get" + colors.red, "5 lives. \n" + colors.white)

    difficulty = True
    while difficulty:
        options = input("\n ").upper()
        if options == "E":
            difficulty = False
            lives = 10
            return lives
        elif options == "M":
            difficulty = False
            lives = 7
            return lives
        elif options == "H":
            difficulty = False
            lives = 5
            return lives
        else:
            print(colors.red + "\n Please write E, M or H" + colors.white,)
            print(" to choose your level of difficulty.")



hangman_game()
