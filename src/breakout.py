import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import time

from blocks.block import Block
from paddle.paddle import Paddle
from paddle.aim import Aim
from border.border import Screen
from misc.base_objects import Vector, Point
from misc.ball import Ball
from misc.heart import Heart
from misc.level import Level


class Breakout:
  def __init__(self):
    self.screen = Screen(800, 600, 570, 0, 0, 800)
    
    self.running = True
    self.clock = pygame.time.Clock()
    self.stuck = True

    #set up display size and caption
    pygame.display.init()
    pygame.display.set_mode((self.screen.width, self.screen.height), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Breakout")

    self.clock.tick()

    self.heart = Heart(Point(self.screen.left_border + 20, self.screen.top_border + 5))
    self.paddle = Paddle(Point(self.screen.width / 2 - 50, 30))
    self.ball = Ball(Point(self.paddle.position.x + self.paddle.width / 2, self.paddle.position.y + self.paddle.height + 11), Vector(0.0, 0.0))
    self.aim = Aim(Point(self.paddle.position.x + self.paddle.width / 2, self.paddle.position.y + self.paddle.height + self.ball.radius + 1))
    self.block = Block(Point(self.screen.left_border + 3, self.screen.top_border - 35))

    self.level = Level(1)
    self.block_list = self.level.create_level(self.block)
  

  def update(self):
    dt = self.clock.tick() / 1000

    keys = pygame.key.get_pressed()

    self.paddle.update(dt, self.stuck, self.screen, self.ball, self.aim)
    
    if self.stuck:
      #shooting the ball   
      if keys[K_SPACE]:
        self.stuck = False

      #adjusting aim
      self.aim.update(dt)

    else:
      if self.ball.update(dt, self.aim.angle, self.screen, self.paddle, self.block_list):
        self.level.lives -= 1
        if self.level.lives > 0:
          self.lose_life()
        if self.level.lives == 0:
          self.lose()

      if len(self.block_list) == 0:
        self.level.level += 1
        self.win()


  def lose_life(self):
    time.sleep(0.5)
    self.stuck = True
    self.paddle = Paddle(Point(self.screen.width / 2 - 50, 30))
    self.ball = Ball(Point(self.paddle.position.x + self.paddle.width / 2, self.paddle.position.y + self.paddle.height + 10), Vector(0.0, 0.0))
    self.aim = Aim(Point(self.paddle.position.x + self.paddle.width / 2, self.paddle.position.y + self.paddle.height + self.ball.radius))

  def win(self):
    time.sleep(0.5)
    self.stuck = True
    self.paddle = Paddle(Point(self.screen.width / 2 - 50, 30))
    self.ball = Ball(Point(self.paddle.position.x + self.paddle.width / 2, self.paddle.position.y + self.paddle.height + 11), Vector(0.0, 0.0))
    self.aim = Aim(Point(self.paddle.position.x + self.paddle.width / 2, self.paddle.position.y + self.paddle.height + self.ball.radius + 1))
    if self.level.level == 4:
      self.level.level = 1
    self.level = Level(self.level.level)
    self.block_list = self.level.create_level(self.block)
    self.level.lives = 3

  def lose(self):
    time.sleep(0.5)
    self.stuck = True
    self.paddle = Paddle(Point(self.screen.width / 2 - 50, 30))
    self.ball = Ball(Point(self.paddle.position.x + self.paddle.width / 2, self.paddle.position.y + self.paddle.height + 11), Vector(0.0, 0.0))
    self.aim = Aim(Point(self.paddle.position.x + self.paddle.width / 2, self.paddle.position.y + self.paddle.height + self.ball.radius + 1))
    if self.level.level > 1:
      self.level.level -= 1
    self.level = Level(self.level.level)
    self.block_list = self.level.create_level(self.block)
    self.level.lives = 3

  def display(self):
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glViewport(0, 0, self.screen.width, self.screen.height)
    gluOrtho2D(0, self.screen.width, 0, self.screen.height)

    #top border 
    self.screen.display()

    #heart
    self.heart.display(self.level.lives)

    #paddle
    self.paddle.display()

    #block
    for block in self.block_list:
      block.display()

    #ball
    self.ball.display()

    #aim
    if self.stuck:
      self.aim.display()
    
    pygame.display.flip()


  def game_loop(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == K_ESCAPE:
          self.running = False
      
    self.update()
    self.display()

if __name__ == '__main__':
  game = Breakout()
  while game.running:
    game.game_loop()
  
  pygame.quit()