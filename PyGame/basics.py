import pygame, sys
from pygame.locals import *

# colous can be represented in two ways
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = pygame.Color(255,0,0) #colour is represent as a Tuple (Red,Green,Blue,Alpha)
GREEN = pygame.Color(0,255,0)
BLUE = pygame.Color(0,0,255)


pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300)) #this is the area the user will see 
pygame.display.set_caption('Hello World')

DISPLAYSURF.fill(WHITE) 
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)), 20) #surf, color, list of points, width
pygame.draw.line(DISPLAYSURF, BLUE, (30,30),(60,60), 7) #surf, colour, start, end, width
#Can use aaline for anti-aliased lines.

pygame.draw.circle(DISPLAYSURF, BLACK, (200,200), 40) #surf, color, center, radius, width
pygame.draw.rect(DISPLAYSURF, RED, (50, 50, 100, 50)) #suf, color, rect/tuple, width

pixel_array = pygame.PixelArray(DISPLAYSURF)
pixel_array[200][250] = BLACK
del pixel_array #you mustdelete the pixel array obj

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		pygame.display.update()

