
# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This program calculates the area and perimter of a rectangle

import ui

def answer_touch_up_inside(sender):
    # displays the answer for area and perimeter
    view['area_answer_label'].text = 'Area = ' + str(3*5) + ' cm^2'
    view['perimeter_answer_label'].text = 'Perimeter = ' + str(2*(5+3)) + ' cm'

view = ui.load_view()
view.present('full_screen')
import ui

view = ui.load_view()
view.present('sheet')
