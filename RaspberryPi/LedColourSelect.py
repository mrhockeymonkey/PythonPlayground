"""
This script prompts the user for a colour and then 
illuminates the specified LED
"""

#import RPi.GPIO as GPIO

# pin mapping
colours = {'red' : 7, 'yellow' : 13, 'green' : 15}

def prompt():
	# prompt the user to chose a colour
	print('Please select either', ', '.join(colours.keys()))
	user_input = input('Colour: ')
	return user_input
	


def illuminate(colour):
	# check colour is valid
	if (colour not in colours.keys()):
		raise Exception('Not a valid colour')
	
	# turn off all colours
	for c in colours.keys():
		print('OFF: ', colours[c])
		GPIO.output(colours[c], False)

	#turn on the selected colour
	print('ON: ', colours[colour])
	GPIO.output(colours[colour], True)

#RPi Setup
GPIO.setmode(GPIO.BOARD)
for p in colours.values():
	print("Setting up pin", p, "for output")
	GPIO.setup(p, GPIO.OUT)

while True:
	# prompt user for colour
	selected_colour = prompt()

	if(selected_colour == 'q'):
		break
	else:
		illuminate(selected_colour)

print('Quitting')
GPIO.cleanup()