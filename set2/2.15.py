import unittest

def create_string_from_list(numbers_list):
    result_string = ""
    for number in numbers_list:
        result_string += str(number)
    return result_string

class TestCreateStringFromList(unittest.TestCase):
    def test_only_single_numbers(self):
        self.assertEqual(create_string_from_list([1,2,3,4]), "1234")

    def test_different_numbers(self):
        self.assertEqual(create_string_from_list([23,45,87,2,896]), "2345872896")

    def test_empty_list(self):
        self.assertEqual(create_string_from_list([""]), "")

if __name__ == "__main__":
    unittest.main()