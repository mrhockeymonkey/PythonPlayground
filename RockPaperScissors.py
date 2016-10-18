import random
import time

#Give each move and number for ease
rock = 1
paper = 2
scissors = 3

#define text representation and rules, i.e. rock beats scissors
names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

#initialize scores
player_score = 0
computer_score = 0

#starts the game and invoke score() when game() finishes
def start() :
	while game():
		pass
	scores()

#control the flow of the game
def game() :
	player = move()
	computer = random.randint(1,3)
	result(player,computer)
	return play_again()

#prompt user for respionse to play again or stop
def play_again():
	while True : 
		answer = input("Would you like to play again? y/n: ")
		if answer == "y" :
			return True
		elif answer == "n" :
			print("\nThank you for playing!")
			return False
		else :
			print("Please only enter either y or n")

#prompt the user to enter 1,2 or 3 as input
def move() :
	while True :
		player_move = input("\n1 = Rock\n2 = Paper\n3 = Scissors\n\nMake a move: ")
		try :
			player_move = int(player_move)
			if player_move in (1,2,3) :
				return player_move
		except ValueError:
			pass
		print("Please only enter either 1, 2 or 3")

#compare player and computer choices to see who won
def result(player,computer):
	print("\n1...",end='',)
	time.sleep(1)
	print("2...",end='')
	time.sleep(1)
	print("3...")
	time.sleep(0.5)
	print("{0} Vs {1}".format(names[player],names[computer]))
	if player == computer :
		print("Tie!\n")
	elif rules[player] == computer : # eg rules[1] = scissor, i.e. rock beats scissors
		print("You win!\n")
		global player_score
		player_score += 1
	elif rules[computer] == player :
		print("You lose!\n")
		global computer_score
		computer_score += 1

#show the scores 
def scores() :
	print("Player: ",player_score)
	print("Computer: ",computer_score)

#this allows it to be imported into a module but not run on import
if __name__ == '__main__' :
	start()


