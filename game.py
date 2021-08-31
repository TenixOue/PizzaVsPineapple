import pygame
from player import player
from mob import mob

class game:
    def __init__(self):

        self.player = player(self)
        self.all_player = pygame.sprite.Group()
        self.all_player.add(self.player)
        self.pressed = {}
        self.score = 0
        self.all_monster = pygame.sprite.Group()
        self.spawner()
        self.spawner()

   
    def update(self, screen):
        myfont = pygame.font.SysFont("monospace", 16)
        score_display = myfont.render(f"score: {self.score}" ,1 , (0,0,0) )
        screen.blit(score_display, (100, 100))


    def spawner(self):
        monster = mob(self)
        self.all_monster.add(monster)
   
    def check_collision(self , sprite, group):
        return pygame.sprite.spritecollide(sprite , group, False, pygame.sprite.collide_mask )
  
