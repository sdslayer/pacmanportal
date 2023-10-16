import pygame
from settings import Settings
from pacman import Pacman
from board import Board
from scoreboard import Scoreboard
from ghosts import Ghosts, Blinky, Inky
from portals import BluePortal, OrangePortal
from menus import Menus
from sounds import Sounds
from game_functions import GameFunctions

class PacManGame:

  def __init__(self):
    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  #screen variable will be used instead of WIN
    self.board = Board(self)
    self.bportal = BluePortal(self)  # Create a single instance of BluePortal
    self.oportal = OrangePortal(self)
    self.scoreboard = Scoreboard(game = self)
    self.pacman = Pacman(self, self.bportal, self.oportal)
    self.ghosts = Ghosts(game = self)
    self.blinky = Blinky(game= self)
    self.inky = Inky(game = self)
    # self.pacman = Pacman(self)
    self.menus = Menus(self)
    self.sounds = Sounds(self)
    self.game_functions = GameFunctions(self)
    #self.ghosts = Ghosts(game = self)
    pygame.display.set_caption('Pac-Man')

  def reset(self):
    pass

  def game_over(self):
    pass

  def play(self):
    clock = pygame.time.Clock()
    running = True
    in_menu = True
    self.settings.power_counter = 0
    self.settings.start_time = pygame.time.get_ticks()
    self.settings.moving = False
    self.settings.startup_counter = 0
    self.settings.start = False
    self.scoreboard.get_high_score()
    print(self.scoreboard.high_score)
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
        #Starting the game and all functions
        else:
          # current_time = pygame.time.get_ticks()
          # elapsed_time = current_time - start_time
          if self.settings.game_over:
            self.game_functions.gameover()
          self.screen.fill((0, 0, 0))
          self.board.update() # Call draw screen and pass the level array to it
          self.scoreboard.draw_misc(poweredup=self.pacman.poweredup)
          if self.settings.startup_counter < 300:
              self.sounds.play_start_up()
              if not self.pacman.started:
                self.pacman.starting_pac()
              self.settings.moving = False
              self.settings.startup_counter +=1
          else:
              moving = True
              self.pacman.started = True
          #Actually startig the game
          if self.pacman.started:
            self.sounds.stop_sounds()
            self.pacman.started = True
            if moving:
              self.blinky.update()
              self.inky.update()
              # print('collided: ', self.ghosts.collided)
              if self.settings.reset:
                self.game_functions.reset()

              self.pacman.check_movement(event= event)  #Changed the function a lil to not accept any arguments
              self.pacman.update_pacman_frame()  # Update pacman's frame every frame
              self.pacman.update()
            # self.ghosts.update_ghosts()
            # self.ghosts.draw()



            ####PORTALS####
            # if event.type == pygame.KEYDOWN:
            #   print('Event key: ', event.key)
            #   keys_pressed = pygame.key.get_pressed()
            #   if keys_pressed == pygame.K_b:
            #       print("LCTRL")
            #       # Get Pac-Man's current position and direction from the self.pacman object
            #       pacman_x = self.pacman.pac_x
            #       pacman_y = self.pacman.pac_y
            #       pacman_direction = self.pacman.direction
            #       print(f"PACX: {pacman_x}, PACY: {pacman_y}, PACDIR: {pacman_direction}")
            #       self.bportal.spawnportal(pacman_x, pacman_y, pacman_direction)
            #   if keys_pressed == pygame.K_o:
            #       print("LCTRL")
            #       # Get Pac-Man's current position and direction from the self.pacman object
            #       pacman_x = self.pacman.pac_x
            #       pacman_y = self.pacman.pac_y
            #       pacman_direction = self.pacman.direction
            #       print(f"PACX: {pacman_x}, PACY: {pacman_y}, PACDIR: {pacman_direction}")
            #       self.oportal.spawnportal(pacman_x, pacman_y, pacman_direction)
            self.bportal.is_moving()
            self.bportal.checkcollisions()
            self.oportal.is_moving()
            self.oportal.checkcollisions()
            if self.bportal.spawned and self.oportal.spawned:
              if not self.bportal.is_moving() and not self.oportal.is_moving():
                self.pacman.teleport()
                #print("Both portals not moving.")
              #print("Orange portal not moving...")
            # self.screen.fill((0, 0, 0))
            # self.board.update() # Call draw screen and pass the level array to it
            self.bportal.draw()
            self.oportal.draw()
            ###PORTALS#####
            power_up_start_time = pygame.time.get_ticks()
            # print('power count: ', power_counter)
            # print('poweredup: ', self.pacman.poweredup)
            if self.pacman.poweredup == True and self.settings.power_counter < 600:
              self.settings.power_counter += 1
              # print(power_counter)
              print('powered UP!')
            elif self.pacman.poweredup and self.settings.power_counter >= 600:
              print('ENDED POWER UP!')
              self.settings.power_counter = 0
              self.pacman.poweredup = False
              # eaten_ghost = [False, False, False]
              # current_time_1 = pygame.time.get_ticks()
              # print('POWERED UP!')
              # elapsed_time_1 = current_time_1 - power_up_start_time
              # print('elapsed time: ', power_up_start_time)
              # if elapsed_time_1 == power_up_start_time + self.settings.poweredup_time:
              #   print('Powered up FINISHED!')
              #   self.pacman.poweredup = False






        # self.bportal.updateportal()
        # self.bportal.checkcollisions()
        # self.oportal.updateportal()
        # self.oportal.checkcollisions()
        # self.screen.fill((0, 0, 0))
        # self.board.update() # Call draw screen and pass the level array to it
        # self.bportal.draw()
        # self.oportal.draw()

        # blinky = Ghost(blinky_x, blinky_y, targets[0], ghost_speed,
        #                blinky_img, blinky_direction, blinky_dead, blinky_box, 0)

        # inky = Ghost(inky_x, inky_y, targets[0], ghost_speed,
        #                inky_img, inky_direction, inky_dead, inky_box, 0)

        # pinky = Ghost(pinky_x, pinky_y, targets[0], ghost_speed,
        #                pinky_img, pinky_direction, pinky_dead, pinky_box, 0)

        # clyde = Ghost(clyde_x, clyde_y, targets[0], ghost_speed,
        #                clyde_img, clyde_direction, clyde_dead, clyde_box, 0)


        pygame.display.update()

    pygame.quit()


def main():
    g = PacManGame()
    g.play()

if __name__ == '__main__':
    main()
