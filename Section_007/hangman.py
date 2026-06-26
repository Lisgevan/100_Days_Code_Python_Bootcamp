import random

from hangman_art import stages, logo
from hangman_words import word_list

lives = 6

print(logo)

# Choose random word
chosen_word = random.choice(word_list)
print(chosen_word)

# Create placeholders for each letter
placeholder = ""
word_length = len(chosen_word)
for position in range(1, word_length):
    placeholder += "_"
print(f"Word to quess: {placeholder}")



# ask use to guess a letter

game_over = False
correct_letters = []

while not game_over:
    print(f"************************** TOU HAVE {lives}/6 LEFT ***************************")
    guess = input("Guess a letter: ").lower()

    # check if guess is in the chosen word
    # if guessed right put letter in proper possition
    
    if guess in correct_letters:
        print(f"you already guessed {guess}")
    
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("************************** IT WAS {chosen_word}!  Y O U   L O S E ***************************")
    
    if "_" not in display:
        game_over = True
        print("************************** Y O U   W I N ! ***************************")
        
    # Show Hangman ASCII art
    print(stages[lives])