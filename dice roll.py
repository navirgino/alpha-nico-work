#ROLLING THE DICE

import random

min=1

max=6

roll_again ="yes"

while roll_again == "yes" or rolle_again == "y":
    print("Rolling the dice...")
    print("The values are...")
    print(random.randit(min, max))
    print(random.randit(min, max))

    roll_again = raw_input("Roll again?")
