import unittest

def total_length_of_words(line):
    if not isinstance(line, str):
        raise TypeError("Invalid parameter!")
    line = line.split()
    total_length = 0
    for word in line:
        total_length += len(word)
    return total_length

class TestTotalLengthOfWords(unittest.TestCase):
    def test_correct_data(self):
        line = """Lorem ipsum dolor 
        sit amet, consectetur adipiscing elit
        In eget dui nulla"""
        self.assertEqual(total_length_of_words(line), 62)

    def test_incorrect_data(self):
        with self.assertRaises(TypeError):
            total_length_of_words(5)



if __name__=="__main__":
    unittest.main()