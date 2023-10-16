import pygame

class Scoreboard():
  def __init__(self, game):
    self.score = 0
    self.high_score = 0
    # self.pacman = game.pacman
    self.screen = game.screen
    self.font = pygame.font.Font('fonts/Pixeboy-z8XGD.ttf', 32)
  def update_score(self, score):
    self.score += score
    print('SCORE: ', self.score)

  def save_score(self):
    pass

  def draw_misc(self, poweredup):
    score_text = self.font.render(f'Score: {self.score}', True, 'white')
    self.screen.blit(score_text, (10,920))
    if poweredup:
       pygame.draw.circle(self.screen, 'blue', (140,930), 15)
