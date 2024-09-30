# Hangman Game

This is a simple terminal-based Hangman game implemented in Python. The goal of the game is to guess the hidden word by inputting letters, one at a time, before running out of lives.

## Features
- Random word selection from a predefined list.
- ASCII art depicting the hangman stages as lives are lost.
- Tracks guessed letters and prevents duplicate guesses.
- Displays the current state of the word after each guess.
- Ends the game when either the word is fully guessed or all lives are lost.

## How to Play
1. The game starts by displaying the number of blanks (underscores) representing each letter in the word.
2. The player guesses a letter by typing it into the console.
3. If the letter is correct, it fills in the corresponding blanks.
4. If the letter is incorrect, the player loses a life and the hangman image progresses to the next stage.
5. The game continues until the player either guesses the word correctly (wins) or runs out of lives (loses).

## Game Flow
1. At the start of the game, a random word is selected from the predefined list.
2. The word is represented as a series of underscores (`_`), one for each letter.
3. The player guesses letters, which are checked against the word.
   - Correct guesses reveal the letters in their respective positions.
   - Incorrect guesses reduce the number of remaining lives and move the hangman closer to completion.
4. The game ends either when the word is fully guessed or the player runs out of lives.

## Requirements
- Python 3.x
- No additional libraries are needed.

## Running the Game
1. Clone or download the code.
2. Open the terminal in the directory containing the script.
3. Run the Python file:
   ```bash
   python hangman.py

### Key Sections:
- **Introduction:** A brief overview of the game.
- **Features:** Key features like the random word generation, hangman stages, and gameplay mechanics.
- **How to Play:** Basic gameplay instructions.
- **Game Flow:** An outline of how the game progresses.
- **Requirements:** Clarifies that no additional libraries are needed.
- **Running the Game:** Instructions for running the game.
- **Code Explanation:** Breakdown of the code and important variables (like `word_list`, `stages`, `display`).
- **Customization:** How users can modify the word list or the game stages.
- **Example Output:** Provides a sample of what the player will see during gameplay.

You can include this as a `README.md` file in your project folder. Let me know if you need any further adjustments!


