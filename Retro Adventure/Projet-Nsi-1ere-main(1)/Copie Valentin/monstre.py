import pygame
from random import *


#Creer classe gérant la notion de monstre sur le jeu
class Monstre(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack  = 5
        self.listemonstre=["Antenne.png","Imprimante.png","pixil-frameSmartphone.png"]
        self.image = pygame.image.load(choice(self.listemonstre))
        self.rect = self.image.get_rect()
        self.rect.x = randint(-200,200)
        self.rect.y = 100

  
        
        


