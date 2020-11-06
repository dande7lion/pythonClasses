import unittest

def factorial(n):
    result = 1
    if n == 0:
        return result
    for i in range(n):
        result = result * ( i+1 )
    return result

class TestFactiorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(0), 1)

if __name__ == "__main__":
    unittest.main()