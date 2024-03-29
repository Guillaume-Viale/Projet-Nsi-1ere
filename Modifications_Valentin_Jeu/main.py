# ecrire PIP3 install pygame dans la console
# fenetre de 700p * 500p
# RETRO ADVENTURE
import pygame
import math
from pygame.locals import *
from pygame import mixer
from monstre2 import *
from monstre3 import *
import scripts
#creation de la fenetre de jeu
pygame.init()
fenetre = pygame.display.set_mode((700, 500))



# IMAGE
fond = pygame.image.load("ImagesFond/CielFinal_20.png").convert()
fond1 = pygame.image.load("ImagesFond/VilleBleu.jpg").convert()
fond2 = pygame.image.load("ImagesFond/VilleOrange.png").convert()
# image de fond
fond = pygame.transform.scale(fond, (700, 500))
fond1 = pygame.transform.scale(fond1, (700, 370))
fond2 = pygame.transform.scale(fond2, (700, 370))
fondMain = pygame.image.load("ImagesFond/Accueil.png").convert()
# fond Menu principale
fondMain = pygame.transform.scale(fondMain, (700, 500))
#sols
sol_herbe = pygame.image.load("ImagesFond/pixil-frameHerbe.png").convert_alpha()
sol_terre = pygame.image.load("ImagesFond/TerreFinal700500.png").convert_alpha()
sol_terre = pygame.transform.scale(sol_terre, (675, 482))
sol2 = pygame.image.load("ImagesFond/Pierre.png").convert_alpha()
sol2 = pygame.transform.scale(sol2, (675, 482))
#UI
vie1 = pygame.image.load("ImagesHeros/Coeur_Heros.png").convert_alpha()
vie2 = pygame.image.load("ImagesHeros/CoeurPerduHeros.png").convert_alpha()
#Image de tir
balle = pygame.image.load("ImagesHeros/attaque.png").convert_alpha()
balle2 = pygame.image.load("ImagesHeros/attaque2.png").convert_alpha()
balle_m = pygame.image.load("ImagesAttaques/wifi.png").convert_alpha()
balle_m = pygame.transform.scale(balle_m, (50, 50))
#image des méchants
mechant1 = pygame.image.load("ImagesEnemies/M_Antenne.png").convert_alpha()
mechant2 = pygame.image.load("ImagesEnemies/M_Imprimante.png").convert_alpha()
mechant3 = pygame.image.load("ImagesEnemies/M_Smartphone.png").convert_alpha()
#implementations des classes(autres programmes)
joueur = scripts.Player() #classe qui donne toute les variables lié au jouer + animation du perso
ennemi = scripts.Monstre() #classe qui donne toute les variables liée au monstre1
ennemi2 = Monstre2() #classe qui donne toute les variables liée au monstre2
ennemi3 = Monstre3() #classe qui donne toute les variables liée au monstre3
# variable liée au jeu
temps = 0
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
transition2 = font.render('READY FOR LEVEL 2 ?', True, white)
transition3 = font.render('READY FOR LEVEL 3 ?', True, white)
fin_texte = font.render('WELL PLAYED!', True, white)

# VARIABLE A NE PAS CHANGER
#timers
time = 0
time2 = 0
time3 = 0
#clic droit
MouseD = False
#booléen qui donnent l'état du jeu
inMenu = True
inGame = False
inEndMenu = False
Interlude2 = False
Interlude3 = False
Fin = False
#orientation du perso (droite= True, gauche = false)
state = False
#clock du jeu(ms)
clock = pygame.time.Clock()
#mecanique de tir
tirs_liste = []


