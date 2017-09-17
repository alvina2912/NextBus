import unittest
import sys
sys.path.append('../Modules')
import DirectionModule

class DirectionModuleTest(unittest.TestCase):


    def test_getDirectionValue_valid(self):
        self.assertEqual(DirectionModule.getDirectionValue('903','north'),'4' )

    def test_getDirectionValue_invalid(self):
        self.assertEqual( DirectionModule.getDirectionValue('903','test'),None)
        self.assertEqual(DirectionModule.getDirectionValue('000','north'),None)

if __name__ == '__main__':
    unittest.main()
