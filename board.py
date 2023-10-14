import pygame
from gameboard import board
from math import pi as PI

class Board:
  def __init__(self, game):
    self.settings = game.settings
    self.color = (33,33,255)
    self.level = board
    self.screen = game.screen #this is how we will call the screen instead of WIN

  def draw_level(self):
      pieceheight = ((self.settings.screen_height - 50) // 32)
      piecewidth = (self.settings.screen_width // 30)
      for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                if self.level[i][j] == 1:
                      pygame.draw.circle(self.screen, 'white', (j * piecewidth + (0.5 * piecewidth), (i * pieceheight + (0.5 * pieceheight))), 4) # Draw small pellet
                if self.level[i][j] == 2:
                      pygame.draw.circle(self.screen, 'white', (j * piecewidth + (0.5 * piecewidth), (i * pieceheight + (0.5 * pieceheight))), 12) # Draw big pellet
                if self.level[i][j] == 3:
                  pygame.draw.line(self.screen, self.color, (j * piecewidth + (0.5 * piecewidth), i * pieceheight), (j * piecewidth + (0.5 * piecewidth), i * pieceheight + pieceheight), 3)
                if self.level[i][j] == 4:
                   pygame.draw.line(self.screen, self.color, (j * piecewidth, i * pieceheight + (0.5 * pieceheight)),
                                 (j * piecewidth + piecewidth, i * pieceheight + (0.5 * pieceheight)), 3)
                if self.level[i][j] == 5:
                    pygame.draw.arc(self.screen, self.color, [(j * piecewidth - (piecewidth * 0.4)) - 2, (i * pieceheight + (0.5 * pieceheight)), piecewidth, pieceheight],
                                0, PI / 2, 3)
                if self.level[i][j] == 6:
                    pygame.draw.arc(self.screen, self.color,
                                    [(j * piecewidth + (piecewidth * 0.5)), (i * pieceheight + (0.5 * pieceheight)), piecewidth, pieceheight], PI / 2, PI, 3)
                if self.level[i][j] == 7:
                    pygame.draw.arc(self.screen, self.color, [(j * piecewidth + (piecewidth * 0.5)), (i * pieceheight - (0.4 * pieceheight)), piecewidth, pieceheight], PI,
                                    3 * PI / 2, 3)
                if self.level[i][j] == 8:
                    pygame.draw.arc(self.screen, self.color,
                                    [(j * piecewidth - (piecewidth * 0.4)) - 2, (i * pieceheight - (0.4 * pieceheight)), piecewidth, pieceheight], 3 * PI / 2,
                                    2 * PI, 3)
                if self.level[i][j] == 9:
                    pygame.draw.line(self.screen, 'white', (j * piecewidth, i * pieceheight + (0.5 * pieceheight)),
                                    (j * piecewidth + piecewidth, i * pieceheight + (0.5 * pieceheight)), 3)

  def update(self):
    self.draw_level()
