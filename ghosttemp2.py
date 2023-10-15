import pygame
from pygame.sprite import Sprite
import copy


class Ghost(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.level = game.board.level

        self.image = pygame.image.load()
        self.rect = self.image.get_rect()

        self.turns, self.in_box = self.check_collisions()
    


class Pinky(Ghost):
    pinky_img = [pygame.transform.scale(pygame.image.load(f'images/ghost_images/pink.png'), (45, 45))]
    pass



