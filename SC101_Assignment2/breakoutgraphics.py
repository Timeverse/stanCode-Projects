"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, (window_width - paddle_width) / 2, window_height - paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, (window_width - ball_radius * 2) / 2, (window_height - ball_radius * 2) / 2)
        # Default initial velocity for the ball
        self._dx = random.randint(1, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self._dx = - self._dx

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.game_start)
        # Draw bricks
        self.brick_count = 0
        for i in range(brick_rows):
            for x in range(brick_cols):
                brick_x = 0 + (i * (brick_width + brick_spacing))
                brick_y = 0 + brick_offset + (x * (brick_height + brick_spacing))
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick_color = color_setter(x)
                self.brick.fill_color = self.brick_color
                self.window.add(self.brick, brick_x, brick_y)
                self.brick_count += 1
        # Score label
        self.user_score = 0
        self.score_label = GLabel('Score :' + str(self.user_score))
        self.window.add(self.score_label, 10, self.score_label.height + 10)

        # Live label
        # Please ignore the attribute of 5 as it will be updated through set_user_live()
        self.user_life = 5
        self.live_label = GLabel('Number of Live Left :')
        self.window.add(self.live_label, window_width - self.live_label.width - 10, self.live_label.height + 10)

        # Game start switch
        self.game_switch = False

    # Method to move paddle
    def move_paddle(self, m):
        if m.x + self.paddle.width / 2 <= self.window.width:
            self.paddle.x = m.x - self.paddle.width / 2
        if m.x - self.paddle.width / 2 <= 0:
            self.paddle.x = m.x

    # Method to determine ball action when meet the 4 walls of the window
    def ball_action(self):
        """
        When the ball hits the upper, right and left wall, the direction will be opposite to enable bounce
        :return: When ball falls below the lower wall, the module return True
        """
        if self.ball.y + self.ball.height / 2 >= self.window.height:
            return True
        if self.ball.y + self.ball.height / 2 <= 0:
            self._dy *= -1
            return False
        if self.ball.x <= 0 or self.ball.x + self.ball.width / 2 >= self.window.width:
            self._dx *= -1
            return False

    # Method to reset ball
    """
    Once ball_action returns True, the method enables the reset of ball and flip game_switch back to False
    """
    def reset_ball(self):
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2, (self.window.height - self.ball.height)\
                        / 2)
        self.game_switch = False

    # Method to start the game
    """
    The method takes the user mouse click and check if the ball is at the starting position
    It then move on to flip the game_switch to True
    """
    def game_start(self, e):
        if self.ball.x == (self.window.width - self.ball.width) / 2:
            if self.ball.y == (self.window.height - self.ball.height) / 2:
                self.game_switch = True
        else:
            pass

    # Method to detect object around ball
    def obj_detect(self):
        """
        The method checks the 4 corners of the ball for any objects that these 4 points met
        :return: if any of the 4 points met objects, the method returns the x and y of the specific point
        """
        object_left_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        object_right_1 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        object_left_2 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        object_right_2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if object_left_1 is not None:
            return object_left_1
        if object_left_2 is not None:
            return object_left_2
        if object_right_1 is not None:
            return object_right_1
        if object_right_2 is not None:
            return object_left_2
        else:
            pass

    # Method to determine action when encounter obstacle
    def obj_action(self):
        """
        The method further distinguish the met objects between, paddle, label and bricks
        :return: If the met object is brick, the method returns True for scoring and removes the brick
        """
        if self.obj_detect() is self.paddle:
            if self._dy >= 0:
                self._dy *= - 1
        else:
            pass
            if self.obj_detect() is not None and self.obj_detect() is not self.score_label and self.obj_detect() is not\
                    self.live_label:
                self.window.remove(self.obj_detect())
                self._dy *= - 1
                return True
            else:
                pass

    # Method for score counter
    def score_count(self):
        self.user_score += 1
        self.score_label.text = 'Score :' + str(self.user_score)

    # Live setter
    def set_user_live(self, lives):
        """
        This is to bring the user set number of lives into the code
        :param lives: Number of lives that user set
        """
        self.user_life = lives

    # Live label update
    def live_update(self):
        """
        This method serve to show the beginning number of lives in the Glabel
        """
        self.live_label.text = 'Number of lives left :' + str(self.user_life)

    # Method for live counter
    def live_count(self):
        self.user_life -= 1
        self.live_label.text = 'Number of lives left :' + str(self.user_life)

    # Method for game over determination
    def game_over(self):
        if self.user_score == self.brick_count:
            return True
        elif self.user_life > 0:
            self.reset_ball()
        else:
            return True

    # Getter for ball movement attributes
    def get_ball_x(self):
        return self._dx

    def get_ball_y(self):
        return self._dy


def color_setter(x):
    num = x
    # random.choice(range(10))
    if num == 0:
        return "red"
    elif num == 1:
        return "cyan"
    elif num == 2:
        return "teal"
    elif num == 3:
        return "orange"
    elif num == 4:
        return "tan"
    elif num == 5:
        return "blue"
    elif num == 6:
        return "navy"
    elif num == 7:
        return "coral"
    elif num == 8:
        return "grey"
    elif num == 9:
        return "black"

