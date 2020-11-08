import unittest

def flatten(sequence):
    result =[]
    for element in sequence:
        if isinstance(element, (list, tuple)):
            result += (flatten(element))
        else:
            result.append(element)
    return result

class TestFlatten(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(flatten([1, 2, [3, 4], 5, (6, 7, 8), 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(flatten([2, 13, (14, 15, [16, [17, 20]], 14), 18]), [2, 13, 14, 15, 16, 17, 20, 14, 18])

if __name__ == "__main__":
    unittest.main()