import pygame

class Scoreboard():
  def __init__(self):
    self.score = 0
    self.high_score = 0

  def update_score(self, score):
    self.score += score
    print('SCORE: ', self.score)

  def save_score(self):
    pass
