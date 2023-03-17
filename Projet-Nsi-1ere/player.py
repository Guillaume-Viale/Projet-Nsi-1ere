import pygame
from attaquesDistance import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.jump_velocity = 10 # La vitesse de saut
        self.jumpaction=False
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("pixil-frameStatique1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 100

    #i peut être un entier quelconque
    def move_right(self,i):
        i = i % 4
# mais sici on stocke dans i le reste de la divsion de i par 4 donc i ne varie que entre 0, 1, 2 et 3
        NameImage = "Mulet_"
        NameImage += str(i+1)
# on met la veleur i+1 au bout du fichier 
        NameImage += ".png"
        self.image = pygame.image.load(NameImage)
        self.rect.x+=self.velocity


       
    def move_left(self,i):
        i = i % 4
        NameImage = "Mulet_G"
        NameImage += str(i+1)
        NameImage += ".png"
        self.image = pygame.image.load(NameImage)
        self.rect.x-=self.velocity

    def move_jump(self):
        self.rect.y -= self.jump_velocity

        



    def launch_projectile(self):
        #creer nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile())



