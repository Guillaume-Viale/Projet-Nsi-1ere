# ecrire PIP3 install pygame dans la console
# fenetre de 700p * 500p
# RETRO ADVENTURE
import pygame
import math
from pygame.locals import *
from pygame import mixer
from monstre2 import*
from monstre3 import*
import scripts

pygame.init()
fenetre = pygame.display.set_mode((700, 500))
# pygame.display.toggle_fullscreen()
boucle = 1

# IMAGE
fond = pygame.image.load("ImagesFond/CielFinal_20.png").convert()
fond = pygame.transform.scale(fond, (700, 500))
fondMain = pygame.image.load("ImagesFond/Accueil.png").convert()
fondMain = pygame.transform.scale(fondMain, (700, 500))
sol_herbe = pygame.image.load("ImagesFond/pixil-frameHerbe.png").convert_alpha()
sol_terre = pygame.image.load("ImagesFond/TerreFinal700500.png").convert_alpha()
sol_terre = pygame.transform.scale(sol_terre, (675, 482))
vie1 = pygame.image.load("ImagesHeros/Coeur_Heros.png").convert_alpha()
vie2 = pygame.image.load("ImagesHeros/CoeurPerduHeros.png").convert_alpha()
balle = pygame.image.load("ImagesHeros/attaque.png").convert_alpha()
balle2 = pygame.image.load("ImagesHeros/attaque2.png").convert_alpha()
balle_m = pygame.image.load("ImagesAttaques/wifi.png").convert_alpha()
balle_m = pygame.transform.scale(balle_m,(50,50))
mechant1 = pygame.image.load("ImagesEnemies/M_Antenne.png").convert_alpha()
mechant2 = pygame.image.load("ImagesEnemies/M_Imprimante.png").convert_alpha()
mechant3 = pygame.image.load("ImagesEnemies/M_Smartphone.png").convert_alpha()
# mechant4=pygame.image.load("").convert_alpha()
joueur = scripts.Player()
ennemi = scripts.Monstre()
ennemi2 = Monstre2()
ennemi3 = Monstre3()
# GAMEPLAY
score = 0
vie = 3
niveau = 1

# TEXTE
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font('ImagesFond/Minecraftia-Regular.ttf', 25)
Title = font.render('RETRO ADVENTURE', False, white)
starttext = font.render('CLICK TO START', True, white)
gameover = font.render('GAME OVER', True, white)
endtext = font.render('TOO BAD TRY AGAIN !', True, white)
# PAS_CHANGER

time = 0
time2 = 0
time3 = 0
MouseD = False
inMenu = True
inGame = False
inEndMenu = False
state = False
clock = pygame.time.Clock()
tirs_liste = []


def draw(inMenu, inGame, inEndMenu, scoreTexte, vie, levelTexte):
    # Fond
    if inMenu:
        fenetre.blit(fondMain, (0, 0))
        fenetre.blit(starttext, (230, 400))
        fenetre.blit(Title, (230, 100))
    if inGame == True:
        fenetre.blit(fond, (0, 0))
        if vie == 3:
            fenetre.blit(vie1, (-300, -150))
            fenetre.blit(vie1, (-250, -150))
            fenetre.blit(vie1, (-200, -150))
            pygame.display.flip
        else:
            if vie == 2:
                fenetre.blit(vie1, (-300, -150))
                fenetre.blit(vie1, (-250, -150))
                fenetre.blit(vie2, (-200, -150))
                pygame.display.flip
            else:
                if vie == 1:
                    fenetre.blit(vie1, (-300, -150))
                    fenetre.blit(vie2, (-250, -150))
                    fenetre.blit(vie2, (-200, -150))
            pygame.display.flip
        fenetre.blit(joueur.image, joueur.rect)
        fenetre.blit(ennemi.image, ennemi.rect)
        fenetre.blit(ennemi2.image, ennemi2.rect)
        fenetre.blit(ennemi3.image, ennemi3.rect)
        for i in range(-450, 350, 45):
            fenetre.blit(sol_herbe, (i, 125))
            fenetre.blit(sol_terre, (i + 50, 175))
            fenetre.blit(sol_terre, (i + 50, 205))
            fenetre.blit(sol_terre, (i + 50, 235))
        fenetre.blit(scoreTexte, (550, 40))
        fenetre.blit(levelTexte, (550, 80))
        for tirs in ennemi2.ondesliste:
            fenetre.blit(balle_m,(tirs[0],tirs[1]))
        for tir in tirs_liste:
            if tir[2]:
                fenetre.blit(balle, (tir[0], tir[1]))
            else:
                fenetre.blit(balle2, (tir[0], tir[1]))
            pygame.display.flip()
    if inEndMenu == True:
        fenetre.blit(fondMain, (0, 0))
        fenetre.blit(endtext, (250, 350))
        fenetre.blit(gameover, (220, 100))

    pygame.display.update()


