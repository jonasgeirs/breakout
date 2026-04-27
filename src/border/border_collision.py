import math

from misc.base_objects import Vector, Point
from misc.calculations import *

def border_collision(screen, ball_position, ball_motion, radius, dt):
    next_hit = None

    borders_to_check = []
    if ball_motion.y > 0:
        borders_to_check.append((screen.top_left, screen.top_normal, "top"))
    if ball_motion.y < 0:
        borders_to_check.append((screen.bottom_left, screen.bottom_normal, "bottom"))
    if ball_motion.x < 0:
        borders_to_check.append((screen.top_left, screen.left_normal, "left"))
    if ball_motion.x > 0:
        borders_to_check.append((screen.top_right, screen.right_normal, "right"))

    for point, normal, name in borders_to_check:
        result = border_collision_helper(ball_position, ball_motion, point, normal, radius, dt)
        if result is not None:
            n, t_hit, p_hit = result
            if next_hit is None or t_hit < next_hit[1]:
                next_hit = (n, t_hit, p_hit, name)

    return next_hit


def border_collision_helper(ball_position, ball_motion, point1, normal, radius, dt):
    motion_dt = ball_motion * dt
    normal_length = math.sqrt(normal.x**2 + normal.y**2)
    unit_normal = Vector(normal.x / normal_length, normal.y / normal_length)

    motion_dot_normal = ball_motion.x * normal.x + ball_motion.y * normal.y
    adjusted_point = Point(
        point1.x - math.copysign(unit_normal.x * radius, motion_dot_normal),
        point1.y - math.copysign(unit_normal.y * radius, motion_dot_normal))

    t_hit = calculate_t_hit(normal, ball_position, motion_dt, adjusted_point)
    if t_hit is not None and 0 <= t_hit <= 1:
        p_hit = calculate_p_hit(t_hit, ball_position, motion_dt)
        return (normal, t_hit, p_hit)