# INTERACTIVE HANGMAN GAME

Hangman is a python terminal game, deployed on HEROKU. The user can play the game at three different levels of difficulty (based on lenghth of word). The player wins the game if they guess the word correctly in the allotted number of guesses. They lose if they fail to guess the correct word in the number of guesses given based on the level of difficulty they chose: 5 lives for EASY, 7 for MEDIUM and 10 for HARD.

After each incorrect guess, a life is lost and the contruction of the gallows and the hanging figure increases.

![CHANGE THIS](./assets/readme/amiresponsive.png)

## How to play

After the player chooses a level of difficulty, a random word will be given and the player will guess one letter at a time. If the letter is part of the word, it will appear in lieu of one of the blank spaces ( _ ). If the letter is not in the word, a life will be lost and a part of the gallows or a body part of the figure will appear. 

The player continues guessing until they complete the word correctly, winning the game, or until all lives are lost and they are hung, signifying the game is over. For either outcome, an end of game message will appear. The player will then have the opportunity to play again, with a different random word, should they choose.

![CHANGE THIS](./assets/readme/diagram.png)

## Features

* Generate a random word for the player to guess. The word is shown as a set of underscores symbolizing each letter. The underscore characters are shown as letters when the player guesses a correct letter. 
* Player chooses a level of difficulty (easy, medium, hard) and the number of lives is reflected (10, 7, 5, respectively).
* If the player makes an incorrect guess, a life is lost and the gallows and hanging figure are built piece by piece (letter by letter). Number of lives remains unchanged if the player guesses a correct letter.
* Error message shown for: duplicate guesses, numbers or special characters.
* Various colors included for aesthetic purposes and as a way to guide the player: E for easy level is in green, for example, yellow for medium and red for hard when the player chooses a level at the outset.

## Testing

* Self-tested for various bugs and functionality.
* Self-tested for all scenarios with invalid guesses (numbers, special characters).
* Tested for all scenarios with successful guesses (letters only).
* Friends and colleagues did the same once the first round of testing was completed by the creator (me).

### PEP8 valitated with no errors
* CHECK THIS!!! ENDED HERE

## Bugs

    1. Special characters (*!"£$%^^& etc.) were possible
        - original solution of using list of banned characters was no longer feasible. isalpha() method was implemented to address this bug
    2. Throughout testing, multiple letters could be entered by the player
        - new condition created that checks for amount of letters
    3. On Heroku, initial encrypted word does not seem to be displaying spaces between characters, resulting in unclear word guess
        - fixed by adding spaces between letters
    4. Some lines are too long
        - fixed indentation and line breaks as per PEP8

## No other known bugs

# Deployment
    This project was deployed onto Heroku

## Steps
    - Create Heroku App
    - Set the buildbacks to python and NodeJS
    - link Heroku app to the repository
    - Deploy manually

# Credits

    - https://www.youtube.com/watch?v=cJJTnI22IF8&t=2s&ab_channel=KylieYing - this was used to understand the logic behind hiding characters in the word
    - https://www.tutorialspoint.com/python/string_isalpha.htm - for isalpha() method and its uses
    - https://www.w3schools.com/python/ref_string_upper.asp - for upper() method to keep user input in uppercase
    - https://ascii.co.uk/art - ASCII art taken from here
    - https://pypi.org/project/colorama/ - for implementing colors into the game