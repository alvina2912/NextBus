import unittest
import sys
sys.path.append('../Modules')
import RouteIDModule

class RouteIDModuleTest(unittest.TestCase):


    def test_getRouteID_valid(self):
        self.assertEqual(RouteIDModule.getRouteID('METRO Red Line'),'903' )

    def test_getRouteID_invalid(self):
        self.assertEqual( RouteIDModule.getRouteID('test'),None)

if __name__ == '__main__':
    unittest.main()
