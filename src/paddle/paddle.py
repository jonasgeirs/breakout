import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Paddle: 

  def __init__(self, position, width = 100, height = 20, speed = 500):
    self.position = position
    self.width = width
    self.height = height
    self.speed = speed

  def update(self, dt, stuck, screen, ball, aim):
    keys = pygame.key.get_pressed()

    if keys[K_a]:
      if self.position.x >= screen.left_border:
        self.position.x -= self.speed * dt
        if stuck:
          ball.position.x -= self.speed * dt
          aim.position.x -= self.speed * dt
  
    if keys[K_d]:
      if self.position.x <= screen.right_border - self.width:
        self.position.x += self.speed * dt
        if stuck:
          ball.position.x += self.speed * dt
          aim.position.x += self.speed * dt

  def display(self):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(self.position.x, self.position.y)
    glVertex2f(self.position.x, self.position.y + self.height)
    glVertex2f(self.position.x + self.width, self.position.y + self.height)
    glVertex2f(self.position.x + self.width, self.position.y)
    glEnd()