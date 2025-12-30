# number guessing game
import random

low_value =1
high_value=100
solution = random.randint(low_value, high_value)
guesses = 0
__running = True
print("welcome to number guessing game .")
print(f"Please enter a valid number from {low_value} upto {high_value}: ")
while __running:
    choice = input(f"Enter your a number from {low_value} upto {high_value}: ")
    if choice.isdigit():
        choice = int(choice)
        guesses += 1
        if choice > high_value or choice < low_value:
            print("your guess is out of the range")
        elif choice > solution:
            print("your guess is too high")
        elif choice < solution:
            print("your guess is too low")
        else:
            print(f"CORRECT! The answer was {solution}")
            print(f"You guessed {guesses} times.")
            __running = False



    else:
        print("your choice is invalid.")
        input(f"Please enter a valid number from {low_value} upto {high_value}: ")
        # if int(choice) < low_value or int(choice) > high_value:
        #     print("your choice is out of range.")
    #     input(f"Please enter a valid number from {low_value} upto {high_value}: ")
    #
    # elif int(choice) >= low_value and int(choice) <= high_value:
    #     guesses += 1
    #     if int(choice) < low_value:
    #                 print("it is lower than solution.")
    #     elif int(choice) > high_value:
    #         print("it is higher than solution.")
    #     elif int(choice) == solution:
    #
    #         print("your choice is correct.")
    #         print(f"you guessed {guesses} times.")
    #         __running = False
    #
    #
    # # print(solution)
