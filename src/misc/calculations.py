from misc.base_objects import Vector, Point

def calculate_normal_vector(point1, point2):
  vector_length = Vector(point2.x, point2.y) - Vector(point1.x, point1.y)
  normal = Vector(-vector_length.y, vector_length.x)

  return normal

def calculate_t_hit(normal, ball_position, ball_motion, object_position):
  a_minus_b = Point(ball_position.x - object_position.x, ball_position.y - object_position.y)
  normal_dot_b_minus_a = normal.x * a_minus_b.x + normal.y * a_minus_b.y
  normal_dot_ball_motion = normal.x * ball_motion.x + normal.y * ball_motion.y

  if normal_dot_ball_motion == 0:
    return None
  
  t_hit = normal_dot_b_minus_a / normal_dot_ball_motion

  return t_hit

def calculate_p_hit(t_hit, ball_position, ball_motion):
  p_hit = ball_position + (ball_motion * t_hit)

  return p_hit

def calculate_reflection(motion, normal):
  motion_dot_normal = motion.x * normal.x + motion.y * normal.y
  normal_dot_normal = normal.x * normal.x + normal.y * normal.y

  reflection = motion - 2 * (motion_dot_normal / normal_dot_normal) * normal

  return reflection