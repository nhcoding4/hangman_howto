import random

words = ["apples"]

selected_word = random.choice(words)

dashes = ""

for letter in selected_word:
    dashes += "-"

print(dashes)

user_guess = input("Make a guess!\n-> ").lower()[0]

# -------------------------------------------------------------------------------------------------

# Step 5

buffer = ""

for i, letter in enumerate(selected_word):    
    if user_guess == letter:        
        buffer += user_guess
    else:
        buffer += dashes[i]

dashes = buffer

# -------------------------------------------------------------------------------------------------