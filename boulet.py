# Créé par phoebus, le 17/03/2020 en Python 3.4
import pygame
import time
import numpy as np
import math

class Boulet(object):
    pygame.init()
    position_x=0
    position_y=0
    depart = 0
    mode = "boulet"
    tour_image = pygame.image.load("explosion.png")
    explosion = []
    envie = True
    j=0

    def __init__(self,pos_x,pos_y, arrive_x,arrive_y,lecran):
        self.perso_image = pygame.image.load("boulet.png")
        self.perso_image = pygame.transform.scale(self.perso_image,(15,15))

        self.depart = np.array([pos_x,pos_y], dtype=np.float)
        self.arrive = np.array([arrive_x,arrive_y], dtype=np.float)

        self.direction = self.depart-self.arrive
        self.direction = -self.direction
        norm=np.linalg.norm(self.direction, ord=1)
        self.direction=self.direction/norm

        #lengths=np.linalg.norm(self.arrive, axis=-1)
        #self.direction[lengths > 0] = self.arrive[lengths > 0] / lengths[lengths > 0][:, np.newaxis]

        self.position_x = pos_x
        self.position_y=pos_y
        self.ecran = lecran
        self.depart_time =int(time.time()*1000.0)
        self.envie = True

        for y in range (0,320,64):                              # parcour  la largeur de limage source par pas de 64
            for x in range (0,320,64):                          # parcour  la hauteur de limage source par pas de 64
                image = pygame.Surface((64,64), pygame.SRCALPHA)
                for yy in range (0,64):                         # parcour  la largeur de limage destination
                    for xx in range (0,64):                     # parcour  la hauteur de limage destination
                        c = self.tour_image.get_at((xx+x, yy+y))     # Recupere la couleur du pixel dans limage source
                        image.set_at((xx,yy),c)                 # affecte la couleur à limage destination
                image=pygame.transform.scale(image,(15,15))
                self.explosion.append(image)

                #i+=1


    @property
    def x(self):
        #print ("Récupération de la position x du perso")
        return self.depart[0]

    @x.setter
    def x(self, pos_x):
        #print ("Changement de la position x du perso")
        self.position_x  =  pos_x

    @property
    def y(self):
        #print ("Récupération de la position x du perso")
        return self.depart[1]

    @y.setter
    def y(self, pos_y):
        #print ("Changement de la position x du perso")
        self.position_y  =  pos_y

    @property
    def isenvie(self):
        return self.envie

    def affiche(self):
        if (self.mode=="boulet"):
            self.affiche_boulet()
        elif (self.mode=="explosion"):
            self.affiche_explosion()


    def deplace(self):

        self.depart=(self.depart+self.direction)

        """
        if self.position_x>=self.ecran.get_width():
            self.position_x=0
        """
    def control_duree(self):
        arrive =int(time.time()*1000.0)
        if (arrive-self.depart_time>=3000):
            self.mode="explosion"

    def affiche_boulet(self):
        self.deplace()
        self.control_duree()
        self.ecran.blit(self.perso_image,(self.depart))

    def affiche_explosion(self):
        self.control_duree_explosion()
        self.ecran.blit(self.explosion[self.j],(self.depart))

    def control_duree_explosion(self):
        arrive =int(time.time()*1000.0)
        if (arrive-self.depart_time>=100):
            self.j+=1
            self.depart_time=int(time.time()*1000.0)
            if (self.j>24):
                self.envie=False
                self.j=0
                self.envie = False

