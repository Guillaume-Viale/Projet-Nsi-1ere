import pygame
from pygame.locals import *
from pygame import mixer

pygame.init()
fenetre = pygame.display.set_mode((700, 500))
x=25
y=25
boucle=1
fond=pygame.image.load("pixil-frame-0(5).png").convert()
fenetre.blit(fond, (0,0))
#pierre=pygame.image.load("PIERRE.png").convert_alpha()
pygame.display.flip()
#fenetre.blit(pierre,(20,20))
pygame.display.flip()
#personnage=pygame.image.load("MAIN_CHARACTER.gif").convert_alpha()
#fenetre.blit(personnage(x,y))
#Class sound:
pygame.mixer.init()
pygame.mixer.music.load("RETRO-ADVENTURE-MUSIC.wav")
pygame.mixer.music.set_volume(3.0)
pygame.mixer.music.play(loops=-1)



while boucle:
    for event in pygame.event.get():

        if event.type == QUIT:
            boucle = 0 