def draw(inMenu, inGame, inEndMenu, scoreTexte, vie, levelTexte, niveau, Interlude2, Interlude3, Fin):
    # Menu Principale
    if inMenu:
        fenetre.blit(fondMain, (0, 0))
        fenetre.blit(starttext, (250, 400))
        fenetre.blit(Title, (230, 100))
    if inGame == True:
        # le jeu commence
        #niveau 2
        if niveau % 2 == 0:
            fenetre.blit(fond1, (0, 0))
            fenetre.blit(ennemi2.image, ennemi2.rect)
            for i in range(-450, 450, 45):
                fenetre.blit(sol2, (i, 145))
                fenetre.blit(sol2, (i + 50, 205))
        #niveau 3
        elif niveau % 3 == 0:
            fenetre.blit(fond2, (0, 0))
            fenetre.blit(ennemi3.image, ennemi3.rect)
            for i in range(-450, 450, 45):
                fenetre.blit(sol2, (i, 145))
                fenetre.blit(sol2, (i + 50, 205))
        #niveau 1
        else:
            fenetre.blit(fond, (0, 0))
            fenetre.blit(ennemi.image, ennemi.rect)
            for i in range(-450, 350, 45):
                fenetre.blit(sol_herbe, (i, 125))
                fenetre.blit(sol_terre, (i + 50, 175))
                fenetre.blit(sol_terre, (i + 50, 205))
                fenetre.blit(sol_terre, (i + 50, 235))
        #UI pour la vie du joueur
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
        # tout les elemnts du jeu(sol,perso,ennemis...)
        fenetre.blit(joueur.image, joueur.rect)
        
        
        fenetre.blit(scoreTexte, (550, 40))
        fenetre.blit(levelTexte, (550, 80))
        #Image de tirs (ennemi + joueur)
        if niveau % 2 == 0:
            for tirs in ennemi2.ondesliste:
                fenetre.blit(balle_m, (tirs[0], tirs[1]))
        for tir in tirs_liste:
            if tir[2]:
                fenetre.blit(balle, (tir[0], tir[1]))
            else:
                fenetre.blit(balle2, (tir[0], tir[1]))
            pygame.display.flip()
    # GameOver
    if inEndMenu == True:
        fenetre.blit(fondMain, (0, 0))
        fenetre.blit(endtext, (200, 400))
        fenetre.blit(gameover, (240, 100))
    #Ecrans de transition entre les niveaux:
    if Interlude2 == True and MouseD == False:
        fenetre.blit(fondMain, (0, 0))
        fenetre.blit(transition2, (220, 100))
    if Interlude3 == True:
        fenetre.blit(fondMain, (0, 0))
        fenetre.blit(transition3, (220, 100))
    #écran de fin
    if Fin == True:
        fenetre.blit(fondMain, (0, 0))
        fenetre.blit(fin_texte,(450,200))
        fenetre.blit(scoreTexte,(450,250))
    pygame.display.update()


