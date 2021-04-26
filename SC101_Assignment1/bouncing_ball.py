"""
File: bouncing_ball.py
Name: Ralph Liu
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
# Global variable
VX = 3
VY = 10
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
ball = GOval(SIZE, SIZE)
ball_round = 0

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, START_X, START_Y)
    onmouseclicked(ball_drop)


def ball_drop(m):
    """
    :param m: The module does not use the mouse positioning function
    :return: The module does not return
    The module simulates a bouncing ball movement with a ball at the start point (START.X and START.Y)
    Upon user mouse click the simulation begin with VX as horizontal movement and VY as vertical movement
    The ball drop will take into the effect of gravity (GRAVITY) and loss of momentum (REDUCE)
    Everytime the ball bounce out to the right, another new ball is placed at start point and await for another click
    Once simulation times (ball_round) reach 3 times, the module ends
    """
    global VX
    global VY
    global window
    global GRAVITY
    global REDUCE
    global ball_round
    if ball_round < 3:
        # This line enables the function to cease once simulation time reaches 3
        if ball.x == START_X and ball.y == START_Y:
            # This line disables the mouse click if the simulation is in motion
            while True:
                ball.move(VX, VY)
                VY = VY + GRAVITY
                if ball.y <= 0 or ball.y >= window.height:
                    VY = -VY * REDUCE
                pause(DELAY)
                if ball.x >= window.width:
                    window.add(ball, START_X, START_Y)
                    ball_round += 1
                    break


if __name__ == "__main__":
    main()
