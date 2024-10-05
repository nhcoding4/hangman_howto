import random

words = ["apples"]

selected_word = random.choice(words)

dashes = ""

for letter in selected_word:
    dashes += "-"

lives_remaining = 6
incorrect_guesses = []

print(dashes)

user_guess = input("Make a guess!\n-> ").lower()[0]

buffer = ""

for i, letter in enumerate(selected_word):    
    if user_guess == letter:        
        buffer += user_guess
    else:
        buffer += dashes[i]


if dashes == buffer:
    lives_remaining -= 1
    incorrect_guesses.append(user_guess)

# -------------------------------------------------------------------------------------------------

# Step 7

if lives_remaining == 0:
    print(f"GAME OVER. The word was {selected_word}.")
    exit(1)  

# -------------------------------------------------------------------------------------------------

dashes = buffer

# -------------------------------------------------------------------------------------------------

# Step 7

if dashes == selected_word:
    print(f"YOU CORRECTLY GUESSED THE WORD: {selected_word}.")
    exit(1)


# -------------------------------------------------------------------------------------------------
