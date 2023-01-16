import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((700, 500))
x=25
y=25
boucle=1
fond=pygame.image.load("pixil-frame-0(5).png").convert()
fenetre.blit(fond, (0,0))
pierre=pygame.image.load("PIERRE.png").convert_alpha()
pygame.display.flip()
fenetre.blit(pierre,(20,20))
pygame.display.flip()
#personnage=pygame.image.load("MAIN_CHARACTER.gif").convert_alpha()
#fenetre.blit(personnage(x,y))
Class sound:
    

while boucle:
    for event in pygame.event.get():

        if event.type == QUIT:
            boucle = 0 
