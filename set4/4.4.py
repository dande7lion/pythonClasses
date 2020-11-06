import unittest

def fibonacci(n):
    elem_n_2 = 0
    elem_n_1 = 1
    elem_current = 0

    if n == 0:
        return elem_current
        
    index = 1

    while index is not n:
        elem_current = elem_n_1 + elem_n_2
        elem_n_2 = elem_n_1
        elem_n_1 = elem_current
        index += 1

    return elem_current

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 0)
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(14), 377)

if __name__ == "__main__":
    unittest.main()