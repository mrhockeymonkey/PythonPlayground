import RPi.GPIO as GPIO
import time

#Setup pin 7 as input with a default value of ON
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	# if the button is pressed, the circuit connected, then pin 7 will beocme LOW
	if(GPIO.input(7)) == False:
		print('Button is pressed')
	elif == True:
		print('Button is not pressed')
	
	time.sleep(0.5)