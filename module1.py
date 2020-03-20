import pygame
from pygame.locals import *

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('')

clock = pygame.time.Clock()

fin = False

while not fin:

    for event in pygame.event.get():
        if event.type == QUIT:
            fin = True
        elif event.type == KEYDOWN and event.key == K_t:
           print("t")

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
