"""
This script will blink a single LED connected to GPIO pin 7
ten times and then exit
"""

import RPi.GPIO as GPIO
import time

# function to blink led with interval 1 second
def blink(pin):
	GPIO.output(pin, True)
	time.sleep(1)
	GPIO.output(pin, False)
	time.sleep(1)

# use the board pin numbering to refer to pins
GPIO.setmode(GPIO.BOARD)

# declare pin 7 to be used for output
GPIO.setup(7, GPIO.OUT)

# blink the led 10 times
for i in range(0,10):
	blink(7)