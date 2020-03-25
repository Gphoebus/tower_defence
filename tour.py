# Créé par phoebus, le 17/03/2020 en Python 3.4
import pygame
from boulet import Boulet
import time

class Tour(object):
    pygame.init()
    position_x=0
    position_y=0
    perimetre = 100
    boulets = []
    nb_max_boulets = 4
    nb_boulets_lance = 0
    cadence = 800
    def __init__(self,pos_x,pos_y, lecran):
        self.tour_image = pygame.image.load("tour.png")
        self.tour_image= pygame.transform.scale(self.tour_image,(36,65))
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
        self.affiche_boulet()

    def affiche_boulet(self):
        for b in self.boulets:
            b.affiche()

    def rayon(self,lepion):
        if (self.nb_boulets_lance<self.nb_max_boulets):
            x=self.x
            y=self.y
#
            print("tour",x,y)
            px=lepion.x
            py=lepion.y

            #print ("pion",px,py)
            dx=abs(x-px)
            dy=abs(y-py)


            dist = ((dx*dx)+(dy*dy))**(1/2)

            if (dist<=self.perimetre):

                self.boulets.append(Boulet(x,y,px,py,self.ecran))
                self.nb_boulets_lance+=1
                print("Un boulet de plus")


