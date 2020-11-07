import unittest

def sum_seq(sequence):
    sum = 0
    for element in sequence:
        if (isinstance(element, (list, tuple))):
            sum += sum_seq(element)
        else:
            sum += element
    return sum

class TestSumSequence(unittest.TestCase):
    def test_sum_seq(self):
        self.assertEqual(sum_seq([1, 2, 3, [4, 5], (6, 7)]), 28)
        self.assertEqual(sum_seq([10, 10, (10, 10, [10, [10, 10]]), [10, [10, (10, 10)], 10]]), 120)

if __name__ == "__main__":
    unittest.main()