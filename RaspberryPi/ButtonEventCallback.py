"""
This script sets up pin 7 as an input with event detection and
callback action. This means everytime the button is pressed the callback
function is fired in another thread.
"""

import RPi.GPIO as GPIO
import time

def informpressed(pin):
	print('BUTTON PRESSED (', pin, ')')

# setup pin 7 as input with a default value of ON
pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# add a listener for edge event and a callback action to take in another thread
GPIO.add_event_detect(pin, GPIO.FALLING)
GPIO.add_event_callback(pin, callback=informpressed, bouncetime=200)

while True:
	print('...')
	time.sleep(0.3)