def main(inMenu, inGame, inEndMenu, vie, score, niveau, time, time2 , time3):
    ir = 0
    ig = 0

    run = True
    while run:
        # Tick at n FPS
        dt = clock.tick()
        time += dt
        time2 += dt
        time3 += dt
        # Event handler
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                inMenu = False
                inGame = True
                MouseD = True
            else:
                MouseD = False

            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    joueur.image = pygame.image.load("ImagesHeros/Mulet_1.png")
                if event.key == K_LEFT:
                    joueur.image = pygame.image.load("ImagesHeros/Mulet_G1.png")
                if event.key == K_UP and joueur.sens == True:
                    joueur.image = pygame.image.load("ImagesHeros/Mulet_1.png")
                if event.key == K_UP and joueur.sens == False:
                    joueur.image = pygame.image.load("ImagesHeros/Mulet_G1.png")

            if event.type == pygame.QUIT:
                run = False

        KEYS_PRESSED = pygame.key.get_pressed()

        #       if KEYS_PRESSED[K_RIGHT] and KEYS_PRESSED[K_UP] == False:
        #           joueur.move_right(ir)
        #           ir += 1

        #       if KEYS_PRESSED[K_LEFT] and KEYS_PRESSED[K_UP] == False:
        #           joueur.move_left(ig)
        #           ig += 1

        if KEYS_PRESSED[K_RIGHT]:
            joueur.move_right(ir)
            ir += 1

        if KEYS_PRESSED[K_LEFT]:
            joueur.move_left(ig)
            ig += 1

        #       if event.type == KEYDOWN:

        if KEYS_PRESSED[K_UP]:
            if KEYS_PRESSED[K_LEFT]:
                joueur.move_jump(135.0)
            elif KEYS_PRESSED[K_RIGHT]:
                joueur.move_jump(45.0)
            else:
                joueur.move_jump(90.0)
        #       if KEYS_PRESSED[K_UP]:
        #               joueur.move_jump_init()
        if not(joueur.isJump):
            if KEYS_PRESSED[K_UP]:
                joueur.isJump = True
        else:
            if joueur.jumpcount >= -10:
                joueur.rect.y -= (joueur.jumpcount * abs(joueur.jumpcount)) * 0.3
                joueur.jumpcount -= 1
            else:
                joueur.jumpcount = 10
                joueur.isJump = False
                
        
        #if joueur.rect.y == 0 or KEYS_PRESSED[K_UP] == False:
            #while joueur.rect.y != 100:
                #joueur.rect.y += 1
        #           desc = False
        if joueur.rect.x > ennemi.rect.x-220:
            ennemi.rect.x+=2
        if joueur.rect.x < ennemi.rect.x-220:
            ennemi.rect.x-=2.5
        if joueur.rect.x > ennemi3.rect.x:
            ennemi3.rect.x+=2
        if joueur.rect.x < ennemi3.rect.x:
            ennemi3.rect.x-=2.5
        for tir in ennemi2.ondesliste:
                
            if joueur.rect.x+5>=tir[0] - 330 >=joueur.rect.x-4 and joueur.rect.y+50 >= tir[1] -180 >= joueur.rect.y-50 :
                vie -= 1
        if joueur.rect.x+20 >= ennemi.rect.x >= joueur.rect.x - 20 and joueur.rect.y == ennemi.rect.y - 100:
            vie -= 1
        if vie <= 0:
            inEndMenu = True

        if MouseD == True:
            score = int(score) + 1

        Affscore = 'score '
        Affscore += str(score)

        Afflevel = 'level '
        Afflevel += str(niveau)

        scoreTexte = font.render(Affscore, True, white)
        levelTexte = font.render(Afflevel, True, white)
        
        if time>500 and KEYS_PRESSED[K_SPACE]:
            if joueur.sens:
                tirs_liste.append([joueur.rect.x-4, joueur.rect.y-5, joueur.sens])
            else:
                tirs_liste.append([joueur.rect.x-4, joueur.rect.y-35, joueur.sens])
            time = 0
        for tir in tirs_liste:
            if tir[2]:
                tir[0] += 20
            else:
                tir[0] -= 20
            if 0>tir[0]>700:
                tirs_liste.remove(tir)
        
        if time2 > 2000:
            ennemi2.ondesliste.append([ennemi2.rect.x+115, ennemi2.rect.y+120])
            time2 = 0
        for tir in ennemi2.ondesliste:
            tir[0] -= 6
            if 0>tir[0]>700:
                ennemi2.ondesliste.remove(tir)
        
        if KEYS_PRESSED[pygame.K_ESCAPE]:
            
            run = False

        

        # Call draw function
        draw(inMenu, inGame, inEndMenu, scoreTexte, vie, levelTexte)


# Class sound:
pygame.mixer.init()
pygame.mixer.music.load("Musiques/musiqueJeu.mp3")
pygame.mixer.music.set_volume(3.0)
pygame.mixer.music.play(loops=-1)

if __name__ == '__main__':
    main(inMenu, inGame, inEndMenu, vie, score, niveau,time, time2,time3)
pygame.quit()
