from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    num_lives = NUM_LIVES

    while True:
        dx = graphics.get_speed_x()
        dy = graphics.get_speed_y()
        # 1.update
        graphics.ball.move(dx, dy)
        # 2.check
        # 2.1 bounce check
        if graphics.ball.x + graphics.ball_radius*2 >= graphics.window.width or graphics.ball.x <= 0:
            graphics.set_x(-dx)
        if graphics.ball.y + graphics.ball_radius*2 >= graphics.window.height or graphics.ball.y <= 0:
            graphics.set_y(-dy)
        # 2.2 collision check
        graphics.collision_check()
        # 2.3 falling check
        if graphics.ball.y + graphics.ball_radius*2 >= graphics.window.height:
            graphics.change_position()
            graphics.set_x(0)
            graphics.set_y(0)
            num_lives -= 1
            if num_lives == 0:
                break
        if graphics.check_brick():
            break
        # 3.pause
        pause(FRAME_RATE)





if __name__ == '__main__':
    main()
