from typing import Any
import pygame
from pygame.sprite import Sprite
from pacman import Pacman


class Ghosts(Sprite):
    # pinky_img = pygame.image.load('images/ghost_images/pink.png')
    # inky_img = pygame.transform.scale(pygame.image.load(insert png sprite))
    # clyde_img = pygame.transform.scale(pygame.image.load(insert png sprite))
    # spooked_img = pygame.transform.scale(pygame.image.load(insert png sprite))
    # dead_ghost_img = pygame.transform.scale(pygame.image.load(insert png sprite))

    # blinky_x = 56 # starting positions outside of the box
    # blinky_y = 58 # starting positions outside of the box
    # blinky_direction = 0

    # pinky_x = 440 # starting positions inside of the box
    # pinky_x_y = 338 # starting positions inside of the box
    # pinky_direction = 2 # direction for them to go up

    # inky_x = 440
    # inky_y = 438
    # inky_direction = 2

    # clyde_x = 440
    # clyde_y = 438
    # clyde_direction = 2

    # counter = 0
    # flicker = False

    # eaten_ghost = [False, False, False, False]
    # targets = [(Pacman.pac_x, Pacman.pac_y), (Pacman.pac_x, Pacman.pac_y),
    #            (Pacman.pac_x, Pacman.pac_y), (Pacman.pac_x, Pacman.pac_y)] #targets player's
    # blinky_dead = False #tracks if they're dead
    # pinky_dead = False
    # inky_dead = False
    # clyde_dead = False

    # blinky_box = False # tracks if they're inside the box
    # pinky_box = False
    # inky_box = False
    # clyde_box = False
    # ghost_speed = 2



    def __init__(self, game):
        # self.x_pos = x_coord
        # self.y_pos = y_coord
        # self.center_x = self.x_pos + 22
        # self.center_y = self.y_pos + 22
        self.settings = game.settings
        self.screen = game.screen
        self.level = game.board.level
        self.pacman = game.pacman
        self.scoreboard = game.scoreboard
        self.target = [(self.pacman.pac_x, self.pacman.pac_y), (self.pacman.pac_x, self.pacman.pac_y), (self.pacman.pac_x, self.pacman.pac_y), (self.pacman.pac_x, self.pacman.pac_y)]
        self.spooked_img = pygame.transform.scale(pygame.image.load('images/ghost_images/powerup.png'), (45, 45))
        self.dead_ghost_img = pygame.transform.scale(pygame.image.load('images/ghost_images/dead.png'), (45, 45))
        # Blinky, Inky, Pinky and Clyde
        self.ghost_speeds = [1,1,1,1]
        self.eaten_ghosts = [False, False, False, False]
        self.collided = False
        # self.speed = speed
        # self.img = img
        # self.direction = direct
        # self.dead = dead
        # self.in_box = box
        # self.id = id
        # self.turns, self.in_box = self.check_collisions()
        # self.rect = self.draw()
        # self.screen = game.screen
        # self.level = game.board.level

    # def draw(self):
    #     powerup = False
    #     eaten_ghost = [False, False, False, False]
    #     if (not powerup and not self.dead) or (eaten_ghost[self.id] and powerup and not self.dead):
    #         self.screen.blit(self.img, (self.x_pos, self.y_pos))
    #     elif powerup and not self.dead and not eaten_ghost[self.id]:
    #         self.screen.blit(spooked_img, (self.x_pos, self.y_pos))
    #     else:
    #         self.screen.blit(dead_img, (self.x_pos, self.y_pos))
    #     ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
    #     return ghost_rect


    # def check_collisions(self, center_x, center_y):
    #   num1 = (self.settings.screen_height - 50) // 32
    #   num2 = self.screen_width // 30
    #   if 0 < self.pacman.pac_x < 870:
    #       if self.level[center_y // num1][center_x // num2] == 1:
    #           self.level[center_y // num1][center_x // num2] = 0
    #           self.scoreboard.score += 10
    #       if self.level[center_y // num1][center_x // num2] == 2:
    #           self.level[center_y // num1][center_x // num2] = 0
    #           self.scoreboard.score += 50
    #           self.pacman.poweredup = True
    #           self.pacman.power_count = 0
    #           self.eaten_ghosts = [False, False, False, False]



    def check_collisions(self, cx, cy, ded, direct):
        # R, L, U, D
        self.center_x = cx
        self.center_y = cy
        self.dead = ded
        self.direction = direct
        self.in_box = True

        HEIGHT = 900
        WIDTH = 950
        num1 = ((HEIGHT - 50) // 32)
        num2 = (WIDTH // 30)
        num3 = 15
        self.turns = [False, False, False, False]
        if 0 < self.center_x // 30 < 29:
            if self.level[(self.center_y - num3) // num1][self.center_x // num2] == 9:
                self.turns[2] = True
            if self.level[self.center_y // num1][(self.center_x - num3) // num2] < 3 \
                    or (self.level[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[1] = True
            if self.level[self.center_y // num1][(self.center_x + num3) // num2] < 3 \
                    or (self.level[self.center_y // num1][(self.center_x + num3) // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[0] = True
            if self.level[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
                    or (self.level[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[3] = True
            if self.level[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
                    or (self.level[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
                    self.in_box or self.dead)):
                self.turns[2] = True

            if self.direction == 2 or self.direction == 3:
                if 12 <= self.center_x % num2 <= 18:
                    if self.level[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
                            or (self.level[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[3] = True
                    if self.level[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
                            or (self.level[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[2] = True
                if 12 <= self.center_y % num1 <= 18:
                    if self.level[self.center_y // num1][(self.center_x - num2) // num2] < 3 \
                            or (self.level[self.center_y // num1][(self.center_x - num2) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[1] = True
                    if self.level[self.center_y // num1][(self.center_x + num2) // num2] < 3 \
                            or (self.level[self.center_y // num1][(self.center_x + num2) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[0] = True

            if self.direction == 0 or self.direction == 1:
                if 12 <= self.center_x % num2 <= 18:
                    if self.level[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
                            or (self.level[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[3] = True
                    if self.level[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
                            or (self.level[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[2] = True
                if 12 <= self.center_y % num1 <= 18:
                    if self.level[self.center_y // num1][(self.center_x - num3) // num2] < 3 \
                            or (self.level[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[1] = True
                    if self.level[self.center_y // num1][(self.center_x + num3) // num2] < 3 \
                            or (self.level[self.center_y // num1][(self.center_x + num3) // num2] == 9 and (
                            self.in_box or self.dead)):
                        self.turns[0] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 350 < self.x_pos < 550 and 370 < self.y_pos < 480:
            self.in_box = True
        else:
            self.in_box = False
        return self.turns, self.in_box

    def eaten(self, ghost):
      self.rect = ghost.rect
      self.dead = ghost.dead
      if self.pacman.poweredup and self.pacman.pac_circle.colliderect(self.rect) and not self.dead and not self.eaten_ghost[0]:
        print('EATEN!!')
        self.dead = True
        self.eaten_ghost[0] = True
        self.scoreboard.score += (2 ** self.eaten_ghost.count(True)) * 100
      return self.dead

    def g_to_p_collision(self, ghost):
      self.rect = ghost.rect
      self.dead = ghost.dead
      # print('dead: ', self.dead)
      if not self.pacman.poweredup:
          if (self.pacman.pac_circle.colliderect(self.rect) and not self.dead):
              if self.settings.lives > 0:
                  print('COLLIDED!!!')
                  self.settings.reset = True
                  # player_x = 450
                  # player_y = 663
                  # direction = 0
                  # direction_command = 0
                  # blinky_x = 56
                  # blinky_y = 58
                  # blinky_direction = 0
                  # inky_x = 440
                  # inky_y = 388
                  # inky_direction = 2
                  # pinky_x = 440
                  # pinky_y = 438
                  # pinky_direction = 2
                  # clyde_x = 440
                  # clyde_y = 438
                  # clyde_direction = 2
                  # blinky_dead = False
                  # inky_dead = False
                  # clyde_dead = False
                  # pinky_dead = False
              else:
                  print('GAME OVER!')
                  self.settings.game_over = True
                  self.settings.moving = False
                  self.settings.startup_counter = 0

    def draw(self, dead, id, center_x, center_y, x_pos, y_pos, image, rect):
        self.dead = dead
        self.id = id
        self.img = image
        self.center_x = center_x
        self.center_y = center_y
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = rect
        powerup = False
        self.eaten_ghost = [False, False, False, False]
        if (not powerup and not self.dead) or (self.eaten_ghost[self.id] and powerup and not self.dead):
            self.screen.blit(self.img, (self.x_pos, self.y_pos))
        elif powerup and not self.dead and not self.eaten_ghost[self.id]:
            self.screen.blit(self.spooked_img, (self.x_pos, self.y_pos))
        else:
            self.screen.blit(self.dead_img, (self.x_pos, self.y_pos))
        ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
        return ghost_rect




    # def move_clyde(self):
    #     # r, l, u, d
    #     # clyde is going to turn whenever advantageous for pursuit
    #     if self.direction == 0:
    #         if self.target[0] > self.x_pos and self.turns[0]:
    #             self.x_pos += self.speed
    #         elif not self.turns[0]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #         elif self.turns[0]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             if self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             else:
    #                 self.x_pos += self.speed
    #     elif self.direction == 1:
    #         if self.target[1] > self.y_pos and self.turns[3]:
    #             self.direction = 3
    #         elif self.target[0] < self.x_pos and self.turns[1]:
    #             self.x_pos -= self.speed
    #         elif not self.turns[1]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #         elif self.turns[1]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             if self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             else:
    #                 self.x_pos -= self.speed
    #     elif self.direction == 2:
    #         if self.target[0] < self.x_pos and self.turns[1]:
    #             self.direction = 1
    #             self.x_pos -= self.speed
    #         elif self.target[1] < self.y_pos and self.turns[2]:
    #             self.direction = 2
    #             self.y_pos -= self.speed
    #         elif not self.turns[2]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #         elif self.turns[2]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             else:
    #                 self.y_pos -= self.speed
    #     elif self.direction == 3:
    #         if self.target[1] > self.y_pos and self.turns[3]:
    #             self.y_pos += self.speed
    #         elif not self.turns[3]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #         elif self.turns[3]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             else:
    #                 self.y_pos += self.speed
    #     if self.x_pos < -30:
    #         self.x_pos = 900
    #     elif self.x_pos > 900:
    #         self.x_pos - 30
    #     return self.x_pos, self.y_pos, self.direction

    # def move_blinky(self):
    #     # r, l, u, d
    #     # blinky is going to turn whenever colliding with walls, otherwise continue straight
    #     if self.direction == 0:
    #         if self.target[0] > self.x_pos and self.turns[0]:
    #             self.x_pos += self.speed
    #         elif not self.turns[0]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #         elif self.turns[0]:
    #             self.x_pos += self.speed
    #     elif self.direction == 1:
    #         if self.target[0] < self.x_pos and self.turns[1]:
    #             self.x_pos -= self.speed
    #         elif not self.turns[1]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #         elif self.turns[1]:
    #             self.x_pos -= self.speed
    #     elif self.direction == 2:
    #         if self.target[1] < self.y_pos and self.turns[2]:
    #             self.direction = 2
    #             self.y_pos -= self.speed
    #         elif not self.turns[2]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #         elif self.turns[2]:
    #             self.y_pos -= self.speed
    #     elif self.direction == 3:
    #         if self.target[1] > self.y_pos and self.turns[3]:
    #             self.y_pos += self.speed
    #         elif not self.turns[3]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #         elif self.turns[3]:
    #             self.y_pos += self.speed
    #     if self.x_pos < -30:
    #         self.x_pos = 900
    #     elif self.x_pos > 900:
    #         self.x_pos - 30
    #     return self.x_pos, self.y_pos, self.direction

    # def move_inky(self):
    #     # r, l, u, d
    #     # inky turns up or down at any point to pursue, but left and right only on collision
    #     if self.direction == 0:
    #         if self.target[0] > self.x_pos and self.turns[0]:
    #             self.x_pos += self.speed
    #         elif not self.turns[0]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #         elif self.turns[0]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             if self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             else:
    #                 self.x_pos += self.speed
    #     elif self.direction == 1:
    #         if self.target[1] > self.y_pos and self.turns[3]:
    #             self.direction = 3
    #         elif self.target[0] < self.x_pos and self.turns[1]:
    #             self.x_pos -= self.speed
    #         elif not self.turns[1]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #         elif self.turns[1]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             if self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             else:
    #                 self.x_pos -= self.speed
    #     elif self.direction == 2:
    #         if self.target[1] < self.y_pos and self.turns[2]:
    #             self.direction = 2
    #             self.y_pos -= self.speed
    #         elif not self.turns[2]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #         elif self.turns[2]:
    #             self.y_pos -= self.speed
    #     elif self.direction == 3:
    #         if self.target[1] > self.y_pos and self.turns[3]:
    #             self.y_pos += self.speed
    #         elif not self.turns[3]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #         elif self.turns[3]:
    #             self.y_pos += self.speed
    #     if self.x_pos < -30:
    #         self.x_pos = 900
    #     elif self.x_pos > 900:
    #         self.x_pos - 30
    #     return self.x_pos, self.y_pos, self.direction

    # def move_pinky(self):
    #     # r, l, u, d
    #     # inky is going to turn left or right whenever advantageous, but only up or down on collision
    #     if self.direction == 0:
    #         if self.target[0] > self.x_pos and self.turns[0]:
    #             self.x_pos += self.speed
    #         elif not self.turns[0]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #         elif self.turns[0]:
    #             self.x_pos += self.speed
    #     elif self.direction == 1:
    #         if self.target[1] > self.y_pos and self.turns[3]:
    #             self.direction = 3
    #         elif self.target[0] < self.x_pos and self.turns[1]:
    #             self.x_pos -= self.speed
    #         elif not self.turns[1]:
    #             if self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #         elif self.turns[1]:
    #             self.x_pos -= self.speed
    #     elif self.direction == 2:
    #         if self.target[0] < self.x_pos and self.turns[1]:
    #             self.direction = 1
    #             self.x_pos -= self.speed
    #         elif self.target[1] < self.y_pos and self.turns[2]:
    #             self.direction = 2
    #             self.y_pos -= self.speed
    #         elif not self.turns[2]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.target[1] > self.y_pos and self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.turns[3]:
    #                 self.direction = 3
    #                 self.y_pos += self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #         elif self.turns[2]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             else:
    #                 self.y_pos -= self.speed
    #     elif self.direction == 3:
    #         if self.target[1] > self.y_pos and self.turns[3]:
    #             self.y_pos += self.speed
    #         elif not self.turns[3]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.target[1] < self.y_pos and self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[2]:
    #                 self.direction = 2
    #                 self.y_pos -= self.speed
    #             elif self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             elif self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #         elif self.turns[3]:
    #             if self.target[0] > self.x_pos and self.turns[0]:
    #                 self.direction = 0
    #                 self.x_pos += self.speed
    #             elif self.target[0] < self.x_pos and self.turns[1]:
    #                 self.direction = 1
    #                 self.x_pos -= self.speed
    #             else:
    #                 self.y_pos += self.speed
    #     if self.x_pos < -30:
    #         self.x_pos = 900
    #     elif self.x_pos > 900:
    #         self.x_pos - 30
    #     return self.x_pos, self.y_pos, self.direction


class Blinky(Ghosts):
  def __init__(self, game):
      super().__init__(game)
      self.blinky_x = 56 # starting positions outside of the box
      self.blinky_y = 58 # starting positions outside of the box
      self.x_pos, self.y_pos = self.blinky_x, self.blinky_y
      self.center_x = self.x_pos + 22
      self.center_y = self.y_pos + 22
      self.blinky_direction = 0
      self.blinky_dead = False
      self.target = self.target[0]
      self.turns, self.in_box = self.check_collisions(self.center_x, self.center_y, self.blinky_dead, self.blinky_direction)
      # self.target = target
      self.speed = 1
      self.id = 0
      self.img = pygame.transform.scale(pygame.image.load('images/ghost_images/red.png'), (45, 45))
      self.rect = self.img.get_rect()





  def move_blinky(self):
    # r, l, u, d
    # blinky is going to turn whenever colliding with walls, otherwise continue straight
    # print('Turns: ', self.turns[0], self.turns[1], self.turns[2], self.turns[3])
    if self.direction == 0:
        if self.target[0] > self.x_pos and self.turns[0]:
            self.x_pos += self.speed
        elif not self.turns[0]:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.direction = 3
                self.y_pos += self.speed
            elif self.target[1] < self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif self.target[0] < self.x_pos and self.turns[1]:
                self.direction = 1
                self.x_pos -= self.speed
            elif self.turns[3]:
                self.direction = 3
                self.y_pos += self.speed
            elif self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif self.turns[1]:
                self.direction = 1
                self.x_pos -= self.speed
        elif self.turns[0]:
            self.x_pos += self.speed
    elif self.direction == 1:
        if self.target[0] < self.x_pos and self.turns[1]:
            self.x_pos -= self.speed
        elif not self.turns[1]:
            if self.target[1] > self.y_pos and self.turns[3]:
                self.direction = 3
                self.y_pos += self.speed
            elif self.target[1] < self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif self.target[0] > self.x_pos and self.turns[0]:
                self.direction = 0
                self.x_pos += self.speed
            elif self.turns[3]:
                self.direction = 3
                self.y_pos += self.speed
            elif self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif self.turns[0]:
                self.direction = 0
                self.x_pos += self.speed
        elif self.turns[1]:
            self.x_pos -= self.speed
    elif self.direction == 2:
        if self.target[1] < self.y_pos and self.turns[2]:
            self.direction = 2
            self.y_pos -= self.speed
        elif not self.turns[2]:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.direction = 0
                self.x_pos += self.speed
            elif self.target[0] < self.x_pos and self.turns[1]:
                self.direction = 1
                self.x_pos -= self.speed
            elif self.target[1] > self.y_pos and self.turns[3]:
                self.direction = 3
                self.y_pos += self.speed
            elif self.turns[3]:
                self.direction = 3
                self.y_pos += self.speed
            elif self.turns[0]:
                self.direction = 0
                self.x_pos += self.speed
            elif self.turns[1]:
                self.direction = 1
                self.x_pos -= self.speed
        elif self.turns[2]:
            self.y_pos -= self.speed
    elif self.direction == 3:
        if self.target[1] > self.y_pos and self.turns[3]:
            self.y_pos += self.speed
        elif not self.turns[3]:
            if self.target[0] > self.x_pos and self.turns[0]:
                self.direction = 0
                self.x_pos += self.speed
            elif self.target[0] < self.x_pos and self.turns[1]:
                self.direction = 1
                self.x_pos -= self.speed
            elif self.target[1] < self.y_pos and self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif self.turns[2]:
                self.direction = 2
                self.y_pos -= self.speed
            elif self.turns[0]:
                self.direction = 0
                self.x_pos += self.speed
            elif self.turns[1]:
                self.direction = 1
                self.x_pos -= self.speed
        elif self.turns[3]:
            self.y_pos += self.speed
    if self.x_pos < -30:
        self.x_pos = 900
    elif self.x_pos > 900:
        self.x_pos - 30
    self.center_x = self.x_pos + 22
    self.center_y = self.y_pos + 22
    # return self.x_pos, self.y_pos, self.direction


  def update(self):
    # print("starting", self.center_x, self.center_y)
    self.turns, self.in_box = self.check_collisions(self.center_x, self.center_y, self.blinky_dead, self.direction)
    self.move_blinky()
    self.g_to_p_collision(self)
    self.dead = self.eaten(self)
    self.rect = self.draw(self.blinky_dead, self.id, self.center_x, self.center_y, self.x_pos, self.y_pos, self.img, self.rect)
    pygame.draw.circle(self.screen, 'white', (self.x_pos + 23, self.y_pos + 24), 20, 2)
