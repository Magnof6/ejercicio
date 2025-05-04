import unittest
from rectangulo import Rectangle

class Test_Rectangle(unittest.TestCase):
    def test_creation_valid(self):
        rectan = Rectangle(0,0,10,10)
        self.assertEqual(rectan.xmin,0)
        self.assertEqual(rectan.ymin,0)
        self.assertEqual(rectan.xmax,10)
        self.assertEqual(rectan.ymax,10)

    def test_creation_invalid(self):
        with self.assertRaises(ValueError):
            Rectangle(10,0,0,10) # xmin > xmax --> debe fallar
        with self.assertRaises(ValueError):
            Rectangle(0,10,0,10) #ymin > ymax --> debe fallar
    
    def test_area(self):
        rect = Rectangle(0,0,10,10)
        self.assertEqual(rect.area(),100)
    
    def test_perimetro(self):
        rect = Rectangle(0,0,10,20)
        self.assertEqual(rect.perimetro(),60)

    def test_centro(self):
        rect = Rectangle(0,0,10,10)
        self.assertEqual(rect.centro(),(5,5))
    def test_diagonal(self):
        rect = Rectangle(0,0,3,4)
        self.assertEqual(rect.diagonal(),5)
    
    def test_overlap(self):
        rect1 = Rectangle(0,0,10,10)
        rect2 = Rectangle(5,5,15,15)
        rect3 = Rectangle(11,11,20,20)

        self.assertTrue(rect1.overlaps(rect2))
        self.assertTrue(rect2.overlaps(rect1))
        self.assertTrue(rect2.overlaps(rect3))
        self.assertTrue(rect3.overlaps(rect2))
        self.assertFalse(rect1.overlaps(rect3))
        self.assertFalse(rect3.overlaps(rect1))
    






















