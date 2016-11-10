# Author: Scott Matthews
# Purpose: A console based game of Poker Dice 
# Requires: Python 3.5.2
# Notes: 

import random
from itertools import groupby

#these are the possible values of the dice
names = { 1: "9", 2: "10", 3: "J", 4: "Q", 5: "K", 6: "A"}

#these are the possible hands one can get
hands = { 1: 'High Card', 2: 'One Pair', 3: 'Two Pair', 4: 'Three of a Kind', 5: 'Full House', 6: 'Four of a Kind', 7: 'Five of a Kind', 8: 'Straight'}

player_score = 0
computer_score = 0

#Starts the game and loops through until game() returns false (when player opts out)
def start():
	print("Lets play a game of Poker Dice!")
	while game():
		pass
	scores()


def game():
	print("the computer will help you throw your five dice",end='\n\n')
	throws()
	return play_again()


def throws():
	#roll five dice, sort and print values to console
	dice_count = 5

	#computer turn to roll dice and show
	computer_dice = roll(dice_count)
	show('computer',computer_dice,dice_count)

	#player turn to roll dice and show
	player_dice = roll(dice_count)
	show('player',player_dice,dice_count)

	#prompt for user input on how many dice they wish to reroll
	while True:
		rerolls = input("How many dice do you want to throw again?")
		try:
			rerolls = int(rerolls)
			if rerolls in (0,1,2,3,4,5):
				break
		except ValueError:
			pass
		print("Oops! Please enter 1, 2, 3, 4 ,5 or 0")

	#If they opt for none then finish the game
	if rerolls == 0:
		pass
	else:
		#ask which dice they want to reroll
		dice_rerolls = roll(rerolls)
		dice_changes = list(range(rerolls))
		print("Enter dice number to reroll: ")
		
		#loop for the number of rerolls user selected
		iterations = 0
		while iterations < rerolls:
			iterations = iterations + 1
			while True:
				#prompt user to choose which dice to reroll and validate input
				selection = input("")
				selection = int(selection)
				try:
					if selection in (1,2,3,4,5):
						break
				except ValueError:
					pass
				print("Oops! Please enter 1, 2, 3, 4 or 5")
			dice_changes[iterations -1] = selection -1
			print("You have changed dice #", selection)
		
		#loop through for each roll and update dice with the dice_changes
		iterations = 0
		while iterations < rerolls:
			iterations = iterations + 1
			replacement = dice_rerolls[iterations - 1]
			player_dice[dice_changes[iterations -1]] = replacement

		show('player',player_dice,dice_count)

	#see who wins
	computer_hand = hand(computer_dice)
	player_hand = hand(player_dice)
	if computer_hand == player_hand:
		print("DRAW")
	elif player_hand < computer_hand:
		print("YOU LOSE")
		global computer_score
		computer_score = computer_score + 1
	else:
		print("YOU WIN")
		global player_score
		player_score = player_score + 1



#Returns a list of 5 random numbers between 1 & 6
def roll(dice_count):
	#represent six sided die
	numbers = range(1,7) 
	#create a list with 5 elements
	dice = list(range(dice_count)) 
	#iterate through and assign random number 1-6 to the dice list
	iterations = 0
	while iterations < dice_count:
		iterations = iterations + 1
		dice[iterations - 1] = random.choice(numbers)
	return dice

#Parses the dice numbers into poker hands
def hand(dice):
	# dice is already sorted, so we group by dice which groups numbers together
	# we make a list using the length of each group as the key, for every group in groupby...
	dice_hand = [len(list(group)) for key, group in groupby(dice)]
	dice_hand.sort(reverse=True)
	straight1 = [1,2,3,4,5]
	straight2 = [2,3,4,5,6]
	if dice == straight1 or dice == straight2:
		return 8
	elif dice_hand[0] == 5:
		return 7
	elif dice_hand[0] == 4:
		return 6
	elif dice_hand[0] == 3:
		if dice_hand[1] == 2:
			return 5
		else:
			return 4
	elif dice_hand[0] == 2:
		if dice_hand[1] == 2:
			return 3
		else:
			return 2
	else:
		return 1
	
	return dice_hand

def show(user,dice,dice_count):
	dice.sort()
	print(user," ",end='')
	for i in range(dice_count):
		print(names[dice[i]],end=' ')
	result = hand(dice)
	print("(",hands[result],")",sep='')
	print("")

#Ask the player if they would like another round
def play_again() :
	answer = input("Would you like to play again? [Y/N]: ")
	if answer in ("y","Y") :
		return True
	else :
		return False

#On finishing display the scores
def scores() :
	print("****SCORES****")
	print("You: ", player_score)
	print("Computer: ", computer_score)


start()