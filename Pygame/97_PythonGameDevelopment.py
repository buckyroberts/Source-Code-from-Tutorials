import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )



def Draw_Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    
    #
    gluPerspective(45.0, (display[0]/display[1]), 0.1, 50)

    # moving back. 
    glTranslatef(0.0,0.0,-5.0)

    # where we might be
    glRotatef(40, 20, 20, 0)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                print(event.button)


        glRotatef(1, 3, 1, 1) 
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Draw_Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()

            
    




























