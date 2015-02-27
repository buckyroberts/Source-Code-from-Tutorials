import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(blue)

Pix = pygame.PixelArray(gameDisplay)

Pix[10][10] = green

pygame.draw.line(gameDisplay, red, (200,300), (500,500),5)
pygame.draw.circle(gameDisplay, red, (200,200), 100)

pygame.draw.rect(gameDisplay, green,(150,150,200,100))
pygame.draw.polygon(gameDisplay, white, ((140,5),(200,16),(88,333),(600,222),(555,222)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()



