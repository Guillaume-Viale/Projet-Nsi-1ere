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
fenetre.blit(fond, (0,0))
pierre=pygame.image.load("PIERRE.png").convert_alpha()
pygame.display.flip()
x_movement=20
y_movement=20
FPS = 60
clock = pygame.time.Clock()
#personnage=pygame.image.load("MAIN_CHARACTER.gif").convert_alpha()
#fenetre.blit(personnage(x,y))
def handle_keys(keys: list, pos: pygame.Rect):
    if keys[pygame.K_w]: # Forward
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
    fenetre.blit(fond, (0,0))
    # Blit player
    fenetre.blit(pierre, pos)

    # Update
    pygame.display.update()
def main():
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
            if event.type == pygame.QUIT:
                run = False
        KEYS_PRESSED = pygame.key.get_pressed()
        # Handle the keys
        handle_keys(KEYS_PRESSED, PLAYER_RECT)
        # Call draw function
        draw(PLAYER_RECT)
#Class sound:
pygame.mixer.init()
pygame.mixer.music.load("RETRO-ADVENTURE-MUSIC.wav")
pygame.mixer.music.set_volume(3.0)
pygame.mixer.music.play(loops=-1)
    # Quit
#pygame.quit()
if __name__ == '__main__':
    main()

