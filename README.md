# INTERACTIVE HANGMAN GAME

Hangman is a Python terminal game, deployed on Heroku. The user can play the game at three different levels of difficulty (based on lenghth of word). The player wins the game if they guess the word correctly in the allotted number of guesses. They lose if they fail to guess the correct word in the number of guesses given based on the level of difficulty they chose: 5 lives for EASY, 7 for MEDIUM and 10 for HARD.

After each incorrect guess, a life is lost and the contruction of the gallows and the hanging figure increases.

At the beginning of the game, the player is asked to give their name, which is then used to wish them luck and, at the end of the game, congratulate them on winning or give condolences on their loss.

Once the game is finished, the player is asked if they'd like to play again. Entering 'Y' will restart the game with a new random word and the difficulty level chosen by the player. Entering in anything other than 'Y' ('N' or another character) will conclude the game with a 'Thanks for playing...' message.

![CHANGE THIS](./assets/readme/amiresponsive.png)

## How to play

First the player chooses a level of difficulty and a random word will be shown using ( _ ) markers for the letters. The player will then guess one letter at a time. If the letter is part of the word, it will appear in lieu of one of the blank spaces ( _ ). If the letter is not in the word, a life will be lost and a part of the gallows or a body part of the figure will appear. 

The player continues guessing until they complete the word correctly, winning the game, or until all lives are lost and they are hung, signifying the game is over. For either outcome, an end of game message will appear incorporating the name the player entered at the beginning. The player will then have the opportunity to play again, with a different random word, should they choose. 

## Features

* Player name is recorded and used to greet them and at the end of the game, both in the congratulatory and condolence messages.
* A function generates a random word for the player to guess. The word is shown as a set of underscores symbolizing each letter. The underscore characters are shown as letters when the player guesses a correct letter. 
* The player chooses a level of difficulty (easy, medium, hard) and the number of lives is reflected (10, 7, 5, respectively).
* If the player makes an incorrect guess, a life is lost and the gallows and hanging figure are built piece by piece (letter by letter). The number of lives remains unchanged if the player guesses a correct letter.
* Error message shown for: duplicate guesses, numbers or special characters.
* Various colors included for aesthetic purposes and as a way to guide the player: E for easy level is in green, for example, yellow for medium and red for hard when the player chooses a level at the outset. Color also used for the player's name at the beginning.

## Testing

* Self-tested for various bugs and functionality.
* Self-tested for all scenarios with invalid guesses (numbers, special characters).
* Tested for all scenarios with successful guesses (letters only).
* Friends and colleagues did the same once the first round of testing was completed by the creator (me).

### PEP8 valitated with no errors
* CHECK THIS!!! - New pep8 page?

## Bugs

    1. At the end of the game, the player is asked if they want to play again. The player had to enter 'N' twice before the 'Thanks for playing' and hangman logo appeared. The while loop was breaking in the wrong place; this is now fixed.

    2. The aforementioned while loop was also causing an error in asking the player if they wanted to play again. At the end of game one, the player was asked if they wanted to play again. If they chose to, the game ran again but at the end did NOT ask if they wanted to play a third time. This is solved now in correcting the syntax of the while loop. It now works properly if the player chooses to play again or to quit. 

    3. The number of lives ISN'T WORKING PROPERLY. FIX THIS BUG. GIVES WHATEVER THE DEFAULT IS SET TO. NEED TO WRITE FUNCTION.

## No known unsolved bugs

# Deployment
    This project is deployed on Heroku.

## Steps
    - View a few YouTube videos for background on ways to approach creating a Hangman game in Python.
    - Create a Hangman game that incorporates user data, interactivity, difficulty levels, play again feature and colored text.
    - Deploy game to Heroku
    - Link the GitHub repository to the Heroku app (with Node JS)
    - Deploy

# Credits

    - I used a YouTube tutorial by Kylie Ying for general background knowledge and, specifically, to edit out spaces and '-' characters in the list of words used for the game.
    
    Resource: https://www.youtube.com/watch?v=cJJTnI22IF8&t=2s&ab_channel=KylieYing

    - For timed space betweeen printed statements I imported sleep() from time, which I found through a Google search.
    
    Resource: https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/#:~:text=Make%20your%20time%20delay%20specific,after%20a%20slight%20delay.%22

    - To incorporate colors and font weights, I used the 'class' method found through a Google search and labeled and called the colors and bold type accordingly.
    
    Resource: https://www.delftstack.com/howto/python/python-bold-text/#:~:text=text%20in%20Python.-,Print%20Bold%20Text%20in%20Python%20Using%20the%20ANSI%20Escape%20Sequence,%3A%20'%5C033%5B1m'%20

    - I had some issues with my while loop in calling the game function again should the player want to play again. I credit Ed B_Alum on Slack for helping, as well as Sean in a tutoring session. Both of their input and ultimately Sean's redefining of my while loop solved the bug and made my code cleaner. 