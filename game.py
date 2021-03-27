# Import a packages to extend Python (just like we extend Sublime, Atom, or VSCode)
from random import randint

# re-import our game variables
from gameComponents import gameVars, winLose, rpsCompare

# player_choice == False
while gameVars.player_choice is False:
	print("   ")
	print("-------/* Rock, Paper, Scissors GAME */-------")
	print("             Humans /VS/ Machines             ")
	print("              /▲/          /■/                ")

	print("   ")
	print("▲ Human Lives ♥: ", gameVars.player_lives, "/", gameVars.total_lives)
	print("■ Machine Lives ♥: ", gameVars.computer_lives, "/", gameVars.total_lives)
	print("   ")
	print("------------/·☆·/------------/·☆·/------------")
	print("   ")

	print("Choose your DESTINY! Or DIE!")
	print("Type QUIT to exit.")
	print("   ")

	gameVars.player_choice = input("Choose rock, paper, or scissors: ")
	#player_choice now equals TRUE ->it has a value

	if gameVars.player_choice == "quit":
		print("   ")
		print("··· Little piece of chicken, you chose to QUIT ··· SEE YOU NEXT TIME! ···")
		print("   ")
		exit()

	gameVars.computer_choice = gameVars.choices[randint(0, 2)]

	print("   ")
	print("▲ Your Human choice: " + gameVars.player_choice)
	print("■ My artificial intelligence choose: " + gameVars.computer_choice)
	print("   ")

	rpsCompare.wonchoice()

	# Step 6: life counter goes to 0
	if gameVars.player_lives == 0:
		winLose.winorlose("lose")
		
	if gameVars.computer_lives == 0:
		winLose.winorlose("won")
		
	# Step 5: life counter message
	print("   ")
	print("Your human lives ♥: ", gameVars.player_lives)
	print("My machine lives ♥: ", gameVars.computer_lives)
	print("==============================================")

	# map the loop keep running, by setting player_choice back to False
	# unset, so that ourloop condition will evaluate to True
	gameVars.player_choice = False