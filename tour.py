# Créé par phoebus, le 17/03/2020 en Python 3.4
import pygame

class Tour(object):
    pygame.init()
    position_x=0
    position_y=0
    def __init__(self,pos_x,pos_y, lecran):
        self.tour_image = pygame.image.load("tour.png")
        self.x = pos_x
        self.y=pos_y
        self.ecran = lecran

    @property
    def x(self):
        #print ("Récupération de la position x de la tour")
        return self.position_x

    @x.setter
    def x(self, pos_x):
        #print ("Changement de la position x de la tour")
        self.position_x  =  pos_x

    @property
    def y(self):
        #print ("Récupération de la position x de la tour")
        return self.position_y

    @y.setter
    def y(self, pos_y):
        #print ("Changement de la position x de la tour")
        self.position_y  =  pos_y

    def affiche(self):

        self.ecran.blit(self.tour_image,(self.x,self.y))
