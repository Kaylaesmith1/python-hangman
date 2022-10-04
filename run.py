# All code or resources used in this project are credited in the README file.
import random
from words import words
from hangedman import lives_left
import string
from time import sleep


class colors:
    purple = '\033[95m'
    cyan = '\033[96m'
    green = '\033[92m'
    red = '\033[91m'
    orange = '\033[33m'
    white = '\033[0m'
    bold = '\033[1m'


def player_name():
    """
    Asks player to enter their name. This will be used to wish them luck and
    either congratulate them or give condolences at game end.
    """
    global name
    while True:
        name = input("\nWho's playing today? ")
        if name.isalpha():
            break
        print(colors.red + "Valid letters (A-Z) only please.\n" + colors.white)
    sleep(1)
    print("\nGood luck, " + colors.cyan + f"{name.capitalize()}!")
    return name


def get_word(words):
    """
    Choose random word from 'words.py' file
    skip 'invalid' words (hyphenated or spaced)
    """
    word = random.choice(words)

    while ' ' in word or '-' in word:
        word = random.choice(words)

    return word.upper()


def hangman_game():
    """
    Interactive game to guess a random word using single letters
    in a specific number of 'lives'.
    """
    hangman_logo()
    welcome_rules()
    player_name()
    word = get_word(words)
    lett_needed = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    lett_guessed = set()  # letters user guesses

    lives = choose_level()

    while len(lett_needed) > 0 and lives > 0:
        print("\nYou've used these letters: ", ' '.join(sorted(lett_guessed)))
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
                lives = lives - 1
                print('\nSorry,', user_guess, 'is not in the word.')

        elif user_guess in lett_guessed:
            print("\nYou've guessed this letter already. Please try again.")

        else:
            print("That doesn't work, please type in a valid letter, A-Z.")

    # player is hanged
    if lives == 0:
        print(colors.red + lives_left[lives] + colors.white)
        print(colors.bold + f"Oh no, {name.capitalize()}, you've been hanged!")
        print("The word was" + colors.red, word)
    else:
        print(colors.bold + f"Congrats {name.capitalize()}!")
        print("You're right, the word was" + colors.cyan, word)


def hangman_logo():
    """
    The word 'Hangman' is spelled out
    in purple letters at the beginning of the game.
    """
    print(colors.purple +
            """
             _   _                                         _
            | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __ | |
            | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \| |
            |  _  | (_| | | | | (_| | | | | | | (_| | | | |_|
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_(_)
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
    sleep(1)
    print('Try to guess the random word before you get hung. \n')
    sleep(1)
    print('Follow the instructions to choose a level: easy, medium or hard.\n')
    sleep(1)
    print('----------------------------------------')
    sleep(1)


def choose_level():
    """
    Type 'e', 'm', or 'h' to choose a level:
    easy (10 lives), medium (7 lives), hard (5 lives).
    """
    print(colors.white + "\nTo start, please choose...\n")
    print(colors.green, 'E' + colors.white, 'for easy and \n')
    print("you'll get" + colors.green, "10 lives. \n" + colors.white)
    sleep(1)
    print(colors.orange, 'M' + colors.white, 'for medium and \n')
    print("you'll get" + colors.orange, "7 lives. \n" + colors.white)
    sleep(1)
    print(colors.red, 'H' + colors.white, 'for hard and \n')
    print("you'll get" + colors.red, "5 lives. \n" + colors.white)

    difficulty = True
    while difficulty:
        options = input("\n ").upper()
        if options == "E":
            lives = 10
            return lives
        elif options == "M":
            lives = 7
            return lives
        elif options == "H":
            lives = 5
            return lives
        else:
            print(colors.red + "\n Please write E, M or H" + colors.white,)
            print(" to choose your level of difficulty.")


hangman_game()


while True:
    if input(colors.white + "Want a rematch? (Y/other > quit)").upper() == "Y":
        hangman_game()
    else:
        print(colors.purple + "Thanks for playing... \n")
        break

sleep(1)
hangman_logo()
