"""
File: draw_line
Name: Yok
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 10
window = GWindow()
old_x = 0
old_y = 0
n = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_point)


def create_point(mouse):
    global old_x, old_y, n
    n += 1
    if n % 2 != 0:
        point = GOval(SIZE, SIZE, x=mouse.x, y=mouse.y)
        window.add(point)
        old_x = mouse.x
        old_y = mouse.y
    else:           # 改為先移除舊point在畫線，避免移除舊point時連線一起移除了
        old_point = window.get_object_at(old_x + SIZE/2, old_y)  # 需要觸碰到OBJECT, 不須考慮空心或實心
        window.remove(old_point)
        line = GLine(old_x, old_y, mouse.x, mouse.y)
        window.add(line)


if __name__ == "__main__":
    main()
