# Import a packages to extend Python (just like we extend Sublime, Atom, or VSCode)
from random import randint

# [] => this is an array
# name = [value1,value2, value3]

# step one
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contents are assigned a number) the index always starts at 0
choices = ["rock", "paper", "scissors"]


# lifes check infor for step 4
player_lives = 3
computer_lives = 3
total_lives = 3

# Step 5.5: looping life counter until 0
#True or False are boolean data types
# essentially, booleans are equivalent to an on or off switch, 1 or 0.
player_choice = False

# define a win or lose function
def winorlose(status):
	# version 1 of function
	# print("Inside winorlose function; sattus is: ", status)
	
	print("You ", status, ", Would you like to play again?")
	choice = input("Y/N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit. See you next time. BYE!")
		exit()

	elif choice == "Y" or choice == "y":
		# reset the player lives and computer lives
		# and reset player choice to False, so our loop restarts
		global player_lives
		global computer_lives
		global total_lives

		player_lives = total_lives
		computer_lives = total_lives

	else:
		print("Make a valid choice - Y or N")
		# this might generate a bug tht we need to fix later
		choice = input("Y/N? ")

# player_choice == False
while player_choice is False:
	print("==========/* RPS GAME */==========")
	print("Player Lives: ", player_lives, "/", total_lives)
	print("Computer Lives: ", computer_lives, "/", total_lives)
	print("==================================")

	# Version 1, to explain array indexing
	# player_choice = choices[1]
	# print("index 1 in the choice array is " + player_choice + ", which is paper")

	print("Choose your weapon! Or type quit to exit")

	player_choice = input("Choose rock, paper, or scissors: ")
	#player_choice now equals TRUE ->it has a value

	if player_choice == "quit":
		print("You chose to quit. You can play in other opportunity!")
		exit()

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
			#step 4 
			#verbose way
			# player_lives = player_lives - 1
			#simplified way
			player_lives -= 1
		else:
			print("You win!")
			computer_lives -= 1


	elif computer_choice == "paper":
		if player_choice == "rock":
			print("You lose!")
			player_lives -= 1
		else:
			print("You win!")
			computer_lives -= 1


	elif computer_choice == "scissors":
		if player_choice == "paper":
			print("You lose!")
			player_lives -= 1
		else:
			print("You win!")
			computer_lives -= 1

	# Step 6: life counter goes to 0
	if player_lives == 0:
		winorlose("lose")
		
	if computer_lives == 0:
		winorlose("won")
		
	# Step 5: life counter message
	print("Player lives: ", player_lives)
	print("Computer lives: ", computer_lives)

	# map the loop keep running, by setting player_choice back to False
	# unset, so that ourloop condition will evaluate to True
	player_choice = False
