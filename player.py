import pygame
from arrow import *

class player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 250
        self.max_health = 250
        self.dps = 60
        self.armor = 20
        self.all_arrow = pygame.sprite.Group()
        self.velocity = 6
        self.image = pygame.image.load('assets/sprite2.png')
        self.rect = self.image.get_rect()
        self.image =  pygame.transform.scale(self.image,(125, 179))
        self.rect.x = 500
        self.rect.y = 500
    
    def launch(self):

        self.all_arrow.add(arrow(self))    
    
    def move_right(self):
        
        self.rect.x += self.velocity   
    def move_left(self):
        self.rect.x -= self.velocity
    def move_up(self):
        self.rect.y -= self.velocity
    def move_down(self):
        self.rect.y += self.velocity
    



