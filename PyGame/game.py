import pygame, sys
from pygame.locals import *

RED = pygame.color(255,0,0) #colour is represent as a Tuple (Red,Green,Blue,Alpha)
BLUE = (0,0,255)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World')

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		pygame.display.update()

#Page 18