def main(inMenu, inGame, inEndMenu, vie, temps, niveau, time, time2, time3, Interlude2, Interlude3,Fin):
    ir = 0
    ig = 0
    #boucle principal
    run = True
    while run:
        # necessaire pour le systeme de timer
        dt = clock.tick()
        time += dt #timer tir joueur
        time2 += dt #timer tir ennemi2
        time3 += dt #timer enneli3 (descente)
        if (Fin == False and Interlude3 == False and Interlude2 == False) and inGame:    
            temps +=float(dt) #timer du jeu
        
        # Event handler
        for event in pygame.event.get():
            #sortie du menu avec clic droit
            if pygame.mouse.get_pressed()[0]:
                inMenu = False
                inGame = True
                MouseD = True
            else:
                MouseD = False
            #sortie de l'interlude avec clic droit
            if Interlude2 == True:
               if MouseD:
                   Interlude2 = False 
                   niveau = 2
            #sortie de l'interlude avec clic droit        
            if Interlude3 == True:
               if MouseD:
                   Interlude3 = False
                   niveau = 3
                   MouseD = True
            # regarde si le perso saute et si il va vers la gauche ou droite(Images)
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
        #nom donnée a la liste des touches et leur état
        KEYS_PRESSED = pygame.key.get_pressed()

        # Mouvement a droite
        if KEYS_PRESSED[K_RIGHT] and joueur.rect.x <= 315:
            joueur.move_right(ir)
            ir += 1
        # Mouvement a Gauche
        if KEYS_PRESSED[K_LEFT] and -315 <= joueur.rect.x:
            joueur.move_left(ig)
            ig += 1

        # donne l'image correspondante lorsque le perso saute
        if KEYS_PRESSED[K_UP]:
            if KEYS_PRESSED[K_LEFT]:
                joueur.move_jump(135.0)
            elif KEYS_PRESSED[K_RIGHT]:
                joueur.move_jump(45.0)
            else:
                joueur.move_jump(90.0)
        # regarde si le perso est sur le sol
        if not (joueur.isJump):
            #méthode pour commencer le saut
            if KEYS_PRESSED[K_UP] and (Fin == False and Interlude3 == False and Interlude2 == False) and inGame:
                joueur.isJump = True
                son2 = pygame.mixer.Sound("sons/jump.wav")
                son2.play()
        # methode de saut --> parabole a l'aide d'une fonction polynome
        else:
            if joueur.jumpcount >= -10:
                joueur.rect.y -= (joueur.jumpcount * abs(joueur.jumpcount)) * 0.3
                joueur.jumpcount -= 1
            else:
                joueur.jumpcount = 10
                joueur.isJump = False

        #niveau 1: l'imprimante;  l' ennemie 1 suit le jouer
        if niveau == 1 and inGame:
            
            if joueur.rect.x > ennemi.rect.x - 220:
                ennemi.rect.x += 2
                #le jouer perd de la vie si il touche l'ennemi
                if ennemi.rect.x - 221 <= joueur.rect.x <= ennemi.rect.x - 220 and joueur.rect.y  >= 50 and inGame:
                    vie -= 1
                    
              
            if joueur.rect.x < ennemi.rect.x - 220:
                ennemi.rect.x -= 2
                #le jouer perd de la vie si il touche l'ennemi
                if ennemi.rect.x - 223 <= joueur.rect.x <= ennemi.rect.x - 218 and joueur.rect.y >= 50 and inGame and not(Interlude2):
                    vie -= 1
               
        #niveau 3, le telephone    
        if niveau % 3 == 0:
            #l'ennemi3 suit le joueur
            if joueur.rect.x > ennemi3.rect.x - 120 and ennemi3.attack == False:
                ennemi3.rect.x += 4
                
            if joueur.rect.x < ennemi3.rect.x - 120 and ennemi3.attack == False:
                ennemi3.rect.x -= 4
                
            if joueur.rect.x != ennemi3.rect.x - 120 and ennemi3.attack == False:
                time3 = 0
            #attaque de l'ennemi3
            if ennemi3.rect.x - 20 >= joueur.rect.x >= ennemi3.rect.x - 240 and time3 > 800:
                ennemi3.attack = True
            if ennemi3.attack == True:
                if ennemi3.rect.y <= 140:
                    ennemi3.rect.y += 14
                if ennemi3.rect.y >= 140 and time3 > 2500:
                    ennemi3.rect.y = -115
                    
                    time3 = 0
                    ennemi3.attack=False
            #le jouer perd de la vie
            if ennemi3.rect.x-125<= joueur.rect.x<= ennemi3.rect.x-115 and ennemi3.rect.y-45<=joueur.rect.y<=ennemi3.rect.y-35 and not(Interlude3):
                vie-=1

        #niveau 2: l'antenne; systeme de dégat de tir pour l'ennemi n2
        if niveau % 2 == 0:
            #systeme de degats pour le tir
            for tir in ennemi2.ondesliste:

                if joueur.rect.x + 5 >= tir[0] - 330 >= joueur.rect.x - 4 and joueur.rect.y + 50 >= tir[
                1] - 180 >= joueur.rect.y - 50 and not(Interlude3)and not(Interlude2):
                    vie -= 1
        #les degats sur les ennemis créer par le joueur    
        for tir in tirs_liste:
            if niveau % 2 == 0:
                if ennemi2.rect.x + 10 >= tir[0] + 115 >= ennemi2.rect.x - 10 and ennemi2.rect.y + 50 >= tir[
                1] + 60 >= ennemi2.rect.y - 90:
                    ennemi2.health -= 25
            elif niveau % 3 == 0:
                if ennemi3.rect.x + 10 >= tir[0] + 115 >= ennemi3.rect.x - 10 and ennemi3.rect.y + 50 >= tir[
                1] + 60 >= ennemi3.rect.y - 90:
                    ennemi3.health -= 25
            else:
                if ennemi.rect.x + 10 >= tir[0] +220 >= ennemi.rect.x - 10 and ennemi.rect.y + 50 >= tir[
                1] + 60 >= ennemi.rect.y - 90:
                    ennemi.health -= 25
        # GameOver
        if vie <= 0:
            inEndMenu = True
        
        
        #l'imprimante est detruite
        if ennemi.isDead == True:
            ennemi.rect.y += 600
            
            if niveau == 1:
                Interlude2 = True
            #niveau = 2
        #l'antenne est detruite
        if ennemi2.isDead == True:
            ennemi2.rect.y += 600
            
            if niveau == 2:
                Interlude3 = True
            #niveau = 3
        #le télephone estdetruit
        if ennemi3.isDead == True:
            ennemi3.rect.y += 600
            
            Fin = True
        # ecrit le temps et le niveau
        Affscore = 'time: '
        Affscore += str(temps/1000)  #temps en seconde

        Afflevel = 'level: '
        Afflevel += str(niveau)

        scoreTexte = font.render(Affscore, True, white)
        levelTexte = font.render(Afflevel, True, white)

        # systeme de tir du perso, 2fois par seconde
        if time > 500 and KEYS_PRESSED[K_SPACE] and (Fin == False and Interlude3 == False and Interlude2 == False) and inGame:
            if joueur.sens:
                tirs_liste.append([joueur.rect.x - 4, joueur.rect.y - 5, joueur.sens])
                joueur.image = pygame.image.load("ImagesHeros/TIR.png")
            else:
                tirs_liste.append([joueur.rect.x - 4, joueur.rect.y - 35, joueur.sens])
                joueur.image = pygame.image.load("ImagesHeros/TIR2.png")
            time = 0
            son = pygame.mixer.Sound("sons/laserShoot.wav")
            son.play()
        for tir in tirs_liste:
            if tir[2]:
                tir[0] += 20
            else:
                tir[0] -= 20
            if -350> tir[0] or 350<tir[0]:
                tirs_liste.remove(tir)
        # systeme de tir pour le mechant 2
        if time2 > 900 and ennemi2.isDead == False and niveau == 2:
                ennemi2.ondesliste.append([ennemi2.rect.x + 115, ennemi2.rect.y + 120])
                time2 = 0
        for tir in ennemi2.ondesliste:
            tir[0] -= 5
            if 0> tir[0] or 815<tir[0]:
                ennemi2.ondesliste.remove(tir)
        #systeme de mort pour les méchants
        if ennemi.health <= 0:
            ennemi.isDead = True
            
        if ennemi2.health <= 0:
            ennemi2.isDead = True
           
        if ennemi3.health <= 0:
            ennemi3.isDead = True
            
        
        
        if KEYS_PRESSED[pygame.K_ESCAPE]:
            run = False

        # Call draw function
        draw(inMenu, inGame, inEndMenu, scoreTexte, vie, levelTexte, niveau, Interlude2, Interlude3,Fin)


# Class sound:
pygame.mixer.init()
pygame.mixer.music.load("Musiques/musiqueJeu.mp3")
pygame.mixer.music.set_volume(3.0)
pygame.mixer.music.play(loops=-1)

if __name__ == '__main__':
    main(inMenu, inGame, inEndMenu, vie, temps, niveau, time, time2, time3, Interlude2, Interlude3,Fin)
pygame.quit()
