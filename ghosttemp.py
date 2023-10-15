import pygame
from pygame.sprite import Sprite
from pacman import Pacman

for i in range(4):
    # blinky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/red.png'), (45, 45))
    pinky_img = pygame.transform.scale(pygame.image.load(f'images/ghost_images/pink.png'), (45, 45))
# inky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/blue.png'), (45, 45))
# clyde_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/orange.png'), (45, 45))
# spooked_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/powerup.png'), (45, 45))
# dead_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/dead.png'), (45, 45))


blinky_x = 56 # starting positions outside of the box
blinky_y = 58 # starting positions outside of the box
blinky_direction = 0

pinky_x = 440 # starting positions inside of the box
pinky_x_y = 338 # starting positions inside of the box
pinky_direction = 2 # direction for them to go up

inky_x = 440
inky_y = 438
inky_direction = 2

clyde_x = 440
clyde_y = 438
clyde_direction = 2

counter = 0
flicker = False

eaten_ghost = [False, False, False, False]
# targets = [(Pacman.self.pac_x, Pacman.self.pac_y), (Pacman.self.pac_x, Pacman.self.pac_y), 
#             (Pacman.self.pac_x, Pacman.self.pac_y), (Pacman.self.pac_x, Pacman.self.pac_y)] #targets player's

blinky_dead = False #tracks if they're dead
pinky_dead = False
inky_dead = False
clyde_dead = False

blinky_box = False # tracks if they're inside the box
pinky_box = False
inky_box = False
clyde_box = False
moving = False
ghost_speed = 2

class Ghosts(Sprite):
    def __init__(self, game, x_coord, y_coord, target, 
                 speed, img, direct, dead, box, id): # I added game
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 22
        self.center_y = self.y_pos + 22
        self.target = target
        self.speed = speed 
        self.img = img
        self.direction = direct
        self.dead = dead
        self.in_box = box
        self.id = id
        self.turns, self.in_box = self.check_collisions()
        self.rect = self.img.get_rect() # outline of ghost collison box
        
        self.screen = game.screen
        self.level = game.board.level
    
    def drawghost(self):
        if True:
           self.screen.blit(self.img, (self.x_pos, self.y_pos))
        return 
