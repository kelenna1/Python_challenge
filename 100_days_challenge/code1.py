# ROCK PAPER SCISSORS GAME
import random

choices = ["rock", "paper", "scissors"]

while True:

    userInput = input("let's play rock paper scissors, take a pick(or enter exit to quit playing): ")

    if userInput == "exit":
        print("Thanks for playing")
        break
    if userInput not in choices:
        print("invalid input, try again")
        continue

    com_input = random.choice(choices)

    if userInput == com_input:
        print("It's a tie")
    elif (userInput == "rock" and com_input == "scissors") or \
        (userInput == "scissors" and com_input == "paper") or \
        (userInput == "paper" and com_input == "rock"):
        print ("You win!!")
    else:
        print("You lost, computer wins")
    
    
