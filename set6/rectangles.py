from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    # "[(x1, y1), (x2, y2)]"
    def __str__(self):
        return f"[{self.pt1.__str__()}, {self.pt2.__str__()}]"

    # "Rectangle(x1, y1, x2, y2)"
    def __repr__(self): 
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"   

    # obsługa rect1 == rect2
    def __eq__(self, other): 
        return self.pt2.__sub__(self.pt1) == other.pt2.__sub__(other.pt1) 

    # obsługa rect1 != rect2
    def __ne__(self, other):        
        return not self.__eq__(other)

    # zwraca środek prostokąta
    def center(self):
        return Point((self.pt2.x - (self.pt2.x - self.pt1.x) / 2), self.pt2.y - ((self.pt2.y - self.pt1.y) / 2))

    # pole powierzchni
    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    # przesunięcie o (x, y)
    def move(self, x, y): 
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y) 

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle1 = Rectangle(1, 1, 5, 4)
        self.rectangle2 = Rectangle(1, 5, 5, 8)
        self.rectangle3 = Rectangle(1, 2, 3, 4)

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            Rectangle("a", "b", "c", "d")
        with self.assertRaises(TypeError):
            Rectangle(3, "h", 4, 8)

    def test_str(self):
        self.assertEqual(self.rectangle1.__str__(), "[(1, 1), (5, 4)]")
        self.assertEqual(self.rectangle2.__str__(), "[(1, 5), (5, 8)]")
        self.assertEqual(self.rectangle3.__str__(), "[(1, 2), (3, 4)]")

    def test_repr(self):
        self.assertEqual(self.rectangle1.__repr__(), "Rectangle(1, 1, 5, 4)")
        self.assertEqual(self.rectangle2.__repr__(), "Rectangle(1, 5, 5, 8)")
        self.assertEqual(self.rectangle3.__repr__(), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        self.assertTrue(self.rectangle1.__eq__(self.rectangle2))
        self.assertFalse(self.rectangle1.__eq__(self.rectangle3))
        self.assertTrue(self.rectangle1.__eq__(self.rectangle1))

    def test_ne(self):
        self.assertFalse(self.rectangle1.__ne__(self.rectangle2))
        self.assertTrue(self.rectangle1.__ne__(self.rectangle3))
        self.assertFalse(self.rectangle3.__ne__(self.rectangle3))

    def test_center(self):
        self.assertEqual(self.rectangle1.center(), Point(3, 2.5))
        self.assertEqual(self.rectangle2.center(), Point(3, 6.5))
        self.assertEqual(self.rectangle3.center(), Point(2, 3))

    def test_area(self):
        self.assertEqual(self.rectangle1.area(), 12)
        self.assertEqual(self.rectangle3.area(), 4)
        self.assertEqual(self.rectangle2.area(), 12)

    def test_move(self):
        self.assertEqual(self.rectangle1.move(2, 8), Rectangle(3, 9, 7, 12))
        self.assertEqual(self.rectangle2.move(-1, 1), Rectangle(0, 6, 4, 9))
        self.assertEqual(self.rectangle3.move(5, -2), Rectangle(6, 0, 8, 2))

if __name__ == "__main__":
    unittest.main()