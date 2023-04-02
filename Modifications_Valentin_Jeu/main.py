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
fond1 = pygame.image.load("ImagesFond/VilleBleu.jpg").convert()
fond2 = pygame.image.load("ImagesFond/VilleOrange.png").convert()
#image de fond
fond = pygame.transform.scale(fond, (700, 500))
fond1 = pygame.transform.scale(fond1, (700, 370))
fond2 = pygame.transform.scale(fond2, (700, 370))
fondMain = pygame.image.load("ImagesFond/Accueil.png").convert()
#fond Menu principale
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


def draw(inMenu, inGame, inEndMenu, scoreTexte, vie, levelTexte,niveau):
    # Menu Principale
    if inMenu:
        fenetre.blit(fondMain, (0, 0))
        fenetre.blit(starttext, (230, 400))
        fenetre.blit(Title, (230, 100))
    if inGame == True:
        #le jeu commence
        if niveau%2 == 0:    
            fenetre.blit(fond1, (0, 0))
        elif niveau%3 == 0:
            fenetre.blit(fond2, (0, 0))
        else:
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
        #tout les elemnts du jeu(sol,perso,ennemis...)   
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
        #rendement graphique des tirs
        for tirs in ennemi2.ondesliste:
            fenetre.blit(balle_m,(tirs[0],tirs[1]))
        for tir in tirs_liste:
            if tir[2]:
                fenetre.blit(balle, (tir[0], tir[1]))
            else:
                fenetre.blit(balle2, (tir[0], tir[1]))
            pygame.display.flip()
    #GameOver
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
        # necessaire pour le systeme de timer
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

            #regarde si le perso saute et si il va vers la gauche ou droite(Images)
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

       
        #Mouvement a droite
        if KEYS_PRESSED[K_RIGHT] and joueur.rect.x<=315:
            joueur.move_right(ir)
            ir += 1
        #Mouvement a Gauche
        if KEYS_PRESSED[K_LEFT] and -315<=joueur.rect.x:
            joueur.move_left(ig)
            ig += 1

        
        #donne l'image correspondante lorsque le perso saute
        if KEYS_PRESSED[K_UP]:
            if KEYS_PRESSED[K_LEFT]:
                joueur.move_jump(135.0)
            elif KEYS_PRESSED[K_RIGHT]:
                joueur.move_jump(45.0)
            else:
                joueur.move_jump(90.0)
        #regarde si le perso est sur le sol
        if not(joueur.isJump):
            if KEYS_PRESSED[K_UP]:
                joueur.isJump = True
                son2 = pygame.mixer.Sound("jump.wav")
                son2.play()
        #methode de saut --> parabole a l'aide d'une fonction polynome
        else:
            if joueur.jumpcount >= -10:
                joueur.rect.y -= (joueur.jumpcount * abs(joueur.jumpcount)) * 0.3
                joueur.jumpcount -= 1
            else:
                joueur.jumpcount = 10
                joueur.isJump = False
                
        
        #les ennemies 1 et 3 suivent le perso
        if joueur.rect.x > ennemi.rect.x-220:
            ennemi.rect.x+=2
        if joueur.rect.x < ennemi.rect.x-220:
            ennemi.rect.x-=2
        if joueur.rect.x > ennemi3.rect.x-120 and ennemi3.attack == False:
            ennemi3.rect.x+=4
        if joueur.rect.x < ennemi3.rect.x-120 and ennemi3.attack == False:
            ennemi3.rect.x-=4
        
        if joueur.rect.x != ennemi3.rect.x-120 and ennemi3.attack == False:
            time3 = 0
            
        if ennemi3.rect.x-123 <= joueur.rect.x <=ennemi3.rect.x-117 and time3>1500:
            ennemi3.attack = True
        if ennemi3.attack == True:
            if ennemi3.rect.y <= 140:
                ennemi3.rect.y+=14
            if ennemi3.rect.y >= 140 and time3>3000:
                ennemi3.rect.y = -115
                time3 = 0
                ennemi3.attack = False

            
            
            
            
                
                
        #systeme de dégat de tir pour l'ennemi n2
        for tir in ennemi2.ondesliste:
                
            if joueur.rect.x+5>=tir[0] - 330 >=joueur.rect.x-4 and joueur.rect.y+50 >= tir[1] -180 >= joueur.rect.y-50 :
                vie -= 1
        for tir in tirs_liste:
                
            if ennemi2.rect.x+5>=tir[0] + 115 >=ennemi2.rect.x-5 and ennemi2.rect.y+50 >= tir[1] +60 >= ennemi2.rect.y-60 :
                ennemi2.health -=50
            if ennemi.rect.x+5>=tir[0] + 216 >=ennemi.rect.x-4 and ennemi.rect.y+50 >= tir[1] +45 >= ennemi.rect.y-50 :
                ennemi.health -=25
            if ennemi3.rect.x+5>=tir[0] + 115 >=ennemi3.rect.x-4 and ennemi3.rect.y+50 >= tir[1] +60 >= ennemi3.rect.y-50 :
                ennemi3.health -=34
        #GameOver
        if vie <= 0:
            inEndMenu = True
        #systeme de score(a changer)
        if MouseD == True:
            score = int(score) + 1
        if ennemi.isDead == True:
            score = int(score) + 1

        if ennemi2.isDead == True:
            score = int(score) + 1
        if ennemi3.isDead == True:
            score = int(score) + 1
        #ecrit le score et le niveau
        Affscore = 'score '
        Affscore += str(score)

        Afflevel = 'level '
        Afflevel += str(niveau)

        scoreTexte = font.render(Affscore, True, white)
        levelTexte = font.render(Afflevel, True, white)
        
        #systeme de tir du perso, 2fois par seconde
        if time>500 and KEYS_PRESSED[K_SPACE]:
            if joueur.sens:
                tirs_liste.append([joueur.rect.x-4, joueur.rect.y-5, joueur.sens])
            else:
                tirs_liste.append([joueur.rect.x-4, joueur.rect.y-35, joueur.sens])
            time = 0
            son = pygame.mixer.Sound("laserShoot.wav")
            son.play()
        for tir in tirs_liste:
            if tir[2]:
                tir[0] += 20
            else:
                tir[0] -= 20
            if 0>tir[0]>700:
                tirs_liste.remove(tir)
        #systeme de tir pour le mechant 2
        if time2 > 2000 and ennemi2.isDead == False:
            ennemi2.ondesliste.append([ennemi2.rect.x+115, ennemi2.rect.y+120])
            time2 = 0
        for tir in ennemi2.ondesliste:
            tir[0] -= 6
            if 0>tir[0]>700:
                ennemi2.ondesliste.remove(tir)
        if ennemi.health <= 0:
            ennemi.isDead = True
        if ennemi2.health <= 0:
            ennemi2.isDead = True
        if ennemi3.health <= 0:
            ennemi3.isDead = True
       
        if ennemi.isDead and ennemi2.isDead and ennemi3.isDead:
            niveau = niveau + 1
            ennemi.isDead = False
            ennemi.health = ennemi.max_health
            ennemi2.isDead = False
            ennemi2.health = ennemi2.max_health
            ennemi3.isDead = False
            ennemi3.health = ennemi3.max_health
        if KEYS_PRESSED[K_l]:
            niveau = niveau+1
        if KEYS_PRESSED[pygame.K_ESCAPE]:
            
            run = False

        

        # Call draw function
        draw(inMenu, inGame, inEndMenu, scoreTexte, vie, levelTexte,niveau)


# Class sound:  
pygame.mixer.init()
pygame.mixer.music.load("Musiques/musiqueJeu.mp3")
pygame.mixer.music.set_volume(3.0)
pygame.mixer.music.play(loops=-1)

if __name__ == '__main__':
    main(inMenu, inGame, inEndMenu, vie, score, niveau,time, time2,time3)
pygame.quit()
