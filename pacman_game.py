import pygame
from settings import Settings
from pacman import Pacman
from board import Board
from scoreboard import Scoreboard
from ghosts import Ghost
from portals import BluePortal, OrangePortal


class PacManGame:

  def __init__(self):
    pygame.init()
    self.settings = Settings()
    self.scoreboard = Scoreboard()
    self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  #screen variable will be used instead of WIN
    self.board = Board(self)
    self.bportal = BluePortal(self)  # Create a single instance of BluePortal
    self.oportal = OrangePortal(self)
    self.pacman = Pacman(self, self.bportal, self.oportal)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    #print("LCTRL")
                    # Get Pac-Man's current position and direction from the self.pacman object
                    pacman_x = self.pacman.pac_x
                    pacman_y = self.pacman.pac_y
                    pacman_direction = self.pacman.direction
                    print(f"PACX: {pacman_x}, PACY: {pacman_y}, PACDIR: {pacman_direction}")
                    self.bportal.spawnportal(pacman_x, pacman_y, pacman_direction)
                if event.key == pygame.K_o:
                    #print("LCTRL")
                    # Get Pac-Man's current position and direction from the self.pacman object
                    pacman_x = self.pacman.pac_x
                    pacman_y = self.pacman.pac_y
                    pacman_direction = self.pacman.direction
                    print(f"PACX: {pacman_x}, PACY: {pacman_y}, PACDIR: {pacman_direction}")
                    self.oportal.spawnportal(pacman_x, pacman_y, pacman_direction)

        self.bportal.updateportal()
        self.bportal.checkcollisions()
        self.oportal.updateportal()
        self.oportal.checkcollisions()
        self.screen.fill((0, 0, 0))
        self.board.update() # Call draw screen and pass the level array to it
        self.pacman.check_movement(event= event)  #Changed the function a lil to not accept any arguments
        self.pacman.update_pacman_frame()  # Update pacman's frame every frame
        self.pacman.update()

        self.bportal.draw()
        self.oportal.draw()

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
