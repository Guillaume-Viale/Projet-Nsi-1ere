#ecrire PIP install pygame dans la console
#fenetre de 700p * 500p
#RETRO ADVENTURE
import pygame
from pygame.locals import *
import math
from player import *
from monstre import *

pygame.init()
pygame.mixer.init()
fenetre = pygame.display.set_mode((700, 500))
#pygame.display.toggle_fullscreen()
boucle=1

#IMAGE
fond=pygame.image.load("CielFinal.20.png").convert()
fond=pygame.transform.scale(fond, (700,500))
fondMain=pygame.image.load("FondMainmenu.jpg").convert()
fondMain=pygame.transform.scale(fondMain,(700,500))
sol_herbe=pygame.image.load("pixil-frameHerbe.png").convert_alpha()
sol_terre=pygame.image.load("TerreFinal700500.png").convert_alpha()
sol_terre=pygame.transform.scale(sol_terre,(675,482))
vie1=pygame.image.load("Coeur_Heros.png").convert_alpha()
vie2=pygame.image.load("CoeurPerduHeros.png").convert_alpha()
balle=pygame.image.load("attaque.png").convert_alpha()
mechant1=pygame.image.load("Antenne.png").convert_alpha()
mechant2=pygame.image.load("Imprimante.png").convert_alpha()
mechant3=pygame.image.load("pixil-frameSmartphone.png").convert_alpha()
#mechant4=pygame.image.load("").convert_alpha()
joueur=Player()
ennemi=Monstre()


#GAMEPLAY
score = '0'
vie = 3


#TEXTE
white = (255, 255, 255)
black = (0, 0, 0)
font=pygame.font.Font('Minecraftia-Regular.ttf', 25)
Title=font.render('RETRO ADVENTURE', False, white)
starttext=font.render('CLICK TO START', True, white)
gameover=font.render('GAME OVER',True,white)


#PAS_CHANGER
FPS = 60
time = 0
MouseD = False
inMenu = True
state=False
GameOver = False
clock = pygame.time.Clock()
tirs_liste = []

def draw(inMenu,GameOver,scoreTexte,vie):
    # Fond et Musique
    if inMenu:

        fenetre.blit(fondMain,(0,0))
        fenetre.blit(starttext, (250,350))
        fenetre.blit(Title,(220,100))


    if inMenu == False:
        fenetre.blit(fond, (0, 0))

        SCREEN_WIDTH = 700
        SCREEN_HEIGHT = 500

        # create game window
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # load image

        fond_width = fond.get_width()
        fond_rect = fond.get_rect()

        # define game variables
        scroll = 0
        tiles = math.ceil(SCREEN_WIDTH / fond_width) + 1

        for i in range(0, tiles):
            screen.blit(fond, (i * fond_width + scroll, 0))
            fond_rect.x = i * fond_width + scroll
            pygame.draw.rect(screen, (255, 0, 0), fond_rect, 1)

            # scroll background
        scroll -= 5

        # reset scroll
        if abs(scroll) > fond_width:
            scroll = 0
        if vie == 3:
            fenetre.blit(vie1,(-300,-150))
            fenetre.blit(vie1,(-250,-150))
            fenetre.blit(vie1,(-200,-150))
            pygame.display.flip
        else:
            if vie == 2:
                fenetre.blit(vie1,(-300,-150))
                fenetre.blit(vie1,(-250,-150))
                fenetre.blit(vie2,(-200,-150))
                pygame.display.flip
            else:
                if vie == 1:
                    fenetre.blit(vie1,(-300,-150))
                    fenetre.blit(vie2,(-250,-150))
                    fenetre.blit(vie2,(-200,-150))
            pygame.display.flip
        fenetre.blit(joueur.image,joueur.rect)
        fenetre.blit(ennemi.image,ennemi.rect)
        
        for i in range (-450,350,45):
            fenetre.blit(sol_herbe, (i,125))
            fenetre.blit(sol_terre, (i+50,175))
            fenetre.blit(sol_terre, (i+50,205))
            fenetre.blit(sol_terre, (i+50,235))
        fenetre.blit(scoreTexte,(600,40))
        for tir in tirs_liste:
            fenetre.blit(vie1,(tir[0],tir[1]))
        if GameOver == True:
            inMenu = True
            fenetre.blit(fondMain,(0,0))
            fenetre.blit(gameover,(230,500))
            pygame.display.flip

    pygame.display.update()
def main(inMenu, GameOver, vie, score, ):
    
    run = True
    while run:
        # Tick at n FPS
        clock.tick(FPS)
        time = clock.get_time


        # Event handler
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                inMenu = False
                MouseD = True

            else:
                MouseD = False

            if inMenu == True:
                pygame.mixer.music.load("MusiqueJeu.mp3")
                pygame.mixer.music.set_volume(2.0)
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.load("RETRO-ADVENTURE-MUSIC.wav")
                pygame.mixer.music.set_volume(2.0)
                pygame.mixer.music.play(loops=-1)




            if event.type == pygame.QUIT:
                run = False

        KEYS_PRESSED = pygame.key.get_pressed()
        if KEYS_PRESSED[K_RIGHT]:
            joueur.move_right()
        if KEYS_PRESSED[K_LEFT]:
            joueur.move_left()
        if KEYS_PRESSED[K_UP]:
                joueur.move_jump()
        if joueur.rect.y==0 or KEYS_PRESSED[K_UP]==False:
            while joueur.rect.y!=100:
                joueur.rect.y+=1
           
        if KEYS_PRESSED[K_q]:
            vie -= 1
        if vie <=0:
            GameOver = True
        if MouseD == True:
            score = str(int(score) + 1)
        scoreTexte = font.render(score, True, white)
        if KEYS_PRESSED[pygame.K_ESCAPE]:
            pygame.quit()
            run = False

        #Tir

    



        # Call draw function
        draw(inMenu,GameOver,scoreTexte,vie)



if __name__ == '__main__':
    main(inMenu,GameOver,vie,score)
pygame.quit()
