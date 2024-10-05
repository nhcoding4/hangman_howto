import random

words = ["apples", "oranges", "pears"]

selected_word = random.choice(words)

dashes = ""

# -------------------------------------------------------------------------------------------------

# Step 3

for letter in selected_word:
    dashes += "-"

print(dashes)

# -------------------------------------------------------------------------------------------------