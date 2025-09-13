# Snake, Water, and Gun Game
'''
Choice mapping:
1  -> snake
-1 -> water
0  -> gun
'''

import random

# Define choice mappings
choice_dict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "snake", -1: "water", 0: "gun"}

# Get user input
your_choice = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

# Validate input
if your_choice not in choice_dict:
    print("Invalid Choice. Please choose 's', 'w', or 'g'.")
else:
    you = choice_dict[your_choice]
    # print(you)
    computer = random.choice([1, -1, 0])
    # print(computer)

    print(f"Computer chose: {reverse_dict[computer]}")
    print(f"You chose: {reverse_dict[you]}")

    # Determine result
    if computer == you:
        print("Game is a tie.")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == 1 and you == -1:
        print("Computer wins.")
    elif computer == -1 and you == 0:
        print("Computer wins.")
    elif computer == -1 and you == 1:
        print("You win!")
    elif computer == 0 and you == 1:
        print("Computer wins.")
    elif computer == 0 and you == -1:
        print("You win!")
