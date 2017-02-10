"""
This script will stop execution and wait 5 seconds for an input. 

This could be useful if expecting a known input in a linear manner
"""

import RPi.GPIO as GPIO

# setup pin 7 as input with a default value of ON
pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# stop execution until
print("Press the button")
edge = GPIO.wait_for_edge(pin, GPIO.FALLING, timeout = 5000)

if edge is None:
	print('Timeout occurred')
else:
	print('Edge detected on', pin)