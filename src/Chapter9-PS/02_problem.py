import random


def game():
    print("Welcome to the game! Let's start playing!")

    # Generate a random score between 1 and 50
    score = random.randint(1, 50)
    print(f"Your score is: {score}")

    with open("hiscore.txt", "r") as file:
        hiscore = file.read()
        if(hiscore !=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
            
    if(score > hiscore):
        print("Congratulations! You have the highest score!")
        with open("hiscore.txt", "w") as file:
            file.write(str(score))

    return score

game()