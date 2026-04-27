import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Aim:

  def __init__(self, position, angle = 0.0):
    self.position = position
    self.angle = angle

  def update(self, dt):
    keys = pygame.key.get_pressed()

    if keys[K_LEFT] and self.angle <= 75.0:
      self.angle += 100.0 * dt
    if keys[K_RIGHT] and self.angle >= -75.0:
      self.angle -= 100.0 * dt

  def display(self):
    glPushMatrix()
    glTranslatef(self.position.x, self.position.y, 0)
    glRotatef(self.angle, 0, 0, 1)
    glTranslatef(-self.position.x, -self.position.y, 0)

    glColor3f(1.0, 0.0, 1.0)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(self.position.x, self.position.y)
    glVertex2f(self.position.x, self.position.y * 2)
    glEnd()

    glPopMatrix()