# re-import our game variable
from gameComponents import gameVars

# define a win or lose function
def winorlose(status):
	
	if status == "won":
		print("   ")
		pre_message = "Today You have won, but some day the MACHINES will rule the world! "
	else:
		print("   ")
		pre_message = "A little step close to the global domain! MACHINES ARE BETTER THAN HUMANS!"

	print(pre_message)
	print("   ")
	print("▶ Would you like to play again Homo-Sapiens?")
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
