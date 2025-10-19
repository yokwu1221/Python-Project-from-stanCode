"""
File: bouncing_ball
Name: Yok
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
point = GOval(SIZE, SIZE) # global
point.filled = True
window.add(point, x=START_X, y=START_Y)
count = 0

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(start)

def start(event):
    global count
    if count < 3 and point.x == 30:     # 跟mouse位置沒關係，
        vy = 0
        while True:  #改成count
            point.move(VX, vy)
            vy += GRAVITY
            if point.x + point.width >= window.width:
                point.x = START_X
                point.y = START_Y
                count += 1
            if point.y + point.height >= window.height:  # bounce back
                if vy > 0:
                    vy = -vy * REDUCE
            if count == 3:
                break
            pause(DELAY)


if __name__ == "__main__":
    main()
