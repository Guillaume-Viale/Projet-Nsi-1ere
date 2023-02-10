#ecrire PIP install pygame dans la console
#fenetre de 700p * 500p
#RETRO ADVENTURE
import pygame
from pygame.locals import *
from pygame import mixer

pygame.init()
fenetre = pygame.display.set_mode((700, 500))
pygame.display.toggle_fullscreen()
boucle=1
#IMAGE
fond=pygame.image.load("CielFinal.20.png").convert()
fond=pygame.transform.scale(fond, (700,500))
fondMain=pygame.image.load("FondMainmenu.jpg").convert()
fondMain=pygame.transform.scale(fondMain,(700,500))
sol=pygame.image.load("pixil-frameHerbe.png").convert_alpha()
pierre=pygame.image.load("pixil-frameStatique1.png").convert_alpha()
vie1=pygame.image.load("Coeur_Heros.png").convert_alpha()
vie2=pygame.image.load("CoeurPerduHeros.png").convert_alpha()

#GAMEPLAY
score = '0'
vie = 3


#TEXTE
white = (255, 255, 255)
black = (0, 0, 0)
font=pygame.font.Font('freesansbold.ttf', 32)
Title=font.render('RETRO ADVENTURE',True, white,black)
starttext=font.render('CLICK TO START', True, white, black)
gameover=font.render('GAME OVER',True,white,black)


#PAS_CHANGER
FPS = 60
MouseD = False
inMenu = True
GameOver = False
clock = pygame.time.Clock()


def handle_keys(keys: list, pos: pygame.Rect):
    if pos.y == 100:
        state= True
    else:
        state= False
        
    if pos.y != 100:
        pos.y += 10
    if state==True :
        if keys[pygame.K_SPACE]:
            # If space is pressed
            for i in range(100):
                pos.y-=1
         
    #MOUVEMENT HORIZONTALE(FLECHES)
    if keys[pygame.K_LEFT]:
        pos.x -= 5
    if keys[pygame.K_RIGHT]:
        pos.x += 5


def draw(pos: pygame.Rect,inMenu,GameOver,scoreTexte,vie):
    # Fond
    if inMenu:
        fenetre.blit(fondMain,(0,0))
        fenetre.blit(starttext, (250,350))
        fenetre.blit(Title,(220,100))
    if inMenu == False:
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
        fenetre.blit(pierre, (pos[0],pos[1]))
        for i in range (-450,350,45):
            fenetre.blit(sol, (i,125))  
        fenetre.blit(scoreTexte,(600,40))
        if GameOver == True:
            inMenu = True
            fenetre.blit(fondMain,(0,0))
            fenetre.blit(gameover,(230,500))
            pygame.display.flip
                  
    pygame.display.update()

def main(inMenu,GameOver,vie,score):
    PLAYER_RECT = pierre.get_rect(center=(
        fenetre.get_width()//2,
        fenetre.get_height()//2
    ))
    run = True
    while run:
        # Tick at n FPS
        clock.tick(FPS)

        # Event handler
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                inMenu = False
                MouseD = True
            else:
                MouseD = False
                
            
            if event.type == pygame.QUIT:
                run = False
                
        KEYS_PRESSED = pygame.key.get_pressed()
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
        # Handle the keys
        handle_keys(KEYS_PRESSED, PLAYER_RECT)
        # Call draw function
        draw(PLAYER_RECT,inMenu,GameOver,scoreTexte,vie)
        print(vie,score)
        
#Class sound:
pygame.mixer.init()
pygame.mixer.music.load("RETRO-ADVENTURE-MUSIC.wav")
pygame.mixer.music.set_volume(3.0)
pygame.mixer.music.play(loops=-1)
    
if __name__ == '__main__':
    main(inMenu,GameOver,vie,score)
pygame.quit()
