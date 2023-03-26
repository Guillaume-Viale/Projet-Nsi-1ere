import pygame
from random import *


#Creer classe gérant la notion de monstre sur le jeu
class Monstre(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack  = 5
        self.listemonstre=["ImagesEnemies/M_Antenne.png","ImagesEnemies/M_Imprimante.png","ImagesEnemies/M_Smartphone.png"]
        self.image = pygame.image.load("ImagesEnemies/M_Imprimante.png")
        self.image = pygame.transform.scale(self.image,(400,350))
        self.rect = self.image.get_rect()
        self.rect.x = randint(-200,200)
        self.rect.y = 200
        self.isDead = False


  
        
        


