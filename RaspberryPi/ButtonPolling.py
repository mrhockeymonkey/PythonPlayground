import RPi.GPIO as GPIO
import time

#Setup pin 7 as input with a default value of OFF
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	if(GPIO.input(7)):
		print('Button is pressed')
	else:
		print('Button is not pressed')
	
	time.sleep(1)