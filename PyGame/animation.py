import pygame
import sys
from pygame.locals import *

pygame.init()

#This clock is used to limit the number of frames rendered er second
# without a clock the game would run as fast as possible for that computer
FPS = 60 
fps_clock = pygame.time.Clock() 

DISP = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# this loads a new display surface with smiley.png drawn onto it
cat_image = pygame.image.load('smiley.png') 
catx = 10
caty = 10
direction = 'right'

while True:
    DISP.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    #blit is to copy a dislaysurface to DISP
    DISP.blit(cat_image, (catx, caty)) # Image, XY coordinate

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps_clock.tick(FPS)