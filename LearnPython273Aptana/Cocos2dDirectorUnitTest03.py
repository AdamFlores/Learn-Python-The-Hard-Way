import cocos
import unittest
import mock
#replace cocos Layer object with a mock

class DirectorUnitTest02(unittest.TestCase):
    def setup(self):
            class MockLayer(cocos.layer.Layer):
                
            class HelloWorld(cocos.layer.Layer):
                def __init__(self):
                    super( HelloWorld, self ).__init__()
    def test_director_init(self):
                if __name__ == "__main__":
                    # director init takes the same arguments as pyglet.window
                    cocos.director.director.init()

if __name__ == "__main__":
    unittest.main()