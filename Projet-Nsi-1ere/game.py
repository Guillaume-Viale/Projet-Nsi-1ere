import pygame
from monstre import*

class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mob=Monstre()
        #mettre dans cette liste les monstres(classes) de la vague
        self.vague=[]
        self.monstre_count=5
        i = 0
        if len(self.vague) >0:
            while i <= len(self.vague):
                #1* par seconde
                if int(pygame.time.get_ticks) % 1000 == 0:
                    #spawner le mosntre a droite
                    #self.vague[i].rect.x = 700 
                    #activer le monstre
                    #self.vague[i].state = True
                    i = i+1
        else:
            #vague 2, plus difficile
            self.vague=[]
            if len(self.vague) >0:
                while i <= len(self.vague):
                #2* par seconde
                    if int(pygame.time.get_ticks) % 500 == 0:
                        #spawner le mosntre a droite
                        #self.vague[i].rect.x = 700 
                        #activer le monstre
                        #self.vague[i].state = True
                        i = i+1
        #possibilité de mettre une vague 3
