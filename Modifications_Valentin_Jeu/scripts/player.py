import pygame
import math
#from scripts.attaquesDistance import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 6
        self.jump_velocity = 10 # La vitesse de saut
        self.jump_time = 0 
        self.angle = 0.0
        self.jumpaction=False
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("ImagesHeros/pixil-frameStatique1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 100
        self.sens=True
        self.isJump = False
        self.jumpcount = 10

    #i peut être un entier quelconque
    def move_right(self,i):
        i = i % 4
# mais sici on stocke dans i le reste de la divsion de i par 4 donc i ne varie que entre 0, 1, 2 et 3
        NameImage = "ImagesHeros/Mulet_"
        NameImage += str(i+1)
# on met la veleur i+1 au bout du fichier 
        NameImage += ".png"
        self.image = pygame.image.load(NameImage)
        self.rect.x+=self.velocity
        self.sens=True


       
    def move_left(self,i):
        i = i % 4
        NameImage = "ImagesHeros/Mulet_G"
        NameImage += str(i+1)
        NameImage += ".png"
        self.image = pygame.image.load(NameImage)
        self.rect.x-=self.velocity
        self.sens=False

    def move_jump_init(self):
        self.rect.y -= self.jump_velocity

    def move_jump(self,angle):
 #       if self.rect.y == 100:
        if angle > 90:
            self.image = pygame.image.load("ImagesHeros/Mulet_G3.png")
        elif angle < 90:
            self.image = pygame.image.load("ImagesHeros/Mulet_3.png")
        else:    
            if self.sens:
                self.image = pygame.image.load("ImagesHeros/Mulet_3.png")
            else:
                self.image = pygame.image.load("ImagesHeros/Mulet_G3.png")
 #       while self.rect.y <= 0:
        #self.rect.y -= self.jump_velocity
 #       while self.rect.y <= 100:
 #           self.rect.y += self.jump_velocity

  #      t=0.0
  #      tampon = self.rect.x
  #      while t<=2.0:
 #           print(t)
  #          self.rect.y = 100.0*t*t-200*math.sin(angle*math.pi/180.0)*t+100        
  #          self.rect.x = 200.0*math.cos(angle*math.pi/180.0)*t + tampon
  #          print(self.rect.y)
  #          t += 0.1



        



    #def launch_projectile(self):
        #creer nouvelle instance de la classe projectile
        #self.all_projectiles.add(Projectile())

