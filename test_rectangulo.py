import unittest
from rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    def test_creation_valid(self):
        rectan = Rectangle(0,0,10,10)
        self.assertEqual(rectan.xmin,0)
        self.assertEqual(rectan.ymin,0)
        self.assertEqual(rectan.xmax,10)
        self.assertEqual(rect.ymax,10)
