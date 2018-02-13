"""
An example of a top down 'camera' that follows a character across a larger map

For the camera to work we define are sprites (grass and player) with a starting x,y co, this is outside the loop
Everytime the D-Pad is pressed co for the player is updated. So the original location is changed (Not the x,y of the rct the player is draw onto!)

Every loop checks that the center of the player is not more that cameraslack pixels away from the center.
If it is then camerax/y is update to account for this.abs

The player RECT is redrwan always with x - camerax and y - cameray. this is becuase the player original x,y co is changing 
BUT its place on screen should not be when the camera is updated. this gives the effect of a camera since only when the player
is past cameraslack does the camerax/y value change and once it does the player rect stops moving sand all other sprites move instead
 
"""

import sys, pygame, random, os
from pygame.locals import *

FPS = 30
WINWIDTH = 640
WINHEIGHT = 480
HALF_WINWIDTH = WINWIDTH / 2
HALF_WINHEIGHT = WINHEIGHT / 2
MOVERATE = 8
CAMERASLACK = 90

#            R    G    B
GRASSCOLOR = (24, 255, 0)

def main():
    global FPSCLOCK, DISPLAYSURF, GRASSIMAGES

    pygame.init()
    FPSCLOCK = pygame.time.Clock() 
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Camera Example')

    #Load images
    PLAYERIMAGE = pygame.image.load(os.path.abspath('./squirrel.png'))
    GRASSIMAGES = []
    for i in range(1,5):
        GRASSIMAGES.append(pygame.image.load(os.path.abspath('./grass%s.png' % i)))

    #Initialize camera pos
    camerax = 0
    cameray = 0
    moveUp = False
    moveDown = False
    moveLeft = False
    moveRight = False

    #Define a player, here we just define enough information to draw the character later
    playerObj = {
        'image': PLAYERIMAGE,
        'x': WINWIDTH / 2,
        'y': WINHEIGHT / 2,
        'width': PLAYERIMAGE.get_width(),
        'height': PLAYERIMAGE.get_height()
    }

    #We do the same for grass object but store them in a list for tracking
    #Also we have used a function to create the objects as they will be created/destroyed often
    grassObjects = []
    for i in range(10):
        grassObjects.append(makeNewGrass(camerax, cameray))
        grassObjects[i]['x'] = random.randint(0, WINWIDTH)
        grassObjects[i]['y'] = random.randint(0, WINHEIGHT)

    #Enter loop
    while True:
        
        #Adjust camera
        playercenterx = playerObj['x'] + int(playerObj['width'] / 2)
        playercentery = playerObj['y'] + int(playerObj['height'] / 2)
        
        #if the player is more than cameraslack pixels away from the midpoint then...
        if (cameray + HALF_WINHEIGHT) - playercentery > CAMERASLACK:
            #update cameray which will update all other objects on screen
            cameray = playercentery + CAMERASLACK - HALF_WINHEIGHT
        elif playercentery - (cameray + HALF_WINHEIGHT) > CAMERASLACK:
            cameray = playercentery - CAMERASLACK - HALF_WINHEIGHT

        DISPLAYSURF.fill(GRASSCOLOR)

        #for each grassObject we create a Rect and blit the grass image onto it
        for gObj in grassObjects:
            gRect = pygame.Rect((
                gObj['x'] - camerax, #this keeps the grass pos updated as camera moves
                gObj['y'] - cameray,
                gObj['width'],
                gObj['height']
            ))

            DISPLAYSURF.blit(GRASSIMAGES[gObj['grassImage']], gRect)

        #Draw player
        #To draw we need to first create a surface upto date with camera pos then blit
        plRect = pygame.Rect((
            playerObj['x'] - camerax,
            playerObj['y'] - cameray,
            playerObj['width'],
            playerObj['height']
        ))
        DISPLAYSURF.blit(playerObj['image'], plRect)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #Movement
            #To get smooth movement we need to track Key UP and DOWN
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    moveDown = False
                    moveUp = True
                elif event.key == K_DOWN:
                    moveUp = False
                    moveDown = True

            elif event.type == KEYUP:
                if event.key == K_UP:
                    moveUp = False
                elif event.key == K_DOWN:
                    moveDown = False

        #Honour movement as decided above
        if moveUp:
            playerObj['y'] -= MOVERATE
        elif moveDown:
            playerObj['y'] += MOVERATE

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def getRandomOffCameraPos(camerax, cameray, objWidth, objHeight):
    cameraRect = pygame.Rect(camerax, cameray, WINWIDTH, WINHEIGHT)
    while True:
        x = random.randint(camerax - WINWIDTH, camerax + (2 * WINWIDTH))
        y = random.randint(cameray - WINHEIGHT, cameray + (2 * WINHEIGHT))
        objRect = pygame.Rect(x, y, objWidth, objHeight)
        if not objRect.colliderect(cameraRect):
            return x, y

def makeNewGrass(camerax, cameray):
    gr = {}
    gr['grassImage'] = random.randint(0, len(GRASSIMAGES) -1)
    gr['width'] = GRASSIMAGES[0].get_width()
    gr['height'] = GRASSIMAGES[0].get_height()
    gr['x'], gr['y'] = getRandomOffCameraPos(camerax, cameray, gr['width'], gr['height'])
    gr['rect'] = pygame.Rect(gr['x'], gr['y'], gr['width'], gr['height'])
    return gr

if __name__ == '__main__':
    main()