"""
Demonstrating how to use maps
"""

import pytmx, os, pygame, sys
from pytmx import load_pygame
from pygame.locals import *

FPS = 30
WINWIDTH = 320
WINHEIGHT = 320

def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    CLOCK = pygame.time.Clock()

    #Load map
    gameMap = pytmx.load_pygame(os.path.abspath("./assets/map1.tmx"))

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for layer in gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = gameMap.get_tile_image_by_gid(gid)
                DISPLAY.blit(tile, (x * gameMap.tilewidth, y * gameMap.tileheight))

        pygame.display.update()
        CLOCK.tick(FPS)



if __name__ == '__main__':
    main()