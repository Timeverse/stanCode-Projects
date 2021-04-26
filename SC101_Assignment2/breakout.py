"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is a Breakout game that the user will bounce the ball back and forth, using a paddle, to knock-out all the bricks
If the ball falls below the paddle and out of the window, user will lose 1 life. The game stops when life reaches 0
Upper left corner is the score tabulation board while upper right corner is the number of lives left
"""


from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.set_user_live(lives)
    graphics.live_update()
    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.game_switch is True:
            graphics.ball.move(graphics.get_ball_x(), graphics.get_ball_y())
            graphics.obj_detect()
            if graphics.obj_action() is True:
                graphics.score_count()
            if graphics.ball_action() is True:
                graphics.live_count()
                if graphics.game_over() is True:
                    break


if __name__ == '__main__':
    main()
