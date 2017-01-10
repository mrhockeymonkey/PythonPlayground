
import random
import tkinter
from tkinter import ttk
from tkinter import constants
from itertools import groupby

def gui():

	#function to pick a card graphic based on the dice value
	def card(dice_value):
		cards = [
"""
|9    |
|      |
|    9|
""",
"""
|10   |
|       |
|   10|
""",
"""
|J     |
|      |
|     J|
""",
"""
|Q    |
|       |
|    Q|
""",
"""
|K    |
|      |
|    K|
""",
"""
|A    |
|       |
|    A|
""",
"""
|       |
|       |
|       |
"""
		]
		return cards[dice_value]

	def roll(dice_count):
		#represent six sided die
		numbers = range(0,6) 
		#create a list the number of elements as dice rolled.
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
		
		#if the dice match one of the two conditions for straight
		if dice == straight1 or dice == straight2:
			return "A Straight!"
		#if the largest grouping of dice valus is five
		elif dice_hand[0] == 5:
			return "Five of a Kind!"
		#if the largest grouping of dice valus is four
		elif dice_hand[0] == 4:
			return "Four of a Kind!"
		#if the largest grouping of dice valus is three
		elif dice_hand[0] == 3:
			#if player has a group of 3 and of 2 this is a full house
			if dice_hand[1] == 2:
				return "Full House!"
			else:
				#if not then they only got three the same
				return "Three of a Kind!"
		#if the largest grouping of dice values is 2
		elif dice_hand[0] == 2:
			#and the second grouping was also a 2
			if dice_hand[1] == 2:
				return "Two Pair!"
			#if not 
			else:
				return "One Pair!"
		else:
			return "High Card!"
		

	def start():
		computer_dice = roll(5)
		computer_dice.sort()
		computer_hand.set(hand(computer_dice))
		computer_dice.sort(reverse = True)
		
		player_dice = roll(5)
		player_dice.sort()
		player_hand.set(hand(player_dice))
		player_dice.sort(reverse = True)

		i = 0
		for cd in computer_dice:
			computer_dice[i] = card(cd)
			i = i + 1

		i = 0
		for pd in player_dice:
			player_dice[i] = card(pd)
			i = i + 1

		computer_cards.set(" ".join(computer_dice))
		player_cards.set(" ".join(player_dice))


	#define the tkinter variables we will use
	computer_cards = tkinter.StringVar()
	computer_hand = tkinter.StringVar()
	player_cards = tkinter.StringVar()
	player_hand = tkinter.StringVar()

	#define and configure the window
	pd_window = tkinter.Toplevel()
	pd_window.title("Poker Dice")
	pd_window.columnconfigure(0, weight = 1, minsize = 600)
	pd_window.rowconfigure(0, weight = 1, minsize = 300)

	#define and configure the frame
	pd_frame = ttk.Frame(pd_window)
	pd_frame.grid(column = 0, row =0, sticky = constants.NSEW)
	for c in range(2):
		pd_frame.columnconfigure(c, weight = 1)
	for r in range (4):
		pd_frame.rowconfigure(r, weight = 1)

	#the computer section
	ttk.Label(pd_frame, text = "Computer").grid(column = 0, row = 0)
	ttk.Label(pd_frame, textvariable = computer_cards).grid(column = 0, row = 1)
	ttk.Label(pd_frame, textvariable = computer_hand).grid(column = 0, row = 2)

	#the player section
	ttk.Label(pd_frame, text = "Player").grid(column = 1, row = 0)
	ttk.Label(pd_frame, textvariable = player_cards).grid(column = 1, row = 1)
	ttk.Label(pd_frame, textvariable = player_hand).grid(column = 1, row = 2)

	ttk.Button(pd_frame, text = "Play", command = start).grid(column = 0, columnspan = 2, row = 3)
	
	computer_cards.set(" ".join([card(6),card(6),card(6),card(6),card(6)]))
	player_cards.set(" ".join([card(6),card(6),card(6),card(6),card(6)]))

if __name__ == '__main__':
	gui()