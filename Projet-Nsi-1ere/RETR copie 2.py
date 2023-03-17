#ecrire PIP install pygame dans la console
#fenetre de 700p * 500p
#RETRO ADVENTURE
import pygame
import math
from pygame.locals import *
from pygame import mixer
from player import *
from monstre import *

pygame.init()
fenetre = pygame.display.set_mode((700, 500))
#pygame.display.toggle_fullscreen()
boucle=1

#IMAGE
fond=pygame.image.load("CielFinal_20.png").convert()
fond=pygame.transform.scale(fond, (700,500))
fondMain=pygame.image.load("FondMainmenu.jpg").convert()
fondMain=pygame.transform.scale(fondMain,(700,500))
sol_herbe=pygame.image.load("pixil-frameHerbe.png").convert_alpha()
sol_terre=pygame.image.load("TerreFinal700500.png").convert_alpha()
sol_terre=pygame.transform.scale(sol_terre,(675,482))
vie1=pygame.image.load("Coeur_Heros.png").convert_alpha()
vie2=pygame.image.load("CoeurPerduHeros.png").convert_alpha()
balle=pygame.image.load("attaque.png").convert_alpha()
mechant1=pygame.image.load("M_Antenne.png").convert_alpha()
mechant2=pygame.image.load("M_Imprimante.png").convert_alpha()
mechant3=pygame.image.load("M_Smartphone.png").convert_alpha()
#mechant4=pygame.image.load("").convert_alpha()
joueur=Player()
ennemi=Monstre()


#GAMEPLAY
score = 0
vie = 3
niveau = 1


#TEXTE
white = (255, 255, 255)
black = (0, 0, 0)
font=pygame.font.Font('Minecraftia-Regular.ttf', 25)
Title=font.render('RETRO ADVENTURE', False, white)
starttext=font.render('CLICK TO START', True, white)
gameover=font.render('GAME OVER',True,white)
endtext=font.render('TOO BAD, TRY AGAIN !', True, white)

#PAS_CHANGER
FPS = 60
time = 0
MouseD = False
inMenu = True
inGame = False
inEndMenu = False
state=False
GameOver = False
clock = pygame.time.Clock()
tirs_liste = []

def draw(inMenu,inGame,inEndMenu,GameOver,scoreTexte,vie,levelTexte):
    # Fond
    if inMenu:
        fenetre.blit(fondMain,(0,0))
        fenetre.blit(starttext, (250,350))
        fenetre.blit(Title,(220,100))
    if inGame == True:
        fenetre.blit(fond, (0,0))
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
        fenetre.blit(scoreTexte,(550,40))
        fenetre.blit(levelTexte,(550,80))
        for tir in tirs_liste:
            fenetre.blit(vie1,(tir[0],tir[1]))
    if inEndMenu == True: 
        fenetre.blit(fondMain,(0,0))
        fenetre.blit(endtext, (250,350))
        fenetre.blit(gameover,(220,100)) 

    pygame.display.update()
def main(inMenu,inGame,inEndMenu, GameOver,vie,score,niveau):
    ir = 0
    ig = 0

    run = True
    while run:
        # Tick at n FPS
        clock.tick(FPS)
        time = clock.get_time
        # Event handler
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                inMenu = False
                inGame = True
                MouseD = True
            else:
                MouseD = False


            if event.type == pygame.QUIT:
                run = False

        KEYS_PRESSED = pygame.key.get_pressed()
        
        if KEYS_PRESSED[K_RIGHT]:
            joueur.move_right(ir)
            ir += 1
        if KEYS_PRESSED[K_LEFT]:
            joueur.move_left(ig)
            ig += 1
        if KEYS_PRESSED[K_UP]:
            joueur.move_jump()
            #joueur.down_jump()
        if joueur.rect.y==0 or KEYS_PRESSED[K_UP]==False:
            while joueur.rect.y<100:
               joueur.down_jump()
       
        if joueur.rect.x > ennemi.rect.x:
            ennemi.rect.x+=5  
        if joueur.rect.x < ennemi.rect.x:
            ennemi.rect.x-=5 
        if KEYS_PRESSED[K_q]:
            vie -= 1
        if vie <=0:
            inEndMenu = True

        if MouseD == True:
            score = int(score) + 1


        Affscore = 'score '
        Affscore += str(score)

        Afflevel = 'level '
        Afflevel += str(niveau) 
            
        scoreTexte = font.render(Affscore, True, white)
        levelTexte = font.render(Afflevel, True, white)
        if KEYS_PRESSED[pygame.K_ESCAPE]:
            pygame.quit()
            run = False

        #Tir
    



        # Call draw function
        draw(inMenu,inGame,inEndMenu,GameOver,scoreTexte,vie,levelTexte)





#Class sound:
pygame.mixer.init()
pygame.mixer.music.load("musiqueJeu.mp3")
pygame.mixer.music.set_volume(3.0)
pygame.mixer.music.play(loops=-1)

if __name__ == '__main__':
    main(inMenu,inGame,inEndMenu,GameOver,vie,score,niveau)
pygame.quit()
