#
# cocos2d
# http://cocos2d.org
#
# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#


import cocos
from cocos.director import director
from cocos.actions import *
from cocos.layer import *
import pyglet

class TestLayer(cocos.layer.Layer):
    def __init__(self):
        super( TestLayer, self ).__init__()
        x,y = director.get_window_size()
        
if __name__ == "__main__":
    director.init( resizable=False )
    #main_scene = cocos.scene.Scene()
    main_scene = cocos.scene.Scene() #Bulk of "processing" not "events" will handle in Scene
    intro_scene = cocos.scene.Scene()
    attract_mode_scene = cocos.scene.Scene()
    city_map_mode_scene = cocos.scene.Scene()
    office_mode_scene = cocos.scene.Scene()
    #main_scene.transform_anchor = (320,240)
    #child1_scene = cocos.scene.Scene()
    #child1_scene.add( ColorLayer( 0,0,255,255 ) )
    #child1_scene.scale = 1.5
    #child1_scene.position = (-160,-120)
    #child1_scene.transform_anchor = (320,240)
    #main_scene.add( child1_scene )
    #director.run (main_scene)
    director.run (main_scene)