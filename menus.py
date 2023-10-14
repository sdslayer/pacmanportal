import pygame
import pygame
import sys
import copy

pygame.init()
# from moviepy.editor import VideoFileClip

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

class Menus():
  def __init__(self, game):
    self.screen = game.screen
    self.pacman = game.pacman
    self.screen_width = self.screen.get_width()
    self.screen_height = self.screen.get_height()
    self.font = pygame.font.Font('fonts/Pixeboy-z8XGD.ttf', 64)
    self.play_button_text = self.font.render('PLAY GAME !', True, WHITE)
    self.play_button_rect = self.play_button_text.get_rect(center=(self.screen_width // 2,700))
    self.logo = self.image = pygame.image.load('images/menu/pac-man-logo.png')
    self.logo_rect = self.logo.get_rect()



  def draw_menu(self):
      self.screen.fill(BLACK)
      self.screen.blit(self.play_button_text, self.play_button_rect)
      self.screen.blit(self.logo, (self.screen_width // 2 - self.logo_rect.width // 2, 0))
      self.draw_animations()
      self.pacman.update_pacman_frame()
      pygame.display.update()

  def draw_animations(self):
    self.pacman.menu_mode()

  # def update_pacman_frame(self):
  #     self.frame_counter += 1 # Increase frame counter (how long its been on screen for)
  #     if self.frame_counter >= self.PACMAN_FRAME_DURATION: # If frame counter > max length of a frame...
  #         self.frame_counter = 0 # Set frame counter to 0
  #         self.current_frame = (self.current_frame + 1) % len(self.pacman_frames) # Set the next frame
  #     # print('Current Frame: ', self.frame_counter)
