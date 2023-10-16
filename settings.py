import pygame

class Settings():
  def __init__(self):
    self.screen_width, self.screen_height = 900, 950
    self.bg_color = (0,0,0)
    self.FPS = 60
    self.SPEED = 3
    self.FONT = pygame.font.Font('emulogic.ttf', 20)
    self.poweredup_time = 10000
    self.startup_time = 5500

    #alien settings
    self.blinky_x = 56
    self.blinky_y = 58
    self.blinky_direction = 0
    self.inky_x = 440
    self.inky_y = 388
    self.inky_direction = 2
    self.pinky_x = 440
    self.pinky_y = 438
    self.pinky_direction = 2
    self.clyde_x = 440
    self.clyde_y = 438
