"""
File: sierpinski.py
Name: Ralph
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow
DELAY = 0				   # The millisecond for delay

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: The number of orders/layers that the fractal will be structure
	:param length: The length of each side of triangle
	:param upper_left_x: The x-axis representing the upper-left starting point of the triangle
	:param upper_left_y: The y-axis representing the upper-left starting point of the triangle
	:return:
	"""
	h_triangle = length * 0.866  # This is the height of the triangle
	c_triangle = length * 0.5  # This is the width of the triangle from any angle to its center point
	down_x = 0.5 * length / 2 + upper_left_x  # This is the x-axis of center down triangle
	down_y = 0.866 * length / 2 + upper_left_y  # This is the y-axis of center down triangle
	if order == 0:
		return
	else:
		# pinpoint the starting point of left triangle
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# pinpoint the starting point of upper right triangle
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)
		# pinpoint the starting point of center down triangle
		sierpinski_triangle(order - 1, length / 2, down_x, down_y)
		# draw each side of triangle
		line_1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		line_1.color = 'black'
		line_2 = GLine(upper_left_x, upper_left_y, upper_left_x + c_triangle, upper_left_y + h_triangle)
		line_2.color = 'red'
		line_3 = GLine(upper_left_x + c_triangle, upper_left_y + h_triangle, upper_left_x + length, upper_left_y)
		line_3.color = 'blue'
		window.add(line_1)
		window.add(line_2)
		window.add(line_3)
		pause(DELAY)



if __name__ == '__main__':
	main()