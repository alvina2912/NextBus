import unittest
import sys
from Modules import DirectionModule

class test_DirectionModule(unittest.TestCase):
    def test_getDirectionValue_valid(self):
        self.assertEqual(DirectionModule.getDirectionValue('903','north'),'4' )

    def test_getDirectionValue_invalid(self):
        self.assertEqual( DirectionModule.getDirectionValue('903','test'),None)
        self.assertEqual(DirectionModule.getDirectionValue('000','north'),None)

if __name__ == '__main__':
    unittest.main()
