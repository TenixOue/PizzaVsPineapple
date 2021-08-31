import pygame
from player import *

class arrow(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 6
        self.player = player
        self.image = pygame.image.load('assets/arrow.png')
        self.image = pygame.transform.scale(self.image , (50, 50))
        self.rect = self.image.get_rect() 
        self.rect.x = player.rect.x + 50 
        self.rect.y = player.rect.y
    

    
    

    def remove(self):
        self.player.all_arrow.remove(self)

    def movement(self):
        
        self.rect.y -= self.velocity
        for monster in self.player.game.check_collision(self,self.player.game.all_monster):
            self.remove()
            monster.damage(self.player.dps)
            
            
        if self.rect.y < 0 :
            self.remove()
            print("suppr")