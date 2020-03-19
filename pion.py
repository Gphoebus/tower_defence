# Créé par phoebus, le 17/03/2020 en Python 3.4
import pygame

class Pion(object):
    pygame.init()
    position_x=0
    position_y=0
    def __init__(self,pos_x,pos_y, lecran):
        self.perso_image = pygame.image.load("perso.png")
        self.perso_image = pygame.transform.scale(self.perso_image,(20,40))
        self.position_x = pos_x
        self.position_y = pos_y
        self.ecran = lecran

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
        self.deplace()

        self.ecran.blit(self.perso_image,(self.x,self.y))

    def deplace(self):

        self.position_x+=2
        if self.position_x>=self.ecran.get_width():
            self.position_x=0