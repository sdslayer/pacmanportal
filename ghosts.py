# import pygame
# from pygame.sprite import Sprite
# from pacman import Pacman


# class Ghosts(Sprite):
#     # blinky_img = pygame.transform.scale(pygame.image.load(insert png sprite))
#     # pinky_img = pygame.transform.scale(pygame.image.load(f'images/ghost_images/pink.png'), 0, 1)
#     # inky_img = pygame.transform.scale(pygame.image.load(insert png sprite))
#     # clyde_img = pygame.transform.scale(pygame.image.load(insert png sprite))
#     # spooked_img = pygame.transform.scale(pygame.image.load(insert png sprite))
#     # dead_ghost_img = pygame.transform.scale(pygame.image.load(insert png sprite))

#     blinky_x = 56 # starting positions outside of the box
#     blinky_y = 58 # starting positions outside of the box
#     blinky_direction = 0

#     pinky_x = 440 # starting positions inside of the box
#     pinky_x_y = 338 # starting positions inside of the box
#     pinky_direction = 2 # direction for them to go up

#     inky_x = 440
#     inky_y = 438
#     inky_direction = 2

#     clyde_x = 440
#     clyde_y = 438
#     clyde_direction = 2

#     counter = 0
#     flicker = False

#     eaten_ghost = [False, False, False, False]
#     targets = [(Pacman.pac_x, Pacman.pac_y), (Pacman.pac_x, Pacman.pac_y), (Pacman.pac_x, Pacman.pac_y), (Pacman.pac_x, Pacman.pac_y)] #targets player's
#     blinky_dead = False #tracks if they're dead
#     pinky_dead = False
#     inky_dead = False
#     clyde_dead = False

#     blinky_box = False # tracks if they're inside the box
#     pinky_box = False
#     inky_box = False
#     clyde_box = False
#     ghost_speed = 2



#     def __init__(self, game, x_coord, y_coord, target, speed, img, direct, dead, box, id):
#         self.x_pos = x_coord
#         self.y_pos = y_coord
#         self.center_x = self.x_pos + 22
#         self.center_y = self.y_pos + 22
#         self.target = target
#         self.speed = speed
#         self.img = img
#         self.direction = direct
#         self.dead = dead
#         self.in_box = box
#         self.id = id
#         self.turns, self.in_box = self.check_collisions()
#         self.rect = self.draw()
#         self.screen = game.screen
#         self.level = game.board.level

#     def draw(self):
#         powerup = False
#         eaten_ghost = [False, False, False, False]
#         if (not powerup and not self.dead) or (eaten_ghost[self.id] and powerup and not self.dead):
#             self.screen.blit(self.img, (self.x_pos, self.y_pos))
#         elif powerup and not self.dead and not eaten_ghost[self.id]:
#             self.screen.blit(spooked_img, (self.x_pos, self.y_pos))
#         else:
#             self.screen.blit(dead_img, (self.x_pos, self.y_pos))
#         ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
#         return ghost_rect

#     def check_collisions(self):
#         # R, L, U, D
#         HEIGHT = 900
#         WIDTH = 950
#         num1 = ((HEIGHT - 50) // 32)
#         num2 = (WIDTH // 30)
#         num3 = 15
#         self.turns = [False, False, False, False]
#         if 0 < self.center_x // 30 < 29:
#             if self.level[(self.center_y - num3) // num1][self.center_x // num2] == 9:
#                 self.turns[2] = True
#             if self.level[self.center_y // num1][(self.center_x - num3) // num2] < 3 \
#                     or (self.level[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (
#                     self.in_box or self.dead)):
#                 self.turns[1] = True
#             if self.level[self.center_y // num1][(self.center_x + num3) // num2] < 3 \
#                     or (self.level[self.center_y // num1][(self.center_x + num3) // num2] == 9 and (
#                     self.in_box or self.dead)):
#                 self.turns[0] = True
#             if self.level[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
#                     or (self.level[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
#                     self.in_box or self.dead)):
#                 self.turns[3] = True
#             if self.level[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
#                     or (self.level[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
#                     self.in_box or self.dead)):
#                 self.turns[2] = True

#             if self.direction == 2 or self.direction == 3:
#                 if 12 <= self.center_x % num2 <= 18:
#                     if self.level[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
#                             or (self.level[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[3] = True
#                     if self.level[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
#                             or (self.level[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[2] = True
#                 if 12 <= self.center_y % num1 <= 18:
#                     if self.level[self.center_y // num1][(self.center_x - num2) // num2] < 3 \
#                             or (self.level[self.center_y // num1][(self.center_x - num2) // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[1] = True
#                     if self.level[self.center_y // num1][(self.center_x + num2) // num2] < 3 \
#                             or (self.level[self.center_y // num1][(self.center_x + num2) // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[0] = True

