import pygame

class Scoreboard():
  def __init__(self, game):
    self.score = 0
    self.high_score = 0
    self.settings = game.settings
    # self.pacman = game.pacman
    self.screen = game.screen
    self.font = pygame.font.Font('fonts/Pixeboy-z8XGD.ttf', 32)
    self.pacs_image = pygame.image.load('images/player_images/1.png')
  def update_score(self, score):
    self.score += score
    print('SCORE: ', self.score)

  def save_score(self):
    pass

  def draw_misc(self, poweredup):
    score_text = self.font.render(f'Score: {self.score}', True, 'white')
    self.screen.blit(score_text, (10,920))
    if poweredup:
       pygame.draw.circle(self.screen, 'blue', (170,930), 10)
    for i in range(self.settings.lives):
      self.screen.blit(pygame.transform.scale(self.pacs_image, (30,30)), (650 + i * 40, 915))
