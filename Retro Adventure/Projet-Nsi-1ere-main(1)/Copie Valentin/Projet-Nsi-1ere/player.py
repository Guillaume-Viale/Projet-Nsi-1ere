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
    def move_right(self):
        self.rect.x+=self.velocity
    def move_left(self):
        self.rect.x-=self.velocity
    def move_jump(self):
        self.rect.y -= self.jump_velocity

        



    def launch_projectile(self):
        #creer nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile())



