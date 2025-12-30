# rock,paper,scissor game
import random

import random

running = True
while running:
    options = ("rock", "paper", "scissor")
    computer = random.choice(options)
    player = input("Enter your choice : ").lower().strip()
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    elif player == "scissor" and computer == "paper":
        print("you win!")
    else:
        print("you lose!")

    play_again = input("Do you want to play again? (y/n): ").lower().strip()

    if play_again =="n".lower():

        running =False

    if play_again != "n" and play_again != "y".lower():
        print("value error.please choice correct value!")



print("Thank you for playing!")



