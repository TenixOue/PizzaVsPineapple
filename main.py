import pygame
from random import *
from game import *
from mob import *



pygame.init()

running = True


#initialise une fenetre
pygame.display.set_caption(("Pizza Steve Defenders "))

programIcon = pygame.image.load('assets/mob.png')
pygame.display.set_icon(programIcon)

screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets\cul.jpg')



game = game()
#musique  
#pygame.mixer.music.load("assets\pleure.mp3")
#pygame.mixer.music.play(loops = -1 )

#boucle qui s"execute si True
while running:

    #inject le background a l'ecran
    screen.blit(background,(0,0))

    #met le joueur a l'ecrant
    screen.blit(game.player.image,game.player.rect)
    
    for arrow in game.player.all_arrow:
        arrow.movement()

    
    #deplacement mob
    
    for monster in game.all_monster:
        monster.avancer()
        monster.update_HP(screen)
    
    #projectile 
    game.player.all_arrow.draw(screen)
    
    #mob
    
    game.all_monster.draw(screen)

    #fait le deplacement 
    if game.pressed.get(pygame.K_d) and game.player.rect.x + 125 < screen.get_width():
        game.player.move_right() 
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_z) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(pygame.K_s) and game.player.rect.y  < 550:
        game.player.move_down()



    #actualise la fenetre
    pygame.display.flip()
   
    #si joueur ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running == False
            pygame.quit()
            print("jeu fermer")
    #detection action 
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            if event.key == pygame.K_SPACE:
                game.player.launch()
        
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False 
        