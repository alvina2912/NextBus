import unittest
import sys
from Modules import TransitStopModule

class test_TransitStopModule(unittest.TestCase):
    def test_getStopValue_valid(self):
        self.assertEqual(TransitStopModule.getStopValue('903','4','147th St Station'),'CE47' )

    def test_getStopValue_invalid(self):
        self.assertEqual( TransitStopModule.getStopValue('903','4','test'),None)
        self.assertEqual(TransitStopModule.getStopValue('000','4','Cedar Grove Transit Station'),None)

if __name__ == '__main__':
    unittest.main()
