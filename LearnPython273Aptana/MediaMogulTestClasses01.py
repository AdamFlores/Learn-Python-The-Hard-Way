from mock import Mock
from mock import MagicMock

class ProductionClass(object):
    def method(self):
        self.something(1,2,3)
        def something(self, a, b, c):
            pass
        
mock = Mock()
mock.method(1,2,3, test='wow')
mock.method.assert_called_with(1,2,3, test='wow')
print "mock test 01 called"

real = ProductionClass()
real.something = MagicMock()
real.method()
real.something.assert_called_once_with(1,2,3)

	