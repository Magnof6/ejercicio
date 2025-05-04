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























