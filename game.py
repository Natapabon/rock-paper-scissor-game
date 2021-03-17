# Import a packages to extend Python (just like we extend Sublime, Atom, or VSCode)
from random import randint

# [] => this is an array
# name = [value1,value2, value3]

# step one
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contents are assigned a number) the index always starts at 0
choices = ["rock", "paper", "scissors"]

# Version 1, to explain array indexing
# player_choice = choices[1]
# print("index 1 in the choice array is " + player_choice + ", which is paper")

player_choice = input("Choose rock, paper, or scissors: ")

print("user chose " + player_choice)

# step 2
# this will be the AI Choise -> a random pick from the choices array
computer_choice = choices[randint(0, 2)]

print("computer_choice: " + computer_choice)

# step 3

if computer_choice == player_choice:
	print("tie")

elif computer_choice == "rock":
	if player_choice == "scissors":
		print("You lose!")
	else:
		print("You win!")


elif computer_choice == "paper":
	if player_choice == "rock":
		print("You lose!")
	else:
		print("You win!")


elif computer_choice == "scissors":
	if player_choice == "paper":
		print("You lose!")
	else:
		print("You win!")


