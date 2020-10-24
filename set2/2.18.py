import unittest
import re

def find_number_of_zeros(number):
    if not isinstance(number, int):
        raise TypeError("InvalidParameter")
    number = str(number)
    return len(re.findall("0", number))
    
class TestFindNumberOfZeros(unittest.TestCase):
    def test_correct_positive_number(self):
        self.assertEqual(find_number_of_zeros(218040009600), 6)

    def test_correct_negative_number(self):
        self.assertEqual(find_number_of_zeros(-2587106080), 3)

    def test_incorrect_data(self):
        with self.assertRaises(TypeError):
            find_number_of_zeros(120.87)

if __name__ == "__main__":
    unittest.main()