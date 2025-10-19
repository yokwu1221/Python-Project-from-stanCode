from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 5    # Initial vertical speed for the ball
MAX_X_SPEED = 2        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x = window_width/2 - paddle_width/2, y = window_height - paddle_offset - paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2 - ball_radius, y=window_height/2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.start_ball)
        onmousemoved(self.handle_move)

        # Draw bricks
        self.color = "black"
        self.brick_number = 0
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick_x = j * (brick_width + brick_spacing)
                brick_y = brick_offset + i * (brick_height + brick_spacing)
                self.brick = GRect(brick_width, brick_height, x=brick_x, y=brick_y)
                if (i+1) % 2 == 1 and j == 0:
                    self.change_color()
                self.brick.filled = True
                self.brick.fill_color = self.color
                self.brick.color = self.color
                self.window.add(self.brick)
                self.brick_number += 1
        self.brick_remove_number = 0

    def change_color(self):
        if self.color == "black":
            self.color = "red"
        elif self.color == "red":
            self.color = "orange"
        elif self.color == "orange":
            self.color = "yellow"
        elif self.color == "yellow":
            self.color = "green"
        elif self.color == "green":
            self.color = "blue"
        elif self.color == "blue":
            self.color = "red"


    def handle_move(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width/2
        if mouse.x < self.paddle.width/2:
            self.paddle.x = 0
        if mouse.x > self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width


    def start_ball(self, event):
        if self.ball.y + self.ball_radius*2 >= self.window.height:
            self.change_position()
            self.__dx = 0
            self.__dy = 0
        if self.__dx != 0 or self.__dy != 0:        # already moving
            pass
        else:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = - self.__dx
            self.__dy = INITIAL_Y_SPEED


    def get_speed_x(self):                          #　ball bounce
        return self.__dx


    def get_speed_y(self):                          #　ball bounce
        return self.__dy


    def set_x(self, new_x):
        self.__dx = new_x


    def set_y(self, new_y):
        self.__dy = new_y


    def collision_check(self):
        a = True
        for x in range(2):
            for y in range(2):
                maybe_object = self.window.get_object_at(self.ball.x + x * self.ball_radius * 2, self.ball.y + y * self.ball_radius *2)

                if maybe_object is not None:        
                    if maybe_object is self.paddle:
                        if self.__dy > 0:
                            self.__dy = -self.__dy      
                    else:                          
                        self.window.remove(maybe_object)
                        if a:
                            self.__dy = -self.__dy
                            a = False
                        self.brick_remove_number += 1


    def change_position(self):
        self.ball.x = self.window.width/2 - self.ball_radius
        self.ball.y = self.window.height/2 - self.ball_radius


    def check_brick(self):
        if self.brick_remove_number == self.brick_number:
            return True
        return False
