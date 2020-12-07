import unittest

def solve1(a, b, c):
    """Rozwiązanie równania liniowego a x + b y + c = 0"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Parameters need to be numbers!")
    i = 0
    c1 = -c
    while i * a <= c:
        if (c1 - (i * a)) % b == 0:
            return i, int((c1 - (i * a)) / b)
        i = i + 1
    return 0

class TestSolve (unittest.TestCase):
    def test_solve1(self):
        self.assertEqual(solve1(3, -2, 4), (0, 2))
        self.assertEqual(solve1(5, 8, -4), 0)
        with self.assertRaises(TypeError):
            solve1("a", 3 ,4)

if __name__ == "__main__":
    unittest.main()