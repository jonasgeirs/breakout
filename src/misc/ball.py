import random

from OpenGL.GL import *
from OpenGL.GLU import *

import math
from math import cos, sin

from misc.base_objects import Vector, Point
from misc.calculations import *
from paddle.paddle_collision import paddle_collision
from blocks.block_collisions import block_collision
from border.border_collision import border_collision

class Ball:

  def __init__(self, position, motion, radius = 10, roundness = 10, speed = 600):
    self.position = position
    self.motion = motion
    self.radius = radius
    self.roundness = roundness
    self.speed = speed
    self.color = (
            1.0,
            random.uniform(0.1, 0.5),
            random.uniform(0.1, 0.5),
        )
  
  def update(self, dt, angle, screen, paddle, block_list):
    if self.motion.x == 0.0 and self.motion.y == 0.0:
      self.motion = Vector(-sin(angle * math.pi / 180.0), cos(angle * math.pi / 180.0)) * self.speed

    remaining_dt = dt

    while remaining_dt > 0.000001:
      max_t_hit = 1.1
      hit_normal = None
      hit_point = None
      hit_surface = None

      result = paddle_collision(paddle, self.position, self.motion, self.radius, remaining_dt)
      if result is not None:
        normal, t_hit, p_hit = result
        if 0 <= t_hit <= max_t_hit:
          max_t_hit = t_hit
          hit_normal = normal
          hit_point = p_hit
          hit_surface = "paddle"

      result = border_collision(screen, self.position, self.motion, self.radius, remaining_dt)
      if result is not None:
        normal, t_hit, p_hit, surface = result
        if 0 <= t_hit <= max_t_hit:
          max_t_hit = t_hit
          hit_normal = normal
          hit_point = p_hit
          hit_surface = surface

      result = block_collision(block_list, self.position, self.motion, self.radius, remaining_dt)
      if result is not None:
        normal, t_hit, p_hit = result
        if 0 <= t_hit <= max_t_hit:
          max_t_hit = t_hit
          hit_normal = normal
          hit_point = p_hit
          hit_surface = "block"

      if max_t_hit > 1.0:
        self.position += self.motion * remaining_dt
        break

      travel_time = min(max_t_hit, 1.0) * remaining_dt
      if hit_point is not None:
        self.position = hit_point
        self.motion = calculate_reflection(self.motion, hit_normal)

      remaining_dt -= travel_time

      if hit_surface == "bottom":
        return True
      
    return False


  def display(self):
    glColor3f(self.color[0], self.color[1], self.color[2])
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(self.position.x, self.position.y)
    for i in range(0, self.roundness + 1):
      angle = 2.0 * math.pi * i / self.roundness
      x = self.position.x + self.radius * cos(angle)
      y = self.position.y + self.radius * sin(angle)
      glVertex2f(x, y)  
      glVertex2f(self.position.x, self.position.y)
    glEnd()

