﻿# Créé par phoebus, le 17/03/2020 en Python 3.4
import pygame
import time
import numpy as np

class Boulet(object):
    pygame.init()
    position_x=0
    position_y=0
    depart = 0
    def __init__(self,pos_x,pos_y, arrive_x,arrive_y,lecran):
        self.perso_image = pygame.image.load("boulet.png")
        self.perso_image = pygame.transform.scale(self.perso_image,(15,15))
        self.depart = np.array([pos_x,pos_y], dtype=np.float)
        self.arrive = np.array([arrive_x,arrive_y], dtype=np.float)

        self.direction =np.array([0,0], dtype=np.float)

        lengths=np.linalg.norm(self.arrive, axis=-1)
        self.direction[lengths > 0] = self.arrive[lengths > 0] / lengths[lengths > 0][:, np.newaxis]

        self.position_x = pos_x
        self.position_y=pos_y
        self.ecran = lecran
        self.depart_time =int(time.time()*1000.0)
        self.envie = True

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
        self.deplace()
        self.control_duree()
        self.ecran.blit(self.perso_image,(self.depart))

    def deplace(self):

        self.depart=(self.depart+self.direction)

        """
        if self.position_x>=self.ecran.get_width():
            self.position_x=0
        """
    def control_duree(self):
        arrive =int(time.time()*1000.0)
        if (arrive-self.depart_time>=3000):
            self.envie = False

