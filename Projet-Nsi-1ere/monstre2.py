
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
        self.listemonstre=["M_Antenne.png","M_Imprimante.png","M_Smartphone.png"]
        self.image = pygame.image.load("M_Antenne.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 100
        self.timer = pygame.time.get_ticks()
        
    
        