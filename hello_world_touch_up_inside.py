#Created by: Younes Elfeitori
#Created on: 13Sep 2013
#Created for: ICS3U
#Daily Assignment: Unit0-02
#This program displays Hello World but in GUI format

import ui

def hello_world_touch_up_inside(sender):
    print ('Hello, World!')
    #view['hello_world_label'].text = ("Hello, World!")

view = ui.load_view()
view.present('sheet')
