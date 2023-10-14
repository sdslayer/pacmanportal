import pygame
from settings import Settings
from pacman import Pacman
from board import Board
from scoreboard import Scoreboard
from menus import Menus
from sounds import Sounds

class PacManGame:

  def __init__(self):
    pygame.init()
    self.settings = Settings()
    self.scoreboard = Scoreboard()
    self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  #screen variable will be used instead of WIN
    self.board = Board(self)
    self.pacman = Pacman(self)
    self.menus = Menus(self)
    self.sounds = Sounds(self)
    # self.ghosts = Ghosts(game = self)
    pygame.display.set_caption('Pac-Man')

  def reset(self):
    pass

  def game_over(self):
    pass

  def play(self):
    clock = pygame.time.Clock()
    running = True
    in_menu = True
    start_time = pygame.time.get_ticks()
    while running:
        clock.tick(self.settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.menus.play_button_rect.collidepoint(event.pos):
                    in_menu = False
        if in_menu:
          self.menus.draw_menu()

        else:
          #Start to load up the game
          current_time = pygame.time.get_ticks()
          elapsed_time = current_time - start_time
          self.screen.fill((0, 0, 0))
          self.board.update() # Call draw screen and pass the level array to it
          self.sounds.play_start_up()
          if not self.pacman.started:
            self.pacman.starting_pac()
          #Actually startig the game
          if elapsed_time >= self.settings.startup_time:
            self.sounds.stop_sounds()
            self.pacman.started = True
            self.pacman.check_movement(event= event)  #Changed the function a lil to not accept any arguments
            power_up_start_time = pygame.time.get_ticks()
            if self.pacman.poweredup == True:
              current_time_1 = pygame.time.get_ticks()
              print('POWERED UP!')
              elapsed_time_1 = current_time_1 - power_up_start_time
              print('elapsed time: ', power_up_start_time)
              if elapsed_time_1 == power_up_start_time + self.settings.poweredup_time:
                print('Powered up FINISHED!')
                self.pacman.poweredup = False
            self.pacman.update_pacman_frame()  # Update pacman's frame every frame
            self.pacman.update()


    pygame.quit()


def main():
    g = PacManGame()
    g.play()

if __name__ == '__main__':
    main()
