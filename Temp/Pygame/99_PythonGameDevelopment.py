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

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)    
    )




def Draw_Cube():

    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv((0,1,1))
            glVertex3fv(verticies[vertex])
    
    glEnd()


    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((0,0,0))
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    
    #
    gluPerspective(90.0, (display[0]/display[1]), 0.1, 50)

    # moving back. 
    glTranslatef(0.0,0.0,-5.0)

    # where we might be
    glRotatef(20, 2, 0, 0)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                print(event.button)

                if event.button == 4:
                    glTranslatef(0.0,0.0,1.0)
                elif event.button == 5:
                    glTranslatef(0.0,0.0,-1.0)

                    


        glRotatef(1, 3, 1, 1) 
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Draw_Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()

            
    




























