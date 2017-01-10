import tkinter
from tkinter import ttk
from tkinter import constants
import random 

def gui():
	word = 0
	word_length = 0
	clue = 0
	dictionary = ["torture","garden","pizza","wine","pepper","abba","cheese"]
	word = random.choice(dictionary)
	word_length = len(word)
	clue = word_length * ["_"]
	tries = 6

	#generate and set the hangman graphic on screen
	def hangedman(hangman) :
		graphic = [
"""
  +------+
  |      |
  |      
  |     
  |     
  |
============
""",
"""
  +------+
  |      |
  |      0
  |     
  |     
  |
============
""",
"""
  +------+
  |      |
  |      0
  |      |
  |     
  |
============
""",
"""
  +------+
  |      |
  |      0
  |     /|
  |     
  |
============
""",
"""
  +------+
  |      |
  |      0
  |     /|\\
  |     
  |
============
""",
"""
  +------+
  |      |
  |      0
  |     /|\\
  |     / 
  |
============
""",
"""
  +------+
  |      |
  |      0
  |     /|\\
  |     / \\
  |
============
"""
		]
		hm_graphic.set(graphic[hangman])

	def game() :
		#set some initial variables
		letters_wrong = incorrect_guesses.get()
		letter = guess_letter()
		first_index = word.find(letter)
		if first_index == -1 :
			letters_wrong += 1
			incorrect_guesses.set(letters_wrong)
		else :
			for i in range(word_length) :
				if letter == word[i] :
					clue[i] = letter

		hangedman(letters_wrong)
		clue_set = " ".join(clue)
		word_output.set(clue_set)

		if letters_wrong == tries :
			result_text = "Game over!"
			result_set.set(result_text)
			computer_score.set(computer_score.get() + 1)

		if "".join(clue) == word :
			result_text = "You win!"
			result_set.set(result_text)
			player_score.set(player_score.get() +1)

	def guess_letter() :
		letter = letter_guess.get()
		#validate input
		letter.strip()
		letter.lower()
		return letter

	def reset_game():
		incorrect_guesses.set(0)
		hangedman(0)
		result_set.set("")
		letter_guess.set("")
		word = random.choice(dictionary)
		word_length = len(word)
		clue = word_length * ["_"]
		new_clue = " ".join(clue)
		word_output.set(new_clue)

	#instatiate the variables we will need
	incorrect_guesses = tkinter.IntVar()
	player_score = tkinter.IntVar()
	computer_score = tkinter.IntVar()
	result_set = tkinter.StringVar()
	letter_guess = tkinter.StringVar()
	word_output = tkinter.StringVar()
	hm_graphic = tkinter.StringVar()

	reset_game()

	#define & configure the window, here we make a 0x0 grid that will expands
	hm_window = tkinter.Toplevel()
	hm_window.title ("Hangman")
	hm_window.columnconfigure(0, weight = 1)
	hm_window.rowconfigure(0, weight = 1)

	#define & configure the frame, here we make a 3x3 grid that expands
	hm_frame = ttk.Frame(hm_window)
	hm_frame.grid(column = 0, row = 0, sticky = constants.NSEW)
	hm_frame.columnconfigure(0, weight = 1)
	hm_frame.columnconfigure(1, weight = 1)
	hm_frame.columnconfigure(2, weight = 1)
	hm_frame.rowconfigure(0, weight = 1)
	hm_frame.rowconfigure(1, weight = 1)
	hm_frame.rowconfigure(2, weight = 1)

	#place the hangman graphic in the first row spanning three columns
	ttk.Label(hm_frame, textvariable = hm_graphic ).grid(column = 0, columnspan = 3, row = 0)
	
	#place the clue in the second row spanning three columns with padding
	ttk.Label(hm_frame, textvariable = word_output).grid(column = 0, columnspan = 3, row = 1, pady = 20)

	#place a label and text entry box in the next row spanning three columns
	ttk.Label(hm_frame, text = "Enter a letter").grid(column = 0, columnspan = 3, row = 2)
	ttk.Entry(hm_frame, exportselection = 0, textvariable = letter_guess).grid(column = 0, columnspan = 3, row = 3)
	ttk.Button(hm_frame, text = "Guess", command = game).grid(column = 0, columnspan = 3, row = 4, pady= 20)

	ttk.Label(hm_frame, text = "Wins").grid(column = 0, row = 5)
	ttk.Label(hm_frame, textvariable = player_score).grid(column = 0, row = 6)
	ttk.Label(hm_frame, text = "Losses").grid(column = 2, row = 5)
	ttk.Label(hm_frame, textvariable = computer_score).grid(column = 2, row = 6)
	ttk.Label(hm_frame, textvariable = result_set).grid(column = 1, row = 7)

	ttk.Button(hm_frame, text = "Replay", command = reset_game).grid(column = 0, columnspan = 3, row = 8, pady = 20)

if __name__ == '__main__':
	gui()





