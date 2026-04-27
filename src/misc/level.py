from misc.base_objects import Point
from blocks.block import Block

class Level:

  def __init__(self, level = 1, lives = 3,rows = 5, columns = 10):
    self.level = level
    self.lives = lives
    self.rows = rows
    self.columns = columns

  def create_level(self, block):

    block_list = []
    if self.level == 1:
      for row in range(self.rows):
        if row == 0:
          continue
        for col in range(self.columns):
          x = block.position.x + col * (block.width + block.offset)
          y = block.position.y - row * (block.height + block.offset)
          block_list.append(Block(Point(x, y)))
    
    if self.level == 2:
      self.rows = 12
      self.columns = 10
      for row in range(self.rows):
        if row % 2 != 0:
          continue
        for col in range(self.columns):
          if col == 0 or col == 9:
            continue
          x = block.position.x + col * (block.width + block.offset)
          y = block.position.y - row * (block.height + block.offset)
          block_list.append(Block(Point(x, y)))

    if self.level == 3:
      self.rows = 9
      self.columns = 10
      for row in range(self.rows):
        if row % 2 == 0:
          continue
        for col in range(self.columns):
          x = block.position.x + col * (block.width + block.offset)
          y = block.position.y - row * (block.height + block.offset)
          block_list.append(Block(Point(x, y)))

    return block_list
