import pygame
import random
import sys     # Module qui permet de quitter et fermer la fenetre du jeu 
import time

class Jeu: # Class qui contient toutes les variables, ainsi que les fonctions utiles pour le bon déroulement du jeu.

    def __init__(self): # Fonction position initial du serpent

        self.ecran = pygame.display.set_mode((520, 450)) # Dimensions de la fenêtre 520.500
        
        pygame.display.set_caption("Snake Zayzay")   # Nom de la fenêtre
        
        self.jeu_encours = True

        # Créer des variables de position et de direction du serpent
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0

        self.serpent_corps = 12

        # Création de la pomme aléatoirement
        self.pomme_position_x = random.randrange(50, 470, 10)
        self.pomme_position_y = random.randrange(50, 365, 10)
        self.pomme = 12

        # Liste qui recense les positions du serpent
        self.positions_serpent = []

        # Fps du serpent
        self.clock = pygame.time.Clock()
        self.clock.tick(10)

    # Nous allons créer une fonction qui permet que le serpent ne parte pas hors cadre. Nous allons délimiter le jeu grace a un rectangle.
    def limites(self):
        pygame.draw.rect(self.ecran, (255,255,255), (30, 40, 460, 350), 3)
        
    # Permet de gerer les evenements (ex : toucher une touche est un evenement, bouger la souris est un evenement), d'afficher certains composants du jeu grace au while loop
    def fonction_principale(self): 
        
        # Variable de la taille du serpent
        self.taille_serpent = 1

        global score
        score = 0

        font = pygame.font.Font(None,25)
        titre = ('S     N     A     K     E')

        while self.jeu_encours:

            text_surface2 = font.render(titre, self.jeu_encours, (0,255,0))
            self.ecran.blit(text_surface2,(175,200))
            self.clock.tick(20)

            # Nous allons afficher le serpent
            pygame.draw.rect(self.ecran,(0,255,0),(self.serpent_position_x, self.serpent_position_y, self.serpent_corps, self.serpent_corps))

            # Afficher la pomme
            pygame.draw.rect(self.ecran,(255,0,0),(self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme))

            # Afficher les limites
            self.limites()

            # Le serpent grossis lorsqu'il mange une pomme
            if self.pomme_position_y == self.serpent_position_y and self.pomme_position_x == self.serpent_position_x :
                self.taille_serpent +=2
                self.pomme_position_x = random.randrange(50, 470, 10)
                self.pomme_position_y = random.randrange(50, 365, 10)

                score +=10

            # Nous allons afficher le score
            score_text = ("Score : {0}".format(score))
            text_surface1 = font.render(score_text, self.jeu_encours, (255,255,255))
            self.ecran.blit(text_surface1,(50,60))
            self.clock.tick(60)

            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT: # Si le type d'evenement est "clicker sur la croix" ...
                    sys.exit()                    # ... alors le jeu s'éteint et la fenêtre disparait.

                # Nous allons créer les evenements qui permettent de bouger le serpents
                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == pygame.K_RIGHT:
                        self.serpent_direction_x = 10
                        self.serpent_direction_y = 0

                    if evenement.key == pygame.K_LEFT:
                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0

                    if evenement.key == pygame.K_DOWN:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = 10

                    if evenement.key == pygame.K_UP:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = -10


            # Après avoir créer les events, nous allons finalement faire bouger le serpent
            self.serpent_position_x += self.serpent_direction_x
            self.serpent_position_y += self.serpent_direction_y


            # Créer une liste qui stock la position de la tête du serpent
            la_tete_du_serpent = []
            la_tete_du_serpent.append(self.serpent_position_x)
            la_tete_du_serpent.append(self.serpent_position_y)

            # Append dans la liste des positions du serpent
            self.positions_serpent.append(la_tete_du_serpent)

            # Condition pour que le corps du serpent suit la tête dans ses deplacements
            if len(self.positions_serpent) > self.taille_serpent:
                self.positions_serpent.pop(0)

            # Afficher les autres parties du serpent
            for i in self.positions_serpent:
                pygame.draw.rect(self.ecran,(0,255,0), (i[0], i[1], self.serpent_corps, self.serpent_corps))

            # Fonction qui nous fait quitter le jeu lorsque l'on perd
            def GameOver():
                time.sleep(1)
                print("SCORE FINAL :" + " " +str(score))
                sys.exit()

            # Si le serpent se mord la queue, alors la partie se termine
            for i in self.positions_serpent[:-1]:
                if  la_tete_du_serpent == i: 
                    GameOver()
                    
                    
            # Si le serpent dépasse les limites du rectangle, alors la partie se termine
            if self.serpent_position_x < 30 or self.serpent_position_x > 480 or self.serpent_position_y < 40 or self.serpent_position_y > 375 :
                GameOver()
    
   
            # Mise a jour constante de l'écran pour voir les modifications
            pygame.display.flip()    
            
            # Couleur de l'écran
            self.ecran.fill((0,0,0)) 

if __name__ == '__main__':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()