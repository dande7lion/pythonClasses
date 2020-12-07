import unittest

def solveP(i, j):
    if not isinstance (i, (float, int)) or not isinstance (j, (float, int)):
        raise TypeError("Parameters need to be numbers!")
    if i < 0 or j < 0:
        raise ValueError("Parameters can not be negative")
    P = {}
    P[(0, 0)] = 0.5

    for k in range (1, j + 1):
        P[(0, k)] = 1.0

    for k in range (1, i + 1):
        P[(k, 0)] = 0.0
        for l in range (1, j + 1):
            P[(k, l)] = 0.5 * P[(k - 1, l)] + P[(k, l - 1)]

    return P.get((i, j))

class TestSolveP(unittest.TestCase):
    def test_solveP(self):
        self.assertEqual(solveP(0, 0), 0.5)
        self.assertEqual(solveP(5, 0), 0.0)
        self.assertEqual(solveP(0, 7), 1.0)
        self.assertEqual(solveP(1, 2), 1.0)
        with self.assertRaises(TypeError):
            solveP("a", 2)
        with self.assertRaises(ValueError):
            solveP(2, -1)

if __name__ == "__main__":
    unittest.main()