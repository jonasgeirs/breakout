import random

from OpenGL.GL import *
from OpenGL.GLU import *

from misc.base_objects import Point
from misc.calculations import *

class Block:

  def __init__(self, position):
    self.position = position
    self.width = 76.7
    self.height = 30
    self.offset = 3
    self.color = (
            random.uniform(0.1, 0.9),
            random.uniform(0.1, 0.5),
            1.0,
        )
    
    self.top_edge = (Point(self.position.x, self.position.y + self.height), 
                     Point(self.position.x + self.width, self.position.y + self.height))
    self.bottom_edge = (Point(self.position.x, self.position.y), 
                        Point(self.position.x + self.width, self.position.y))
    self.left_edge = (Point(self.position.x, self.position.y),
                      Point(self.position.x, self.position.y + self.height))
    self.right_edge = (Point(self.position.x + self.width, self.position.y), 
                       Point(self.position.x + self.width, self.position.y + self.height))

    self.top_normal = calculate_normal_vector(self.top_edge[0], self.top_edge[1])
    self.bottom_normal = calculate_normal_vector(self.bottom_edge[0], self.bottom_edge[1])
    self.left_normal = calculate_normal_vector(self.left_edge[0], self.left_edge[1])
    self.right_normal = calculate_normal_vector(self.right_edge[0], self.right_edge[1])

  def display(self):
      glColor3f(self.color[0], self.color[1], self.color[2])
      glBegin(GL_QUADS)
      glVertex2f(self.position.x, self.position.y)
      glVertex2f(self.position.x, self.position.y + self.height)
      glVertex2f(self.position.x + self.width, self.position.y + self.height)
      glVertex2f(self.position.x + self.width, self.position.y)
      glEnd()