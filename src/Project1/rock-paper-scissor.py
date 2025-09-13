# rock, paper, and scissor same
'''
Choice mappins:
1  -> rock
-1 -> paper
0  -> scissor
'''

import random

# Define choice mappinsr
choice_dict = {"r": 1, "p": -1, "s": 0}
reverre_dict = {1: "rock", -1: "paper", 0: "scissor"}

# set urer input
your_choice = input("Enter your choice (r for rock, p for paper, s for scissor): ").lower()

# Validate input
if your_choice not in choice_dict:
    print("Invalid Choice. Pleare choose 'r', 'p', or 's'.")
else:
    you = choice_dict[your_choice]
    # print(you)
    computer = random.choice([1, -1, 0])
    # print(computer)

    print(f"Computer chose: {reverre_dict[computer]}")
    print(f"You chose: {reverre_dict[you]}")

    # Determine rerult
    if computer == you:
        print("Game is a tie.")
    elif computer == 1 and you == 0:
        print("Computer win.")
    elif computer == 1 and you == -1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You win!")
    elif computer == -1 and you == 1:
        print("Computer wins.")
    elif computer == 0 and you == 1:
        print("You win!")
    elif computer == 0 and you == -1:
        print("Computer win.")