#             if self.direction == 0 or self.direction == 1:
#                 if 12 <= self.center_x % num2 <= 18:
#                     if self.level[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
#                             or (self.level[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[3] = True
#                     if self.level[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
#                             or (self.level[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[2] = True
#                 if 12 <= self.center_y % num1 <= 18:
#                     if self.level[self.center_y // num1][(self.center_x - num3) // num2] < 3 \
#                             or (self.level[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[1] = True
#                     if self.level[self.center_y // num1][(self.center_x + num3) // num2] < 3 \
#                             or (self.level[self.center_y // num1][(self.center_x + num3) // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[0] = True
#         else:
#             self.turns[0] = True
#             self.turns[1] = True
#         if 350 < self.x_pos < 550 and 370 < self.y_pos < 480:
#             self.in_box = True
#         else:
#             self.in_box = False
#         return self.turns, self.in_box

#     def move_clyde(self):
#         # r, l, u, d
#         # clyde is going to turn whenever advantageous for pursuit
#         if self.direction == 0:
#             if self.target[0] > self.x_pos and self.turns[0]:
#                 self.x_pos += self.speed
#             elif not self.turns[0]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#             elif self.turns[0]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 if self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 else:
#                     self.x_pos += self.speed
#         elif self.direction == 1:
#             if self.target[1] > self.y_pos and self.turns[3]:
#                 self.direction = 3
#             elif self.target[0] < self.x_pos and self.turns[1]:
#                 self.x_pos -= self.speed
#             elif not self.turns[1]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[1]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 if self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 else:
#                     self.x_pos -= self.speed
#         elif self.direction == 2:
#             if self.target[0] < self.x_pos and self.turns[1]:
#                 self.direction = 1
#                 self.x_pos -= self.speed
#             elif self.target[1] < self.y_pos and self.turns[2]:
#                 self.direction = 2
#                 self.y_pos -= self.speed
#             elif not self.turns[2]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[2]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 else:
#                     self.y_pos -= self.speed
#         elif self.direction == 3:
#             if self.target[1] > self.y_pos and self.turns[3]:
#                 self.y_pos += self.speed
#             elif not self.turns[3]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[3]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 else:
#                     self.y_pos += self.speed
#         if self.x_pos < -30:
#             self.x_pos = 900
#         elif self.x_pos > 900:
#             self.x_pos - 30
#         return self.x_pos, self.y_pos, self.direction

#     def move_blinky(self):
#         # r, l, u, d
#         # blinky is going to turn whenever colliding with walls, otherwise continue straight
#         if self.direction == 0:
#             if self.target[0] > self.x_pos and self.turns[0]:
#                 self.x_pos += self.speed
#             elif not self.turns[0]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#             elif self.turns[0]:
#                 self.x_pos += self.speed
#         elif self.direction == 1:
#             if self.target[0] < self.x_pos and self.turns[1]:
#                 self.x_pos -= self.speed
#             elif not self.turns[1]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[1]:
#                 self.x_pos -= self.speed
#         elif self.direction == 2:
#             if self.target[1] < self.y_pos and self.turns[2]:
#                 self.direction = 2
#                 self.y_pos -= self.speed
#             elif not self.turns[2]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#             elif self.turns[2]:
#                 self.y_pos -= self.speed
#         elif self.direction == 3:
#             if self.target[1] > self.y_pos and self.turns[3]:
#                 self.y_pos += self.speed
#             elif not self.turns[3]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#             elif self.turns[3]:
#                 self.y_pos += self.speed
#         if self.x_pos < -30:
#             self.x_pos = 900
#         elif self.x_pos > 900:
#             self.x_pos - 30
#         return self.x_pos, self.y_pos, self.direction

#     def move_inky(self):
#         # r, l, u, d
#         # inky turns up or down at any point to pursue, but left and right only on collision
#         if self.direction == 0:
#             if self.target[0] > self.x_pos and self.turns[0]:
#                 self.x_pos += self.speed
#             elif not self.turns[0]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#             elif self.turns[0]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 if self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 else:
#                     self.x_pos += self.speed
#         elif self.direction == 1:
#             if self.target[1] > self.y_pos and self.turns[3]:
#                 self.direction = 3
#             elif self.target[0] < self.x_pos and self.turns[1]:
#                 self.x_pos -= self.speed
#             elif not self.turns[1]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[1]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 if self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 else:
#                     self.x_pos -= self.speed
#         elif self.direction == 2:
#             if self.target[1] < self.y_pos and self.turns[2]:
#                 self.direction = 2
#                 self.y_pos -= self.speed
#             elif not self.turns[2]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[2]:
#                 self.y_pos -= self.speed
#         elif self.direction == 3:
#             if self.target[1] > self.y_pos and self.turns[3]:
#                 self.y_pos += self.speed
#             elif not self.turns[3]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[3]:
#                 self.y_pos += self.speed
#         if self.x_pos < -30:
#             self.x_pos = 900
#         elif self.x_pos > 900:
#             self.x_pos - 30
#         return self.x_pos, self.y_pos, self.direction

