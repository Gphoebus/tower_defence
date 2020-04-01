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
        self.depart_time =int(time.time()*1000.0)

        self.x -= self.tour_image.get_width()/2
        self.y -= self.tour_image.get_height()/2

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
        """
        boulets_a_detruire = []
        for b in self.boulets:
            b.affiche()
            if (b.isenvie==False):
                boulets.remove(b)
        """
        boulets_a_detruire = []                     # liste des boulets a détruire
        for i in range(len(self.boulets)):               # parcour de la liste des boulets
            if (len(self.boulets)>0):                    # Si la liste n est pas vide
                leboulet = self.boulets[i]               # Extraction d'un boulet de la liste des boulets
                leboulet.affiche()                  # Affichage du boulet extrait
                if (leboulet.isenvie==False):       # verification si le boulet est en vie
                    boulets_a_detruire.append(i)    # si le boulet es mort l'ajouter à la liste des boulets à enlever

        # --- parcour de la liste des boulets à détruire

        for j in boulets_a_detruire:
            leboulet =self.boulets[j]
            #les_explosions.append(Explode(leboulet.x,leboulet.y,gameDisplay))
            self.boulets.remove(self.boulets[j])              # suppression du boulet de la liste des boulets

    def rayon(self,lepion):
        if (len(self.boulets)<self.nb_max_boulets):
            x=self.x
            y=self.y

            #print("tour",x,y)
            px=lepion.x
            py=lepion.y

            #print ("pion",px,py)
            dx=abs(x-px)
            dy=abs(y-py)


            dist = ((dx*dx)+(dy*dy))**(1/2)

            if (dist<=self.perimetre):
                arrive =int(time.time()*1000.0)
                if (arrive-self.depart_time>=self.cadence):
                    print("arrive = {} , depart = {} , difference {}".format(arrive,self.depart_time,arrive-self.depart_time))
                    self.boulets.append(Boulet(x,y,px,py,self.ecran))
                    self.nb_boulets_lance+=1
                    print("Un boulet de plus")
                    self.depart_time=int(time.time()*1000.0)


