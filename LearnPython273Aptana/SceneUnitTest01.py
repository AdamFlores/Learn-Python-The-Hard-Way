import cocos
import unittest



class SceneUnitTest02(unittest.TestCase):
    def setup(self):
            class HelloWorld(cocos.layer.Layer):
                def __init__(self):
                    super( HelloWorld, self ).__init__()
    def test_scene_init(self):
                if __name__ == "__main__":
                    # director init takes the same arguments as pyglet.window
                    cocos.director.director.init()
                    self.hello_layer = cocos.layer.Layer
                    self.main_scene = cocos.scene.Scene (self.hello_layer)
                    #cocos.director.director.run (self.main_scene)
                    #self.director.run( cocos.scene.Scene( self.HelloWorld() ) )

if __name__ == "__main__":
    unittest.main()