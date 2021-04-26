"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import random
import babygraphicsgui as gui


FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 500
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    starting_x = 0 + GRAPH_MARGIN_SIZE
    num_year = len(YEARS)
    total_width_interval = (width - GRAPH_MARGIN_SIZE) - (0 + GRAPH_MARGIN_SIZE)
    width_interval = total_width_interval / num_year
    x_coordinate = starting_x + year_index * width_interval
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(0 + GRAPH_MARGIN_SIZE, 0 + GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, \
                       0 + GRAPH_MARGIN_SIZE)
    canvas.create_line(0 + GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, \
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    canvas.create_line(0 + GRAPH_MARGIN_SIZE, 0, 0 + GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    canvas.create_line(CANVAS_WIDTH - GRAPH_MARGIN_SIZE, 0, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    num_year = len(YEARS)
    for i in range(num_year):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, fill='black', font='times 8 italic bold', \
                           text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    draw_run = len(YEARS) - 1  # Number of runs needed to plot the graph
    x_lst = []  # The list to hold the x coordinate for each year
    rank_lst = []  # The list to hold the actual ranking of a name for each year
    draw_rank_lst = []  # The list to hold the y coordinate for each year to represent ranking
    scale_adjuster = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK  # This is the conversion factor between
    # actual ranking and the y coordinate for graph plot

    for i in range(len(lookup_names)):
        color = COLORS[i % len(COLORS)]  # Circular in color index
        name_to_check = lookup_names[i]
        for j in range(len(YEARS)):
            x = int(get_x_coordinate(CANVAS_WIDTH, j))
            x_lst.append(x)
            year_to_check = str(YEARS[j])
            name_exist = name_data[name_to_check].get(year_to_check)
            if name_exist is None:
                year_rank = 0
                draw_rank = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                year_rank = int(name_data[name_to_check][year_to_check])
                draw_rank = int(year_rank * scale_adjuster) + GRAPH_MARGIN_SIZE
            rank_lst.append(year_rank)
            draw_rank_lst.append(draw_rank)
        for k in range(0, draw_run, 1):
            canvas.create_line(x_lst[k], draw_rank_lst[k], x_lst[k + 1], draw_rank_lst[k + 1], \
                               width=LINE_WIDTH, fill=color)
        for n in range(0, draw_run + 1, 1):
            if rank_lst[n] == 0:
                canvas.create_text(x_lst[n] + TEXT_DX, draw_rank_lst[n], fill='black', font='times 8 italic bold', \
                                   text=str(name_to_check) + ' : ' + str('**'), anchor=tkinter.S)
            else:
                canvas.create_text(x_lst[n] + TEXT_DX, draw_rank_lst[n], fill='black', font='times 8 italic bold', \
                                   text=str(name_to_check) + ' : ' + str(rank_lst[n]), anchor=tkinter.S)
        x_lst = []
        rank_lst = []
        draw_rank_lst = []


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
