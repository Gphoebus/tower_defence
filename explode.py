import pygame
import time

class Explode(object):
    pygame.init()
    position_x=0
    position_y=0
    depart = 0
    tour_image = pygame.image.load("explosion.png")
    envie = True

    explosion = []
    i=0
    j=0

    def __init__(self,pos_x,pos_y,lecran):

        self.position_x = pos_x
        self.position_y=pos_y
        self.depart_time =int(time.time()*1000.0)
        self.envie = True
        self.ecran = lecran

        i=0

        for y in range (0,320,64):                              # parcour  la largeur de limage source par pas de 64
            for x in range (0,320,64):                          # parcour  la hauteur de limage source par pas de 64
                image = pygame.Surface((64,64), pygame.SRCALPHA)
                for yy in range (0,64):                         # parcour  la largeur de limage destination
                    for xx in range (0,64):                     # parcour  la hauteur de limage destination
                        c = self.tour_image.get_at((xx+x, yy+y))     # Recupere la couleur du pixel dans limage source
                        image.set_at((xx,yy),c)                 # affecte la couleur à limage destination
                image=pygame.transform.scale(image,(15,15))
                self.explosion.append(image)

                i+=1


    @property
    def x(self):
        #print ("Récupération de la position x du perso")
        return self.position_x

    @x.setter
    def x(self, pos_x):
        #print ("Changement de la position x du perso")
        self.position_x  =  pos_x

    @property
    def y(self):
        #print ("Récupération de la position x du perso")
        return self.position_y

    @y.setter
    def y(self, pos_y):
        #print ("Changement de la position x du perso")
        self.position_y  =  pos_y

    def affiche(self):
        self.control_duree()
        self.ecran.blit(self.explosion[self.j],(self.position_x,self.position_y))

    def control_duree(self):
        arrive =int(time.time()*1000.0)
        if (arrive-self.depart_time>=100):
            self.j+=1
            self.depart_time=int(time.time()*1000.0)
            if (self.j>24):
                self.envie=False
                self.j=0

    @property
    def isenvie(self):
        return self.envie
