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
fond=pygame.image.load("CielFinal.20.png").convert()
fond=pygame.transform.scale(fond, (700,500))
sol=pygame.image.load("pixil-frameHerbe.png").convert_alpha()
fenetre.blit(fond, (0,0))

pierre=pygame.image.load("pixil-frameStatique1.png").convert_alpha()
pygame.display.flip()
x_movement=20
y_movement=20
FPS = 60
white = (255, 255, 255)
black = (0, 0, 0)
MouseD = False
inMenu = True
GameOver = False
clock = pygame.time.Clock()
font=pygame.font.Font('freesansbold.ttf', 32)
Title=font.render('RETRO ADVENTURE',True, white,black)
starttext=font.render('CLICK TO START', True, white, black)
gameover=font.render('GAME OVER',True,white,black)
#personnage=pygame.image.load("MAIN_CHARACTER.gif").convert_alpha()
#fenetre.blit(personnage(x,y))
def handle_keys(keys: list, pos: pygame.Rect):
    if pos.y == 100:
        state= True
    else:
        state= False
        
    if pos.y != 100:
        pos.y += 5
    if state==True :
        if keys[pygame.K_SPACE]:
            # If space is pressed
            for i in range(100):
                pos.y-=1
         
    if keys[pygame.K_z]: # Forward
        # If z is pressed
        pos.y -= 2
    
    if keys[pygame.K_a]:
        # If q is pressed
        pos.x -= 2
     
    if keys[pygame.K_s]:
        pos.y += 2
     
    if keys[pygame.K_d]:
        pos.x += 2
def draw(pos: pygame.Rect):
    # Fond
    if inMenu:
        fenetre.blit(fondMain,(0,0))
        fenetre.blit(starttext, (250,350))
        fenetre.blit(Title,(250,100)
    if inMenu == False:
        fenetre.blit(fond, (0,0))
   
        fenetre.blit(pierre, (pos[0],pos[1]))
        for i in range (-450,350,45):
            fenetre.blit(sol, (i,125))  
         if GameOver == True:
            fenetre.blit(fondMain,(0,0))
            inMenu = True
            fenetre.blit(gameover,(250,100))
            pygame.display.flip
                  
    pygame.display.update()
def main(inMenu,GameOver):
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
        if KEYS_PRESSED[pygame.K_q]:
            GameOver = True
            
        # Handle the keys
        handle_keys(KEYS_PRESSED, PLAYER_RECT)
        # Call draw function
        draw(PLAYER_RECT,inMenu,GameOver)
        print(MouseD,inMenu,GameOver)
        
#Class sound:
pygame.mixer.init()
pygame.mixer.music.load("RETRO-ADVENTURE-MUSIC.wav")
pygame.mixer.music.set_volume(3.0)
pygame.mixer.music.play(loops=-1)
    # Quit
#pygame.quit()
if __name__ == '__main__':
    main(inMenu,GameOver)
pygame.quit()
