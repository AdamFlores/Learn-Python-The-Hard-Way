import cocos
import unittest
import mock
#replace cocos Layer object with a mock

class DirectorUnitTest03(unittest.TestCase):
    def setup(self):
       #     def mock_layer(mock):
       #         return cocos.layer.Layer
            class HelloWorld(mock):
                def __init__(self):
                    super( HelloWorld, self ).__init__()
    def test_director_init(self):
                if __name__ == "__main__":
                    # director init takes the same arguments as pyglet.window
                    cocos.director.director.init()

if __name__ == "__main__":
    unittest.main()