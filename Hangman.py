import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

lives = 6
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)
display = ["_"]* word_length
correct_letters = []

game_over = False

print(f"Word to guess: {''.join(display)}")

while not game_over: 
    print(f"***************{lives}/6 LIVES LEFT ***********************")
    guess = input("Enter a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
        continue
    
    correct_letters.append(guess)
    
    for position in range(word_length):
       letter = chosen_word[position]
       if letter == guess:
           display[position] = letter   
           
    print(f"{''.join(display)}")
       
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} which is not in the word. You loose a life")
        if lives == 0:
            game_over = True
            print(f"******************** It was {chosen_word}! You Loose **************************")
            
    if "_" not in display:
       game_over = True
       print("********************** Your Win *****************************")
       
    print(stages[lives]) 