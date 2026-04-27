from OpenGL.GL import *
from OpenGL.GLU import *

from misc.base_objects import Point
from misc.calculations import *

class Screen:

  def __init__(self, width, height, top_border, bottom_border, left_border, right_border):
    self.width = width
    self.height = height
    self.top_border = top_border
    self.bottom_border = bottom_border
    self.left_border = left_border
    self.right_border = right_border

    self.top_left = Point(self.left_border, self.top_border)
    self.bottom_left = Point(self.left_border, self.bottom_border)
    self.top_right = Point(self.right_border, self.top_border)
    self.bottom_right = Point(self.right_border, self.bottom_border)

    self.top_normal = calculate_normal_vector(self.top_left, self.top_right)
    self.bottom_normal = calculate_normal_vector(self.bottom_left, self.bottom_right)
    self.left_normal = calculate_normal_vector(self.top_left, self.bottom_left)
    self.right_normal = calculate_normal_vector(self.top_right, self.bottom_right)

  def display(self):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(self.left_border, self.top_border)
    glVertex2f(self.right_border, self.top_border)
    glEnd()
