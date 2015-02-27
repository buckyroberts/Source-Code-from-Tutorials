import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('3d')

white = (255,255,255)
black = (0,0,0)

red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

FPS = 30


def cube(startPoint, fullSize):
    node_1 = [startPoint[0], startPoint[1]]
    node_2 = [startPoint[0]+fullSize, startPoint[1]]
    node_3 = [startPoint[0], startPoint[1]+fullSize]
    node_4 = [startPoint[0]+fullSize, startPoint[1]+fullSize]

    offset = int(fullSize / 2)

    x_mid = int(display_width / 2)
    x_offset = -1* int(startPoint[0]-x_mid)
    print(x_offset)
    if x_offset < -100:
        x_offset = -100
    elif x_offset > 100:
        x_offset = 100
    node_5 = [node_1[0]+x_offset, node_1[1]-offset]
    node_6 = [node_2[0]+x_offset, node_2[1]-offset]
    node_7 = [node_3[0]+x_offset, node_3[1]-offset]
    node_8 = [node_4[0]+x_offset, node_4[1]-offset]
    

    # top line #
    pygame.draw.line(gameDisplay, white, (node_1),(node_2))
    # bottom line #
    pygame.draw.line(gameDisplay, white, (node_3),(node_4))
    # left line #
    pygame.draw.line(gameDisplay, white, (node_1),(node_3))
    # right line #
    pygame.draw.line(gameDisplay, white, (node_2),(node_4))

    # top line #
    pygame.draw.line(gameDisplay, white, (node_5),(node_6))
    # bottom line #
    pygame.draw.line(gameDisplay, white, (node_7),(node_8))
    # left line #
    pygame.draw.line(gameDisplay, white, (node_5),(node_7))
    # right line #
    pygame.draw.line(gameDisplay, white, (node_6),(node_8))


    pygame.draw.circle(gameDisplay, light_green, node_1, 5)
    pygame.draw.circle(gameDisplay, light_green, node_2, 5)
    pygame.draw.circle(gameDisplay, light_green, node_3, 5)
    pygame.draw.circle(gameDisplay, light_green, node_4, 5)

    pygame.draw.circle(gameDisplay, light_green, node_5, 5)
    pygame.draw.circle(gameDisplay, light_green, node_6, 5)
    pygame.draw.circle(gameDisplay, light_green, node_7, 5)
    pygame.draw.circle(gameDisplay, light_green, node_8, 5)


    pygame.draw.line(gameDisplay, white, (node_1),(node_5))

    pygame.draw.line(gameDisplay, white, (node_2),(node_6))
 
    pygame.draw.line(gameDisplay, white, (node_3),(node_7))

    pygame.draw.line(gameDisplay, white, (node_4),(node_8))

    


    
    


def gameLoop():

    location = [300,200]
    size = 100

    current_move = 0

    z_move = 0
    z_location = 50

    y_move = 0

    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_move = -5
                    
                elif event.key == pygame.K_RIGHT:
                    current_move = 5


                    
                elif event.key == pygame.K_UP:
                    y_move = -5
                elif event.key == pygame.K_DOWN:
                    y_move = 5
                    

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    current_move = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0
                    #current_move = 0

        gameDisplay.fill(black)

        if z_location > 200:
            z_move = 0

        z_location += z_move

        current_size = size

        location[0] += current_move
        location[1] += y_move

        cube(location, current_size)
        pygame.display.update()
        
        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()
