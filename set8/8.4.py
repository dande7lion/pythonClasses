import math
import unittest

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)) or not isinstance(c, (float, int)):
        raise TypeError("Incorrect input - parameters need to be numbers")
    if a + b < c or a + c < b or b + c < a:
        raise ValueError("Nieprawidlowe dlugosci bokow")
    # p - połowa obwodu trójkąta
    p = ( a + b + c ) / 2
    # S - pole trójkąta
    S = math.sqrt( p * ( p - a ) * ( p - b ) * ( p - c ) )
    return S   

class TestHeron(unittest.TestCase):
    def test_heron(self):
        self.assertEqual(heron(3, 4, 5), 6.0)
        with self.assertRaises(ValueError):
            heron(13, 4, 18)
        with self.assertRaises(TypeError):
            heron("a", 7, 7)

if __name__ == "__main__":
    unittest.main()