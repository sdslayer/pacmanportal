import pygame
from settings import Settings
from pacman import Pacman
from board import Board
from scoreboard import Scoreboard


class PacManGame:

  def __init__(self):
    pygame.init()
    self.settings = Settings()
    self.scoreboard = Scoreboard()
    self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  #screen variable will be used instead of WIN
    self.board = Board(self)
    self.pacman = Pacman(self)
    # self.ghosts = Ghosts(game = self)
    pygame.display.set_caption('Pac-Man')

  def reset(self):
    pass

  def game_over(self):
    pass

  def play(self):
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(self.settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        self.screen.fill((0, 0, 0))
        self.board.update() # Call draw screen and pass the level array to it
        self.pacman.check_movement(event= event)  #Changed the function a lil to not accept any arguments
        self.pacman.update_pacman_frame()  # Update pacman's frame every frame
        self.pacman.update()


    pygame.quit()


def main():
    g = PacManGame()
    g.play()

if __name__ == '__main__':
    main()
