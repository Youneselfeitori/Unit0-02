#Created by: Younes Elfeitori
#Created on: 15 Sep 2017
#Created for : ICS3U
#This program is the hello world progrem but with 3 buttons


import ui

def english_touch_up_inside(sender):
    #Displays english version
    view['hello_world_label'].text = ('Hello, World!')
    
def french_touch_up_inside(sender):
    #Displays french version
    view['hello_world_label'].text = ('Bonjor le monde')
    
def spanish_touch_up_inside(sender):
    #Displays spanish version
    view['hello_world_label'].text = ('Hola Mundo')
	
view = ui.load_view()
view.present('sheet')
