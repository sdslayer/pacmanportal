import pygame
from pygame.sprite import Sprite
import copy

class Pacman(Sprite):
  def __init__(self, game, bportal, oportal):
    super().__init__()
    self.screen = game.screen
    self.settings = game.settings
    self.screen_rect = game.screen.get_rect()
    self.scoreboard = game.scoreboard
    self.level = game.board.level
    self.bportal = bportal
    self.oportal = oportal
    #load the pacman image
    self.image = pygame.image.load('images/player_images/0.png')
    self.rect  = self.image.get_rect()

    self.start_pos, self.end_pos = 900, 0


    #pacman animation settings
    self.PACMAN_FRAME_DURATION = 5  # Number of game frames to display each frame
    self.current_frame = 0
    self.frame_counter = 0
    # R, D, L, R
    self.poweredup = False
    self.started = False
    self.turns_allowed = [False, False, False, False]
    self.direction = 0  # 0: left, 1: right, 2: up, 3: down
    self.direction_command = 0
    self.pac_x_menu, self.pac_y_menu = 0, 500
    self.pac_x, self.pac_y = 450, 663
    self.center_x = self.pac_x + 22
    self.center_y = self.pac_y + 22

    self.pacman_frames = []
    for i in range(4):
        frame_path = f'images/player_images/{i}.png' # Path to the frames
        pacman_frame = pygame.image.load(frame_path).convert_alpha() # Load the frames
        pacman_frame = pygame.transform.scale(pacman_frame, (40, 40)) # Resize pacman frames
        self.pacman_frames.append(pacman_frame) # Add each resized frame to the array

    self.pacman = pygame.Rect(30, 30, 60, 60) # Draw pacman rectangle

  def update_pacman_frame(self):
      self.frame_counter += 1 # Increase frame counter (how long its been on screen for)
      if self.frame_counter >= self.PACMAN_FRAME_DURATION: # If frame counter > max length of a frame...
          self.frame_counter = 0 # Set frame counter to 0
          self.current_frame = (self.current_frame + 1) % len(self.pacman_frames) # Set the next frame
      # print('Current Frame: ', self.frame_counter)

  # def check_collisions(self):
  #   centerx, centery = self.pac_x + 23, self.pac_y + 24
  #   pieceheight = ((self.settings.screen_height - 50) // 32)
  #   piecewidth = (self.settings.screen_width // 30)
  #   if 0 < self.pac_x < 870:
  #     if self.level[centery // pieceheight][centerx // piecewidth] == 1:
  #       self.level[centery // pieceheight][centerx // piecewidth] = 0 #clear the pellet
  #       self.scoreboard.update_score(10)

  def check_collisions(self):
    centerx, centery = self.pac_x + 23, self.pac_y + 24
    pieceheight = ((self.settings.screen_height - 50) // 32)
    piecewidth = (self.settings.screen_width // 30)
    self.poweredup = False
    if 0 < self.pac_x < 870:
      if self.level[centery // pieceheight][centerx // piecewidth] == 1:
        self.level[centery // pieceheight][centerx // piecewidth] = 0 #clear the pellet
        self.scoreboard.update_score(10)
      if self.level[centery // pieceheight][centerx // piecewidth] == 2:
        self.level[centery // pieceheight][centerx // piecewidth] = 0 #clear the pellet
        self.poweredup = True
        self.scoreboard.update_score(50)

  def check_pos(self):
    # print('directon: ', self.direction)
    centerx, centery = self.pac_x + 23, self.pac_y + 24
    turns = [False, False, False, False]
    self.turns_allowed = turns
    # print('turns 1: ', turns[0], turns[1], turns[2], turns[3])
    pieceheight = ((self.settings.screen_height - 50) // 32)
    piecewidth = (self.settings.screen_width // 30)
    padding = 15
    #check collisions based on the center of the player +/- the padding
    if centerx // 30 < 29:
      if self.direction == 0:
        if self.level[centery//pieceheight][(centerx + padding) // piecewidth] < 3:
          turns[0] = True
      if self.direction == 1:
        if self.level[centery//pieceheight][(centerx - padding) // piecewidth] < 3:
          turns[1] = True
      if self.direction == 2:
        if self.level[(centery + padding) //pieceheight][centerx // piecewidth] < 3:
          turns[3] = True
      if self.direction == 3:
        if self.level[(centery - padding) //pieceheight][(centerx - padding) // piecewidth] < 3:
          turns[2] = True

      if self.direction == 2 or self.direction == 3:
        if 12 <= centerx % piecewidth <= 18:
          if self.level[(centery + padding) // pieceheight][centerx // piecewidth] < 3:
            turns[3] = True
          if self.level[(centery - padding) // pieceheight][centerx // piecewidth] < 3:
            turns[2] = True
        if 12 <= centery % pieceheight <= 18:
          if self.level[centery // pieceheight][(centerx - piecewidth)// piecewidth] < 3:
            turns[1] = True
          if self.level[centery // pieceheight][(centerx + piecewidth)// piecewidth] < 3:
            turns[0] = True

      if self.direction == 0 or self.direction == 1:
        if 12 <= centerx % piecewidth <= 18:
          if self.level[(centery + pieceheight) // pieceheight][centerx // piecewidth] < 3:
            turns[3] = True
          if self.level[(centery - pieceheight) // pieceheight][centerx // piecewidth] < 3:
            turns[2] = True
        if 12 <= centery % pieceheight <= 18:
          if self.level[centery//pieceheight][(centerx + padding)// piecewidth] < 3:
            turns[0] = True
          if self.level[centery//pieceheight][(centerx - padding)// piecewidth] < 3:
            turns[1] = True
    else:
      turns[0] = True
      turns[1] = True

    self.turns_allowed = turns
    # print('turns: ', turns[0], turns[1], turns[2], turns[3])

  def move_pac(self):
    #R, L, U, D
    if self.direction == 0 and self.turns_allowed[0]:
      self.pac_x += self.settings.SPEED
    elif self.direction == 1 and self.turns_allowed[1]:
      self.pac_x -= self.settings.SPEED
    if self.direction == 2 and self.turns_allowed[2]:
      self.pac_y -= self.settings.SPEED
    elif self.direction == 3 and self.turns_allowed[3]:
      self.pac_y += self.settings.SPEED


  def check_movement(self, event):
      keys_pressed = pygame.key.get_pressed()
      self.check_collisions()
      self.check_pos()
      self.check_pos()
      self.move_pac()

      if keys_pressed[pygame.K_b]:
          self.bportal.spawnportal(self.pac_x, self.pac_y, self.direction)
      if keys_pressed[pygame.K_o]:
          self.oportal.spawnportal(self.pac_x, self.pac_y, self.direction)

      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              self.direction_command = 0
          if event.key == pygame.K_LEFT:
              self.direction_command = 1
          if event.key == pygame.K_UP:
              self.direction_command = 2
          if event.key == pygame.K_DOWN:
              self.direction_command = 3

      if event.type == pygame.KEYUP:
          if event.key == pygame.K_RIGHT and self.direction_command == 0:
              self.direction_command = self.direction
          if event.key == pygame.K_LEFT and self.direction_command == 1:
              self.direction_command = self.direction
          if event.key == pygame.K_UP and self.direction_command == 2:
              self.direction_command = self.direction
          if event.key == pygame.K_DOWN and self.direction_command == 3:
              self.direction_command = self.direction

      if self.direction_command == 0 and self.turns_allowed[0]:
          self.direction = 0
      if self.direction_command == 1 and self.turns_allowed[1]:
          self.direction = 1
      if self.direction_command == 2 and self.turns_allowed[2]:
          self.direction = 2
      if self.direction_command == 3 and self.turns_allowed[3]:
          self.direction = 3

      for i in range(4):
          if self.direction_command == i and self.turns_allowed[i]:
              self.direction = i

      if self.pac_x > 900:
          self.pac_x = -47
      elif self.pac_x < -50:
          self.pac_x = 897

  def update(self):
    self.current_pacman_frame = self.pacman_frames[self.current_frame]
    # print('Current Frame: ', self.current_frame)
    if self.direction == 0:
        self.screen.blit((self.current_pacman_frame), (self.pac_x, self.pac_y))
    elif self.direction == 1:
        self.screen.blit(pygame.transform.flip(self.current_pacman_frame, True, False), (self.pac_x, self.pac_y))
    elif self.direction == 2:
        self.screen.blit(pygame.transform.rotate(self.current_pacman_frame, 90), (self.pac_x, self.pac_y))
    elif self.direction == 3:
        self.screen.blit(pygame.transform.rotate(self.current_pacman_frame, 270), (self.pac_x, self.pac_y))
    pygame.draw.circle(self.screen, 'white', (self.pac_x + 23, self.pac_y + 24), 20, 2)

  def draw(self):
    self.screen.blit(self.image, self.rect)



  def menu_mode(self):
    self.current_pacman_frame = self.pacman_frames[self.current_frame]
    if self.pac_x_menu > 900:
      self.end_pos = 900
    if self.pac_x_menu < -50:
      self.end_pos = 0

    if self.end_pos == 0:
      self.pac_x_menu += self.settings.SPEED
      self.screen.blit(self.current_pacman_frame, (self.pac_x_menu, self.pac_y_menu))
    if self.end_pos == 900:
      self.pac_x_menu -= self.settings.SPEED
      self.screen.blit(pygame.transform.flip(self.current_pacman_frame, True, False), (self.pac_x_menu, self.pac_y_menu))
    pygame.display.update()

  def copy(self):
      copyobj = Pacman()
      for name, attr in self.__dict__.items():
          if hasattr(attr, 'copy') and callable(getattr(attr, 'copy')):
              copyobj.__dict__[name] = attr.copy()
          else:
              copyobj.__dict__[name] = copy.deepcopy(attr)
      return copyobj

  def starting_pac(self):
    self.screen.blit(self.pacman_frames[2], (self.pac_x, self.pac_y))
    pygame.display.update()
