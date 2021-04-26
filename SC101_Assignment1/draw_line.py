"""
File: draw_line.py
Name: Ralph Liu
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow, pause
from campy.gui.events.mouse import onmouseclicked

# Global variable
window = GWindow()
m_click = 0
SIZE = 10
oval = GOval(SIZE, SIZE)
start_x = 0
start_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    """
    :param mouse: This is to track the position of the mouse cursor on x and y axis
    :return: The module does not return anything but to enable user to pinpoint the starting point of a line by a oval
    When user clicks the 2nd time, there will be a line connecting the starting point (The center of oval) to the
    ending point
    """
    # Thi is to count the mouse click to differentiate even and odd clicks
    global m_click
    # These 2 variables are to store the position of the first click
    global start_x
    global start_y
    m_click += 1
    if m_click % 2 != 0:
        window.add(oval, x=mouse.x - oval.width / 2, y=mouse.y - oval.height / 2)
        start_x = mouse.x
        start_y = mouse.y
    else:
        line = GLine(start_x, start_y, mouse.x, mouse.y)
        window.add(line)
        window.remove(oval)


if __name__ == "__main__":
    main()
