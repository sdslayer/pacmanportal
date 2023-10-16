import pygame

class Scoreboard():
  def __init__(self, game):
    self.score = 0
    self.high_score = 0
    self.temp = ''
    self.settings = game.settings
    # self.pacman = game.pacman
    self.screen = game.screen
    self.font = pygame.font.Font('fonts/Pixeboy-z8XGD.ttf', 32)
    self.pacs_image = pygame.image.load('images/player_images/1.png')
  def update_score(self, score):
    self.score += score
    print('SCORE: ', self.score)

  def get_high_score(self):
    with open('scores/highscore.txt', 'r') as file:
      self.temp = file.read()
      self.high_score = int(self.temp)


  def save_score(self):
    print('saving')
    if self.score > self.high_score:
      with open('scores/highscore.txt', 'w') as file:
        file.write(str(self.score))

  def draw_misc(self, poweredup):
    score_text = self.font.render(f'Score: {self.score}', True, 'white')
    self.screen.blit(score_text, (10,920))
    if poweredup:
       pygame.draw.circle(self.screen, 'blue', (170,930), 10)
    for i in range(self.settings.lives):
      self.screen.blit(pygame.transform.scale(self.pacs_image, (30,30)), (650 + i * 40, 915))
