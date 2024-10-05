import random

words = ["apples"]

selected_word = random.choice(words)

dashes = ""

for letter in selected_word:
    dashes += "-"

# -------------------------------------------------------------------------------------------------

# Step 6

lives_remaining = 6
incorrect_guesses = []

# -------------------------------------------------------------------------------------------------

print(dashes)

user_guess = input("Make a guess!\n-> ").lower()[0]

buffer = ""

for i, letter in enumerate(selected_word):    
    if user_guess == letter:        
        buffer += user_guess
    else:
        buffer += dashes[i]

# -------------------------------------------------------------------------------------------------

# Step 6

if dashes == buffer:
    lives_remaining -= 1
    incorrect_guesses.append(user_guess)


# -------------------------------------------------------------------------------------------------

dashes = buffer