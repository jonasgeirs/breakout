# Breakout

A Python-based 2D Breakout-style game created as an assignment for the course Tölvugrafík in Reykjavík University, winter 2025.
The project combines real-time rendering, input handling, and custom collision detection to recreate classic arcade gameplay using Python and OpenGL.

## What this project does

- Implements a playable Breakout clone with a paddle, ball, blocks, and a lives system.
- Supports three progressively arranged levels with block layouts that change between levels.
- Uses an aim indicator when the ball is attached to the paddle.
- Handles collision detection between the ball and the paddle, blocks, and screen borders.
- Displays remaining lives as heart icons and resets game state after level completion or life loss.

## File 

- `assignment_2.py` — main game entrypoint and game loop
- `paddle/paddle.py` — paddle movement and display
- `paddle/aim.py` — aiming indicator while the ball is attached to the paddle
- `blocks/block.py` — block objects, appearance, and collision properties
- `border/border.py` — screen border and top-wall rendering
- `blocks/block_collisions.py`, `paddle/paddle_collision.py`, `border/border_collision.py` — collision detection helpers
- `misc/level.py` — level generation and progression logic
- `misc/ball.py` — ball movement, physics, collision handling, and rendering
- `misc/heart.py` — lives display using hearts
- `misc/base_objects.py` — simple `Point` and `Vector` classes
- `misc/calculations.py` — collision math, reflection, and normal vector utilities

## How to run

1. Install Python 3 if it is not already installed.
2. Install the required packages:

```bash
pip install pygame PyOpenGL
```

3. Run the game from the `src` folder:

```bash
py/python/python3 breakout.py
```

## Controls

- `A` — move paddle left
- `D` — move paddle right
- `Left Arrow` — adjust aim left
- `Right Arrow` — adjust aim right
- `Spacebar` — launch the ball
- `Esc` — quit the game

## License

This project is developed as part of a university assignment and is not licensed for commercial use, redistribution, or modification.