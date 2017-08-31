import pygame, sys, time, os
from pygame.locals import *

pygame.init()
DISP = pygame.display.set_mode((400,300))
pygame.display.set_caption('sound') 

#to play background music (only one song can be played atv a time)
music_object = pygame.mixer.music.load(os.path.abspath('./assets/tetrisb.mid')) #WAV/MP3/MIDI
pygame.mixer.music.play(-1, 0.0) #number of loops (-1 keeps looping), starting point (seconds)


#To play a sound you create an object for that sound in th emixer
sound_object = pygame.mixer.Sound(os.path.abspath('./assets/beep2.ogg')) #WAV/MP3/OGG
sound_object.play()
time.sleep(1)
sound_object.stop()