import pygame
from random import *


#Creer classe gérant la notion de monstre sur le jeu
class Monstre2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack  = 5
        self.ondesliste = []
        self.listemonstre=["ImagesEnemies/M_Antenne.png","ImagesEnemies/M_Imprimante.png","ImagesEnemies/M_Smartphone.png"]
        self.image = pygame.image.load("ImagesEnemies/M_Antenne.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,(490,350))
        self.rect.x = 450
        self.rect.y = 190
        self.isDead= false
        self.timer = pygame.time.get_ticks()
        
