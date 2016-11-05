import random 
import time

player_score = 0
computer_score = 0

def start() :
	print("Let's play a game of hangman")
	while game() :
		pass
	scores()

def game() :
	#Pick a random word from a set of predefined
	dictionary = ["torture","garden","pizza","wine","pepper","abba","cheese"]
	word = random.choice(dictionary)
	
	#work out hoe many blanks to display and how many tries
	word_length = len(word)
	clue = word_length * ["_"]
	
	#set some initial variables
	tries = 6
	letters_tried = ""
	letters_right = 0
	letters_wrong = 0
	global computer_score,player_score

	hangedman(letters_wrong)
	print ((" ".join(clue)))
	
	#The two conditions to keep playing are running out of tries and getting the word
	while (letters_wrong != tries) and ("".join(clue) != word) :
		letter = guess_letter()
		#is the letter valid?
		if len(letter)==1 and letter.isalpha():
			#has the letter has already been picked (find returns -1 if letter present)
			if letters_tried.find(letter) !=-1 :
				print("You've already picked this letter!")
			#is the letter part of the word?
			else :
				letters_tried = letters_tried + letter
				first_index = word.find(letter)
				#is it correct?
				if first_index == -1 :
					letters_wrong += 1
					print("Incorrect!")
				else :
					print("Good guess, ", letter, " is correct!")
					for i in range(word_length) :
						if letter == word[i] :
							clue[i] = letter
		else :
			print("Choose another")

		#update the display
		hangedman(letters_wrong)
		print ((" ".join(clue)))
		print("Guesses: ", letters_wrong, "/", tries)
		#determine if player or computer has won
		if letters_wrong == tries :
			print("Game over!")
			print("The word was \"", word"\"")
			computer_score += 1
			break
		if "".join(clue) == word :
			print("You win!")
			player_score += 1
			break
	return play_again()

def guess_letter() :
	print()
	letter = input("Take a guess: ")
	#validate input
	letter.strip()
	letter.lower()
	print
	return letter

def hangedman(hangman) :
	graphic = [
		"""
		  +------+
		  |      |
		  |      
		  |     
		  |     
		  |
		==============
		""",
		"""
		  +------+
		  |      |
		  |      0
		  |     
		  |     
		  |
		==============
		""",
		"""
		  +------+
		  |      |
		  |      0
		  |      |
		  |     
		  |
		==============
		""",
		"""
		  +------+
		  |      |
		  |      0
		  |     /|
		  |     
		  |
		==============
		""",
		"""
		  +------+
		  |      |
		  |      0
		  |     /|\\
		  |     
		  |
		==============
		""",
		"""
		  +------+
		  |      |
		  |      0
		  |     /|\\
		  |     / 
		  |
		==============
		""",
		"""
		  +------+
		  |      |
		  |      0
		  |     /|\\
		  |     / \\
		  |
		==============
		"""
	]
	print(graphic[hangman])
	
def play_again() :
	answer = input("Would you like to play again? [Y/N]: ")
	if answer in ("y","Y") :
		return True
	else :
		return False

def scores() :
	print("You: ", player_score)
	print("Computer: ", computer_score)


start()