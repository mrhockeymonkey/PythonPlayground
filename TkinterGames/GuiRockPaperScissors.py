
#import tkinter and ttk which replaces some tkinter widgets with better versions
import tkinter
from tkinter import ttk
from tkinter import constants
import random

def gui():
	#Give each move and number for ease
	rock = 1
	paper = 2
	scissors = 3

	player_score = 0
	computer_score = 0

	#define text representation and rules, i.e. rock beats scissors
	names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
	rules = {rock: scissors, paper: rock, scissors: paper}

	#starts the game and invoke
	def start() :
		while game():
			pass

	#control the flow of the game
	def game() :
		player = player_choice.get()
		computer = random.randint(1,3)
		computer_choice.set(names[computer])
		result(player,computer)

	#compare player and computer choices to see who won
	def result(player,computer):
		if player == computer :
			result_set.set('Tie!')
		else:
			if rules[player] == computer:
				result_set.set('You win!')
				player_score.set(player_score.get() + 1)
			else:
				result_set.set('You lose!')
				computer_score.set(computer_score.get() + 1)

	rps_window = tkinter.Toplevel()
	rps_window.title ("Rock, Paper, Scissors")

	player_choice = tkinter.IntVar()
	computer_choice = tkinter.StringVar()
	result_set = tkinter.StringVar()
	player_choice.set(1)
	player_score = tkinter.IntVar(value=0)
	computer_score = tkinter.IntVar(value=0)

	rps_frame = ttk.Frame(rps_window, width = 3000)
	rps_frame.grid(column = 0, row = 0, sticky = constants.E)
	rps_frame.columnconfigure(0, weight = 1)
	rps_frame.rowconfigure(0, weight = 1)

	tkinter.Label(rps_frame, text = 'Player').grid(column = 1, row = 1, sticky = 'w')

	ttk.Radiobutton(rps_frame, text = 'Rock', variable = player_choice, value = 1).grid(column = 1, row = 2, sticky = 'w')
	ttk.Radiobutton(rps_frame, text = 'Paper', variable = player_choice, value = 2).grid(column = 1, row = 3, sticky = 'w')
	ttk.Radiobutton(rps_frame, text = 'Scissors', variable = player_choice, value = 3).grid(column = 1, row = 4, sticky = 'w')

	ttk.Label(rps_frame, text = 'Computer').grid(column = 3, row = 1, sticky = 'e')
	ttk.Label(rps_frame, textvariable = computer_choice).grid(column = 3, row = 3, sticky = 'e')
	ttk.Button(rps_frame, text = 'Play', command = start).grid(column = 2, row = 2, sticky = 'e')
	ttk.Label(rps_frame, text = 'Score').grid(column = 1, row = 5, sticky = 'e')
	ttk.Label(rps_frame, textvariable = player_score).grid(column = 1, row = 6, sticky = 'e')
	ttk.Label(rps_frame, text = 'Score').grid(column = 3, row = 5, sticky = 'e')
	ttk.Label(rps_frame, textvariable = computer_score).grid(column = 3, row = 6, sticky = 'e')
	ttk.Label(rps_frame, textvariable = result_set).grid(column = 2, row = 7, sticky = 'e')

#this allows it to be imported into a module but not run on import
if __name__ == '__main__' :
	gui()


