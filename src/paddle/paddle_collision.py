from misc.base_objects import Point
from misc.calculations import *

def paddle_collision(paddle, ball_position, ball_motion, radius, dt):
    motion_dt = ball_motion * dt

    left = paddle.position.x
    right = paddle.position.x + paddle.width
    top = paddle.position.y + paddle.height

    point1 = Point(left, top)
    point2 = Point(right, top)
    normal = calculate_normal_vector(point1, point2)

    t_hit = calculate_t_hit(normal, ball_position, motion_dt, point1)
    if t_hit is None or not 0 <= t_hit <= 1:
      return None
    
    p_hit = calculate_p_hit(t_hit, ball_position, motion_dt)
    if ball_motion.y < 0 and left <= p_hit.x <= right:
      p_hit.y = top + radius

      return (normal, t_hit, p_hit)
    
    return None