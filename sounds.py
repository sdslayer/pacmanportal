import pygame
#note sounds is buggy asf since it runs on a loop and will keep playing the same audio
pygame.mixer.init()  # Initialize the mixer

class Sounds():
  def __init__(self, game):
    self.pacman = game.pacman
    self.start = 0

  def play_start_up(self):
    if self.start == 0:
      self.start = 1
      self.start_up = pygame.mixer.music.load('sounds/pacman-beginning/pacman_beginning.wav')  # Load your sound file
      pygame.mixer.music.play()

  def stop_sounds(self):
    pygame.mixer.music.stop()
