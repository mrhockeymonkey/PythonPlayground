"""
This script will check for events every 3 seconds
Even though the gap is longer than in ButtonPolling.py, becuase we
are using events we should not see any inputs missed

This is good that we dont miss inputs but capturing an event only occurs
once, so multiple button presses within 3 seconds are not picked up
"""

import RPi.GPIO as GPIO
import time

# setup pin 7 as input with a default value of ON
pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# create a new listener for events (Events are RISING or FALLING or BOTH)
GPIO.add_event_detect(pin, GPIO.FALLING)

while True:
	if (GPIO.event_detected(pin)):
		print('Button pressed')

	time.sleep(3)