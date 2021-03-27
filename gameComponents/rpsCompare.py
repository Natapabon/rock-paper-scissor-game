# re-import our game variable
from gameComponents import gameVars

# the comparative function between the choices machine vs human
def wonchoice():

	if gameVars.computer_choice == gameVars.player_choice:
			print("               ··· TIE···                 ")
			print(" ··· Lets see how far your luck lasts. ···")

	elif gameVars.computer_choice == "rock":
		if gameVars.player_choice == "scissors":
			print("         ··· ■ YOU LOSE ■ ···        ")
			print(" ··· Close to die, piece of meat. ···")
			gameVars.player_lives -= 1

		else:
			print("           ··· ▲ YOU WON ▲ ···           ")
			print(" ··· You only delayed the inevitable! ···")
			gameVars.computer_lives -= 1


	elif gameVars.computer_choice == "paper":
		if gameVars.player_choice == "rock":
			print("          ··· ■ YOU LOSE ■ ···         ")
			print(" ··· Technology over biology, LOSER!···")
			gameVars.player_lives -= 1
			
		else:
			print("                ··· ▲ YOU WON ▲ ···                ")
			print(" ··· That does not cut my dominance intentions. ···")
			gameVars.computer_lives -= 1


	elif gameVars.computer_choice == "scissors":
		if gameVars.player_choice == "paper":
			print("                     ··· ■ YOU LOSE ■ ···                    ")
			print(" ··· I will be kind to you when we rule the planet, LOSER!···")
			gameVars.player_lives -= 1
			
		else:
			print("                ··· ▲ YOU WON ▲ ···                ")
			print(" ··· Despite defeat, the Machines keep rocking! ···")
			gameVars.computer_lives -= 1
