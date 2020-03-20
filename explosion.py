import pygame
from pygame.locals import *

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('')

tour_image = pygame.image.load("explosion.png")

explosion = []                                          # definit une liste vide
      # definition d'une image de 64 par 64 pixels
#image = pygame.Surface((64,64))

i=0

for y in range (0,320,64):                              # parcour  la largeur de limage source par pas de 64
    for x in range (0,320,64):                          # parcour  la hauteur de limage source par pas de 64
        image = pygame.Surface((64,64), pygame.SRCALPHA)
        for yy in range (0,64):                         # parcour  la largeur de limage destination
            for xx in range (0,64):                     # parcour  la hauteur de limage destination
                c = tour_image.get_at((xx+x, yy+y))     # Recupere la couleur du pixel dans limage source
                image.set_at((xx,yy),c)                 # affecte la couleur à limage destination
        image=pygame.transform.scale(image,(15,15))
        explosion.append(image)
        print("decoupe",i)
        i+=1
print("fin de decoupe")




clock = pygame.time.Clock()

fin = False
i=0
while not fin:
    gameDisplay.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            fin = True
        elif event.type == MOUSEBUTTONDOWN:
            i+=1
            print(i)
            if (i>24):
                i=0

        #print(event)


    clock.tick(60)

    #gameDisplay.blit(tour_image,(10,10))


    gameDisplay.blit(explosion[i],(0,0))


    pygame.display.update()
pygame.quit()
quit()
