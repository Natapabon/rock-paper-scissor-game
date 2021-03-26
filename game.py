# Import a packages to extend Python (just like we extend Sublime, Atom, or VSCode)
from random import randint

# re-import our game variables
from gameComponents import gameVars

# define a win or lose function
def winorlose(status):
	
	if status == "won":
		pre_message = "Today You have won, but some day the MACHINES will rule the world"
	else:
		pre_message = "A little step close to the global domain! Machines are better than Humans, LOSER!"

	print(pre_message + "Would you like to play again Homo-Sapiens?")
	choice = False
	
	while choice == False:
		choice = input("Y/N? ")

		if choice == "Y" or choice == "y":
			# reset the player lives and computer lives
			gameVars.player_lives = gameVars.total_lives
			gameVars.computer_lives = gameVars.total_lives

		elif choice == "N" or choice == "n":
			print("   ")
			print("··· Disappointing choice ··· HASTA LA VISTA BABY! ···")
			print("   ")
			exit()

		else:
			print("Make a valid choice - Y or N")
			choice = False

# player_choice == False
while gameVars.player_choice is False:
	print("-------/* Rock, Paper, Scissors GAME */-------")
	print("             Humans /VS/ Machines             ")
	print("   ")
	print("Human Lives: ", gameVars.player_lives, "/", gameVars.total_lives)
	print("Machine Lives: ", gameVars.computer_lives, "/", gameVars.total_lives)
	print("   ")
	print("------------/···/------------/···/------------")
	print("   ")

	print("Choose your DESTINY! Or DIE!")
	print("Type QUIT to exit.")
	print("   ")

	gameVars.player_choice = input("Choose rock, paper, or scissors: ")
	#player_choice now equals TRUE ->it has a value

	if gameVars.player_choice == "quit":
		print("   ")
		print("··· Little chicken you chose to QUIT ··· HASTA LA VISTA BABY! ···")
		print("   ")
		exit()

	gameVars.computer_choice = gameVars.choices[randint(0, 2)]

	print("   ")
	print("* Human chose: " + gameVars.player_choice)
	print("* Machine chose: " + gameVars.computer_choice)
	print("   ")

	if gameVars.computer_choice == gameVars.player_choice:
		print("               ··· TIE···                 ")
		print(" ··· Lets see how far your luck lasts. ···")

	elif gameVars.computer_choice == "rock":
		if gameVars.player_choice == "scissors":
			print(" ··· Close to die, piece of meat. ···")
			gameVars.player_lives -= 1

		else:
			print("              ··· YOU WON ···            ")
			print(" ··· You only delayed the inevitable! ···")
			gameVars.computer_lives -= 1


	elif gameVars.computer_choice == "paper":
		if gameVars.player_choice == "rock":
			print(" ··· Technology over biology, LOSER!···")
			gameVars.player_lives -= 1
		
		else:
			print("                   ··· YOU WON ···                 ")
			print(" ··· That does not cut my dominance intentions. ···")
			gameVars.computer_lives -= 1


	elif gameVars.computer_choice == "scissors":
		if gameVars.player_choice == "paper":
			print(" ··· I will be kind to you when we rule the planet, LOSER!···")
			gameVars.player_lives -= 1
		
		else:
			print("                  ··· YOU WON ···                 ")
			print(" ··· Despite defeat, the Machines keep rocking! ···")
			gameVars.computer_lives -= 1

	# Step 6: life counter goes to 0
	if gameVars.player_lives == 0:
		winorlose("lose")
		
	if gameVars.computer_lives == 0:
		winorlose("won")
		
	# Step 5: life counter message
	print("   ")
	print("Your human lives: ", gameVars.player_lives)
	print("My machine lives: ", gameVars.computer_lives)
	print("==============================================")

	# map the loop keep running, by setting player_choice back to False
	# unset, so that ourloop condition will evaluate to True
	gameVars.player_choice = False