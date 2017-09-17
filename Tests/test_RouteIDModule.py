import unittest
import sys
from Modules import RouteIDModule

class test_RouteIDModule(unittest.TestCase):
    def test_getRouteID_valid(self):
        self.assertEqual(RouteIDModule.getRouteID('METRO Red Line'),'903' )

    def test_getRouteID_invalid(self):
        self.assertEqual( RouteIDModule.getRouteID('test'),None)

if __name__ == '__main__':
    unittest.main()
