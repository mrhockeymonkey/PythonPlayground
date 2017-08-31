import pygame, sys, time
from pygame.locals import *

pygame.init()
DISP = pygame.display.set_mode((400,300))
pygame.display.set_caption('fonts')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

font_object = pygame.font.Font('freesansbold.ttf', 32) #font name, size
text_surface = font_object.render('Hello World!', True, GREEN, BLUE) #text, anti-alias, Fore, Back
text_rect = text_surface.get_rect()
text_rect.center = (200, 150)

while True:
    DISP.fill(WHITE)
    DISP.blit(text_surface, text_rect) #image, XY coordinate
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()