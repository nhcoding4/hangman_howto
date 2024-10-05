import random

words = ["apples", "oranges", "pears"]

selected_word = random.choice(words)

dashes = ""

for letter in selected_word:
    dashes += "-"

print(dashes)

# -------------------------------------------------------------------------------------------------

# Step 4
user_guess = input("Make a guess!\n-> ").lower()[0]

# -------------------------------------------------------------------------------------------------