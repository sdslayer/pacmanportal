import pygame
from pygame.sprite import Sprite

class Ghost(Sprite):
    def __init__(self, game, x_coord, y_coord, target, 
                 speed, img, direct, dead, box, id):
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 22
        self.center_y = self.y_pos + 22
        self.target = target
        self.speed = speed
        self.img = img
        self.in_box = box
        self.id = id
        self.turns, self.in_box = self.check_collisions()
        self.rect = self.draw()


    def draw(self):
        if (not powerup and not self.dead) or (eaten_ghost[self.id]
                                               and powerup and not self.dead):
            screen.blit(self.img, (self.x_pos, self.y_pos))
        elif powerup and not self.dead and not eaten_ghost[self.id]:
            screen.blit(spooked_img, (self.x_pos, self.y_pos))
        else:
            screen.blit(dead_img, (self.x_pos, self.y_pos))
        ghost_Rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
        return ghost_rect
    
    def check_collisons(self):
        pass
        return self.turns, self.in_box

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('insert ghost sprite')
        self.rect = self.image.get_rect()

        self.GHOST_FRAME_DURATION = 5
        self.current_frame = 0
        self.frame_counter = 0

        PACMAN = pygame.Rect(30, 30, 60, 60)

        # blinky_img = pygame.transform.scale(pygame.image.load(insert png sprite))
        # pinky_img = pygame.transform.scale(pygame.image.load(insert png sprite))
        # inky_img = pygame.transform.scale(pygame.image.load(insert png sprite))
        # clyde_img = pygame.transform.scale(pygame.image.load(insert png sprite))
        # spooked_img = pygame.transform.scale(pygame.image.load(insert png sprite))
        # dead_ghost_img = pygame.transform.scale(pygame.image.load(insert png sprite))
        
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

       
        eaten_ghost = [False, False, False, False]
        targets = [(player_x, player_y), (player_x, player_y), (player_x, player_y), (player_x, player_y)] #targets player's
        blinky_dead = False #tracks if they're dead
        pinky_dead = False
        inky_dead = False
        clyde_dead = False

        blinky_box = False # tracks if they're inside the box 
        pinky_box = False
        inky_box = False
        clyde_box = False
        ghost_speed = 2