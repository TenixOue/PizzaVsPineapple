import pygame 
from random import randint


class mob(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 120
        self.max_health = 120
        self.attack = 30 
        self.velocity = randint(1, 5)
        self.image = pygame.image.load('assets/mob_drip.png')
        self.rect = self.image.get_rect()
        self.image =  pygame.transform.scale(self.image,(125, 179))
        self.rect.x = randint(500, 1000)
        print(self.rect.x)
    
    def damage(self, dps):
        self.health -= dps 
        
        if self.health <= 0:
            self.rect.x = randint(500, 1000)
            self.rect.y = -200
            self.velocity = randint(1, 2)
            self.health = self.max_health
            self.game.score += 30

    def respawn(self):
        if self.rect.y >= 720:
            self.rect.x = randint(500, 1000)
            self.rect.y = -200     
    
    def avancer(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.y += self.velocity
        if self.rect.y >= 720:
            self.rect.x = randint(500, 1000)
            self.rect.y = -200     
    
    
    def update_HP(self, surface):
        color_bar = (246, 82, 82)
        back_bar_color = (128, 128, 128)
        bar_position = [self.rect.x +5 , self.rect.y -15 , self.health , 4]
        back_bar = [self.rect.x +5 , self.rect.y -15 , self.max_health , 4]
        pygame.draw.rect(surface, back_bar_color , back_bar)
        pygame.draw.rect(surface, color_bar,bar_position)

        self.max_health