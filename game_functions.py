import pygame

class GameFunctions():
  def __init__(self, game):
    self.settings = game.settings
    self.pacman = game.pacman
    self.blinky = game.blinky
    self.ghosts = game.ghosts

  def gameover(self):
    pygame.quit()

  def reset(self):
    print('ressetting!!')
    print('lives: ', self.settings.lives)
    if not self.settings.game_over:
      #ghosts
      self.blinky.x_pos = 56
      self.blinky.y_pos = 58
      self.blinky.blinky_direction = 0
      self.ghosts.eaten_ghost = [False, False, False, False]
      self.blinky.blinky_dead = False
      #pacman
      self.pacman.direction = 0
      self.pacman.direction_command = 0
      self.pacman.poweredup = False
      self.pacman.pac_x, self.pacman.pac_y = self.pacman.start_pos, self.pacman.end_pos
      #settings
      self.settings.lives -= 1
      # self.settings.game_over = False
      self.settings.moving = True
      self.settings.startup_counter = 0
      self.settings.powerup = False
      self.settings.power_counter = 0
      self.settings.reset = False
    else:
      self.gameover()
