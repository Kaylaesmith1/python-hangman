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
    lett_needed = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    lett_guessed = set()  # letters user guesses

    lives = 10

    # get user input
    while len(lett_needed) > 0 and lives > 0:
        print('Lives left:', lives, )
        print("You've used these letters: ", ' '.join(lett_guessed))

        word_guess = [lett if lett in lett_guessed else '_' for lett in word]
        print(lives_left[lives])
        print('Current word: ', ' '.join(word_guess))

        user_guess = input('Please guess a letter: ').upper()
        if user_guess in alphabet - lett_guessed:
            lett_guessed.add(user_guess)
            if user_guess in word - lett_needed:
                lett_needed.remove(user_guess)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nSorry,', lett_guessed, 'is not in the word.')

        elif user_guess in lett_guessed:
            print("\nYou've guessed this letter already. Please try again.")

        else:
            print('Error. Please type in a valid letter.')

    # player is hanged
    if lives == 0:
        print(lives_left[lives])
        print("You've been hanged! The word was", word)
    else:
        print("Congrats! You're right, the word was", word, '!')


user_input = input('Please type a letter: ')


print(user_input)
