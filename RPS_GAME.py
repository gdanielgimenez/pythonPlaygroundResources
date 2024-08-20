# simple rock paper scissors game implementing use of dictionary for key value pairs for player and computer choices
# random for selecting the computer choice between rock paper scissors from a list options
# using if elif conditionals for checking the result of the game either draw or win lose
# input so the player can type either of the 3 options "rock paper scissors"
# function get_choices that we call to put everything in motion
import random


def get_choices():
    player_choice = input("enter a choice (rock paper scissors)  \n:")
    options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}

    if player_choice == computer_choice:
        print("is a draw! thanks for playing!")
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win! paper beats rock!")
        else:
            print("You lose! :(  scissors beats paper!")
    elif player_choice == "rock":
        if computer_choice == "paper":
            print("You lose! :( paper beats rock!")
        else:
            print("You win! rock beats scissors!")
    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("You lose! :( rock beats scissors!")
        else:
            print("You win! scissors beats paper!")
    return choices


choices = get_choices()
print(choices)
