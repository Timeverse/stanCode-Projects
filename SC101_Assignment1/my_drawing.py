"""
File: 
Name: Ralph Liu
----------------------
TODO: This is to draw a picture using the elements of GObjects
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: The codes draws a picture of Taipei 101 with the label of 'stanCode 最高!'
    Sending the message out that stanCode is the best coding school in Taiwan
    """
    window = GWindow(800, 500)
    # This is the base of 101
    building_base = GPolygon()
    building_base.add_vertex((300, 500))
    building_base.add_vertex((500, 500))
    building_base.add_vertex((450, 400))
    building_base.add_vertex((350, 400))
    building_base.filled = True
    building_base.fill_color = 'teal'
    window.add(building_base)

    # This is the layers of the building (AKA the bamboo)
    bamboo_1 = GPolygon()
    bamboo_1.add_vertex((360, 400))
    bamboo_1.add_vertex((440, 400))
    bamboo_1.add_vertex((460, 350))
    bamboo_1.add_vertex((340, 350))
    bamboo_1.filled = True
    bamboo_1.fill_color = 'teal'
    window.add(bamboo_1)
    bamboo_2 = GPolygon()
    bamboo_2.add_vertex((360, 350))
    bamboo_2.add_vertex((440, 350))
    bamboo_2.add_vertex((460, 300))
    bamboo_2.add_vertex((340, 300))
    bamboo_2.filled = True
    bamboo_2.fill_color = 'teal'
    window.add(bamboo_2)
    bamboo_3 = GPolygon()
    bamboo_3.add_vertex((360, 300))
    bamboo_3.add_vertex((440, 300))
    bamboo_3.add_vertex((460, 250))
    bamboo_3.add_vertex((340, 250))
    bamboo_3.filled = True
    bamboo_3.fill_color = 'teal'
    window.add(bamboo_3)
    bamboo_4 = GPolygon()
    bamboo_4.add_vertex((360, 250))
    bamboo_4.add_vertex((440, 250))
    bamboo_4.add_vertex((460, 200))
    bamboo_4.add_vertex((340, 200))
    bamboo_4.filled = True
    bamboo_4.fill_color = 'teal'
    window.add(bamboo_4)
    bamboo_5 = GPolygon()
    bamboo_5.add_vertex((360, 200))
    bamboo_5.add_vertex((440, 200))
    bamboo_5.add_vertex((460, 150))
    bamboo_5.add_vertex((340, 150))
    bamboo_5.filled = True
    bamboo_5.fill_color = 'teal'
    window.add(bamboo_5)

    # This is the top of the building
    top_1 = GRect(80, 20)
    top_1.color = 'black'
    top_1.filled = True
    top_1.fill_color = 'teal'
    window.add(top_1, 360, 130)
    top_2 = GPolygon()
    top_2.add_vertex((390, 130))
    top_2.add_vertex((410, 130))
    top_2.add_vertex((420, 80))
    top_2.add_vertex((380, 80))
    top_2.color = 'black'
    top_2.filled = True
    top_2.fill_color = 'teal'
    window.add(top_2)
    top_3 = GLine(400, 80, 400, 20)
    top_3.color = 'black'
    window.add(top_3)

    # This is the chinese coin on top of the building base
    big_coin = GOval(50, 50)
    big_coin.color = 'black'
    big_coin.filled = True
    big_coin.fill_color = 'green'
    window.add(big_coin, 375, 360)
    big_coin_2 = GRect(20, 20)
    big_coin_2.color = 'black'
    big_coin_2.filled = True
    big_coin_2.fill_color = 'gold'
    window.add(big_coin_2, 390, 375)

    # This is the label
    label = GLabel('stanCode 最高!', 100, 100)
    window.add(label)



if __name__ == '__main__':
    main()