#     def move_pinky(self):
#         # r, l, u, d
#         # inky is going to turn left or right whenever advantageous, but only up or down on collision
#         if self.direction == 0:
#             if self.target[0] > self.x_pos and self.turns[0]:
#                 self.x_pos += self.speed
#             elif not self.turns[0]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#             elif self.turns[0]:
#                 self.x_pos += self.speed
#         elif self.direction == 1:
#             if self.target[1] > self.y_pos and self.turns[3]:
#                 self.direction = 3
#             elif self.target[0] < self.x_pos and self.turns[1]:
#                 self.x_pos -= self.speed
#             elif not self.turns[1]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[1]:
#                 self.x_pos -= self.speed
#         elif self.direction == 2:
#             if self.target[0] < self.x_pos and self.turns[1]:
#                 self.direction = 1
#                 self.x_pos -= self.speed
#             elif self.target[1] < self.y_pos and self.turns[2]:
#                 self.direction = 2
#                 self.y_pos -= self.speed
#             elif not self.turns[2]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[2]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 else:
#                     self.y_pos -= self.speed
#         elif self.direction == 3:
#             if self.target[1] > self.y_pos and self.turns[3]:
#                 self.y_pos += self.speed
#             elif not self.turns[3]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[3]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 else:
#                     self.y_pos += self.speed
#         if self.x_pos < -30:
#             self.x_pos = 900
#         elif self.x_pos > 900:
#             self.x_pos - 30
#         return self.x_pos, self.y_pos, self.direction


# ###############################################################
# # class Ghost(Sprite):
# #     def __init__(self, game, x_coord, y_coord, target,
# #                  speed, img, direct, dead, box, id):
# #         self.x_pos = x_coord
# #         self.y_pos = y_coord
# #         self.center_x = self.x_pos + 22
# #         self.center_y = self.y_pos + 22
# #         self.target = target
# #         self.speed = speed
# #         self.img = img
# #         self.direction = direct
# #         self.dead = dead
# #         self.in_box = box
# #         self.id = id
# #         self.turns, self.in_box = self.check_collisions()
# #         self.rect = self.draw()
# #         powerup = False #this will be for the ghosts
# #         power_counter = 0 # this will be for the ghosts
# #         eaten_ghost = [False, False, False, False] #this will be for the ghosts
# #         targets = [(Pacman.pac_x, Pacman.pac_y), (Pacman.pac_x, Pacman.pac_y), (Pacman.pac_x, Pacman.pac_y), (Pacman.pac_x, Pacman.pac_y)]


# #     def draw(self):
# #         if (not powerup and not self.dead) or (eaten_ghost[self.id]
# #                                                and powerup and not self.dead):
# #             screen.blit(self.img, (self.x_pos, self.y_pos))
# #         elif powerup and not self.dead and not eaten_ghost[self.id]:
# #             screen.blit(spooked_img, (self.x_pos, self.y_pos))
# #         else:
# #             screen.blit(dead_img, (self.x_pos, self.y_pos))
# #         ghost_Rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
# #         return ghost_rect

# #     def check_collisons(self):
# #         self.turns = [False, False, False, False]
# #         return self.turns, self.in_box

# #         super().__init__()
# #         self.screen = game.screen
# #         self.settings = game.settings
# #         self.screen_rect = game.screen.get_rect()

# #         self.image = pygame.image.load('insert ghost sprite')
# #         self.rect = self.image.get_rect()

# #         self.GHOST_FRAME_DURATION = 5
# #         self.current_frame = 0
# #         self.frame_counter = 0

# #         PACMAN = pygame.Rect(30, 30, 60, 60)

# #         # blinky_img = pygame.transform.scale(pygame.image.load(insert png sprite))
# #         # pinky_img = pygame.transform.scale(pygame.image.load(insert png sprite))
# #         # inky_img = pygame.transform.scale(pygame.image.load(insert png sprite))
# #         # clyde_img = pygame.transform.scale(pygame.image.load(insert png sprite))
# #         # spooked_img = pygame.transform.scale(pygame.image.load(insert png sprite))
# #         # dead_ghost_img = pygame.transform.scale(pygame.image.load(insert png sprite))

# #         blinky_x = 56 # starting positions outside of the box
# #         blinky_y = 58 # starting positions outside of the box
# #         blinky_direction = 0

# #         pinky_x = 440 # starting positions inside of the box
# #         pinky_x_y = 338 # starting positions inside of the box
# #         pinky_direction = 2 # direction for them to go up

# #         inky_x = 440
# #         inky_y = 438
# #         inky_direction = 2

# #         clyde_x = 440
# #         clyde_y = 438
# #         clyde_direction = 2


# #         eaten_ghost = [False, False, False, False]
# #         targets = [(player_x, player_y), (player_x, player_y), (player_x, player_y), (player_x, player_y)] #targets player's
# #         blinky_dead = False #tracks if they're dead
# #         pinky_dead = False
# #         inky_dead = False
# #         clyde_dead = False

# #         blinky_box = False # tracks if they're inside the box
# #         pinky_box = False
# #         inky_box = False
# #         clyde_box = False
# #         ghost_speed = 2
