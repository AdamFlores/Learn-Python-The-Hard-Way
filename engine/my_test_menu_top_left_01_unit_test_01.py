# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

testinfo = "s, q"
tags = "menu, menu_valign, menu_halign"

from pyglet import image
from pyglet.gl import *
from pyglet import font

from cocos.director import *
from cocos.menu import *
from cocos.scene import *
from cocos.layer import *

class MainMenu(Menu):
    def __init__( self ):
        super( MainMenu, self ).__init__("Media Mogul Version 0.02" )

        self.menu_valign = TOP
        self.menu_halign = LEFT

        # then add the items
        items = [
            ( MenuItem('Play Game Mode 1', self.on_quit ) ),
            ( MenuItem('Debug Mode 1', self.on_quit ) ),
            ( MenuItem('Edit Mode 1', self.on_quit ) ),
            ( MenuItem('Data Mode 1', self.on_quit ) ),

        ]

        self.create_menu( items, selected_effect=zoom_in(),
                          unselected_effect=zoom_out())

    def on_quit( self ):
        pyglet.app.exit()

def main():

    pyglet.font.add_directory('.')

    director.init( resizable=True)
    director.run( Scene( MainMenu() ) )

if __name__ == '__main__':
    main()
