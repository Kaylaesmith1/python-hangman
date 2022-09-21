import random
from words import words
from hangedman import lives_left
import string


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
    word = get_word(words)
    letters_needed = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    letters_guessed = set()  # letters user guesses

    lives = 7

    # get user input
    while len(letters_needed) > 0 and lives > 0:
        print('Lives left:', lives, )
        print("You've used these letters: ", ' '.join(letters_guessed))

        word_guess = [letter if letter in letters_guessed else '-' for letter in word]
        print(lives_left[lives])
        print('Current word: ', ' '.join(word_guess))

    user_guess = input('Guess a letter: ').upper()
    if user_guess in alphabet - letters_guessed:
        letters_guessed.add(user_guess)
        if user_guess in word - letters_needed:
            letters_needed.remove(user_guess)

    elif user_guess in letters_guessed:
        print("\nYou've guessed this letter already. Please try again.")

    else:
        print('Error. Please type in a valid letter.')

user_input = input('Please type a letter: ')
print(user_input)
