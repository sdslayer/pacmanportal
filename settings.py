import pygame

class Settings():
  def __init__(self):
    self.screen_width, self.screen_height = 900, 950
    self.bg_color = (0,0,0)
    self.FPS = 60
    self.SPEED = 3
    self.FONT = pygame.font.Font('emulogic.ttf', 20)
    