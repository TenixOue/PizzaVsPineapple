import pygame

class player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 250
        self.max_health = 250
        self.attack = 40
        self.all_arrow = pygame.sprite.Group()
        self.velocity = 2
        self.image = pygame.image.load('assets/sprite.png')
        self.rect = self.image.get_rect()
        self.image =  pygame.transform.scale(self.image,(125, 179))
        self.rect.x = 500
        self.rect.y = 500
    
    def launch(self):

        self.all_arrow.add(arrow())    
    
    def move_right(self):
        self.rect.x += self.velocity   
    def move_left(self):
        self.rect.x -= self.velocity
    def move_up(self):
        self.rect.y -= self.velocity
    def move_down(self):
        self.rect.y += self.velocity


class game:
    def __init__(self):
        self.player = player()
        self.pressed = {}


class arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 3 
        self.image = pygame.image.load('assets/arrow.png')
        self.rect = self.image.get_rect()



pygame.init()

running = True


#initialise une fenetre
pygame.display.set_caption(("LE G@MING "))

screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets\cover2.jpg')


game = game()
#musique  
#pygame.mixer.music.load("assets\SOUND.mp3")
#pygame.mixer.music.play(loops = -1 )

#boucle qui s"execute si True
while running :

    #inject le background a l'ecran
    screen.blit(background,(-300,-100))

    #met le joueur a l'ecrant
    screen.blit(game.player.image,game.player.rect)

    #projectile 
    game.player.all_arrow.draw(screen)
    
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
