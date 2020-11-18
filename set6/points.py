import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

     # konstuktor
    def __init__(self, x, y): 
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordiantes need to be numbers!")
        self.x = x
        self.y = y

    # zwraca string "(x, y)"
    def __str__(self):
        return f"({self.x}, {self.y})"   

    # zwraca string "Point(x, y)"
    def __repr__(self):
        return f"Point ({self.x}, {self.y})"

    # obsługa point1 == point2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # obsługa point1 != point2
    def __ne__(self, other):        
        return not self.x == other.x and self.y == other.y

    # Punkty jako wektory 2D.

    # v1 + v2
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # v1 - v2
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # v1 * v2, iloczyn skalarny
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    # v1 x v2, iloczyn wektorowy 2D
    def cross(self, other):         
        return Point(self.x * other.y, - self.y * other.x)

    # długość wektora
    def length(self):
        return round(math.sqrt(self.x**2 + self.y**2), 2)

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.point1 = Point(3, 5)
        self.point2 = Point(-5, 7)
        self.point3 = Point(1, 2)
        self.point4 = Point(3, -5)

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            Point("a", "b")
        with self.assertRaises(TypeError):
            Point("/", ":")

    def test_str(self):
        self.assertEqual(self.point1.__str__(), "(3, 5)")
        self.assertEqual(self.point2.__str__(), "(-5, 7)")
        self.assertEqual(self.point3.__str__(), "(1, 2)")

    def test_repr(self):
        self.assertEqual(self.point1.__repr__(), "Point (3, 5)")
        self.assertEqual(self.point2.__repr__(), "Point (-5, 7)")
        self.assertEqual(self.point3.__repr__(), "Point (1, 2)")

    def test_eq(self):
        self.assertTrue(self.point1.__eq__(Point(3, 5)))
        self.assertFalse(self.point2.__eq__(Point(5 ,3)))
        self.assertFalse(self.point3.__eq__(Point(17 ,3)))

    def test_ne(self):
        self.assertTrue(self.point1.__ne__(Point(2, 5)))
        self.assertFalse(self.point2.__ne__(Point(-5, 7)))
        self.assertFalse(self.point4.__ne__(Point(3, -5)))

    def test_add(self):
        self.assertEqual(self.point1.__add__(self.point2), Point(-2, 12))
        self.assertEqual(self.point2.__add__(self.point3), Point(-4, 9))
        self.assertEqual(self.point3.__add__(self.point4), Point(4, -3))

    def test_sub(self):
        self.assertEqual(self.point1.__sub__(self.point2), Point(8, -2))
        self.assertEqual(self.point2.__sub__(self.point3), Point(-6, 5))
        self.assertEqual(self.point3.__sub__(self.point4), Point(-2, 7))

    def test_mul(self):
        self.assertEqual(self.point3.__mul__(self.point4), -7)
        self.assertEqual(self.point1.__mul__(self.point2), 20)
        self.assertEqual(self.point2.__mul__(self.point4), -50)

    def test_cross(self):
        self.assertEqual(self.point1.cross(self.point2), Point(21, 25))
        self.assertEqual(self.point2.cross(self.point3), Point(-10, -7))
        self.assertEqual(self.point3.cross(self.point4), Point(-5, -6))

    def test_length(self):
        self.assertEqual(self.point1.length(), 5.83)
        self.assertEqual(self.point2.length(), 8.60)
        self.assertEqual(self.point3.length(), 2.24)
        self.assertEqual(self.point4.length(), 5.83)

if __name__ == "__main__":
    unittest.main()