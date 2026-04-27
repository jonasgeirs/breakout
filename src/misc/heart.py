from OpenGL.GL import *
from OpenGL.GLU import *

class Heart:

  def __init__(self, poisition, offset = 30):
    self.position = poisition
    self.offset = offset

  def display(self, lives):
    for i in range(0, lives):
      glColor3f(1.0, 0.0, 0.0)
      glBegin(GL_POLYGON)
      glVertex2f(self.position.x + self.offset * i, self.position.y)
      glVertex2f(self.position.x + self.offset * i - 10, self.position.y + 10)
      glVertex2f(self.position.x + self.offset * i - 10, self.position.y + 18)
      glVertex2f(self.position.x + self.offset * i - 4, self.position.y + 20)
      glVertex2f(self.position.x + self.offset * i, self.position.y + 15)
      glVertex2f(self.position.x + self.offset * i + 4, self.position.y + 20)
      glVertex2f(self.position.x + self.offset * i + 10, self.position.y + 18)
      glVertex2f(self.position.x + self.offset * i + 10, self.position.y + 10)
      glEnd()