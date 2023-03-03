from player import *
from monstre import *


class Chill:

    def __init__(self):
        self.player = Player(self)
        #groupe de monstre
        self.all_monstre = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monstre()

    
    def spawn_monstre(self):
        monstre = Monstre()
        self.all_monstres.add(monstre)