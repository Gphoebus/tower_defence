"""
Tower defence made by phoebus brain
programation POO
Touche T pour pouvoir poser une tour

"""
import pygame
from pygame.locals import *
from tour import Tour
from pion import Pion
from boulet import Boulet


pygame.init()                                       # initialisation de pygame
gameDisplay = pygame.display.set_mode((800,600))    # Création de la fenetre de jeu
pygame.display.set_caption('Tower')                 # Affectation du nom de la fenetre

clock = pygame.time.Clock()                         # Démarrage de timer

#tour1 =Tour(10,10,gameDisplay)                      # création d une tour
#tour2=Tour(710,470,gameDisplay)                     # création d une tour
troll=Pion(16,278,gameDisplay)                      # création d un troll
boulets = []                                        # liste des boulets vide au départ
#les_explosions =[]
tours = []
une_tour = Tour(0,0,gameDisplay)

fin = False

mode = "normal"

while not fin:                                      # boulcle du jeu

    for event in pygame.event.get():                # traitement des evenements
        if event.type == QUIT:
            fin = True
        elif event.type == MOUSEBUTTONDOWN:

            if mode=="normal":
                posSouris = pygame.mouse.get_pos()  # Récupérer la position du pointeur
                boulets.append(Boulet(400,300,posSouris[0],posSouris[1],gameDisplay))
            elif mode=="tour":
                posSouris = pygame.mouse.get_pos()  # Récupérer la position du pointeur
                tours.append(Tour(posSouris[0],posSouris[1],gameDisplay) )
                mode = "normal"
        elif event.type == KEYDOWN and event.key == K_t:
            mode="tour"
        else:
            if mode=="tour":
                posSouris = pygame.mouse.get_pos()  # Récupérer la position du pointeur
                une_tour.x=posSouris[0]
                une_tour.y=posSouris[1]
                une_tour.affiche()
        pygame.display.update()





    #print (pressed)
    clock.tick(60)                                  # Réglage fps 60 img/s
    gameDisplay.fill((0,0,0))                       # mise a jour du fond

    #tour1.affiche()
    #tour2.affiche()
    troll.affiche()

    for t in tours:
        t.affiche()
        t.rayon(troll)
           # boulets.append(Boulet(t.x,t.y,troll.x,troll.y,gameDisplay))


    boulets_a_detruire = []                     # liste des boulets a détruire
    for i in range(len(boulets)):               # parcour de la liste des boulets
        if (len(boulets)>0):                    # Si la liste n est pas vide
            leboulet = boulets[i]               # Extraction d'un boulet de la liste des boulets
            leboulet.affiche()                  # Affichage du boulet extrait
            if (leboulet.isenvie==False):       # verification si le boulet est en vie
                boulets_a_detruire.append(i)    # si le boulet es mort l'ajouter à la liste des boulets à enlever

    # --- parcour de la liste des boulets à détruire

    for j in boulets_a_detruire:
        leboulet =boulets[j]
        #les_explosions.append(Explode(leboulet.x,leboulet.y,gameDisplay))
        boulets.remove(boulets[j])              # suppression du boulet de la liste des boulets
    """
    explosions_a_detruire=[]
    for k in range(len(les_explosions)):
        lexplosion = les_explosions[k]
        lexplosion.affiche()
        if (lexplosion.isenvie==False):
            explosions_a_detruire.append(k)

    for l in explosions_a_detruire:
        les_explosions.remove(les_explosions[l])
    """





    pygame.display.update()                         # Mise a jour de l'affichage


pygame.quit()                                       # Fin de pygame
quit()                                              # Fin de python
