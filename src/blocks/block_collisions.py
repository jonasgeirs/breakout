def block_collision(block_list, ball_position, ball_motion, radius, dt):
    motion_dt = ball_motion * dt
    new_pos = ball_position + motion_dt

    ball_left = new_pos.x - radius
    ball_right = new_pos.x + radius
    ball_top = new_pos.y + radius
    ball_bottom = new_pos.y - radius

    for block in block_list:

      block_left = block.position.x
      block_right = block.position.x + block.width
      block_top = block.position.y + block.height
      block_bottom = block.position.y

      if ball_left < block_right and ball_right > block_left and ball_top > block_bottom and ball_bottom < block_top:

        overlap_x = min(block_right - ball_left, ball_right - block_left)
        overlap_y = min(block_top - ball_bottom, ball_top - block_bottom)

        if overlap_x < overlap_y:
          if ball_motion.x > 0:
            normal = block.right_normal
          else: 
            normal = block.left_normal
        else:
          if ball_motion.y > 0:
            normal = block.bottom_normal
          else: 
            normal = block.top_normal

        block_list.remove(block)

        return (normal, 0, new_pos)