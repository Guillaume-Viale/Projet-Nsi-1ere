import pygame

#definir la classe qui va gérer le projectile du joueur
class Projectile(pygame.sprite.Sprite):

    #definir constructeur de cette classe
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load("projectile.png")
        self.rect = self.image.get_rect()


    