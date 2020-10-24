import unittest

def number_of_words(line):
    if not isinstance(line, str):
        raise Exception ("Invalid parameter!")
    words = line.split()
    return(len(words))

class TestNumberOfWords(unittest.TestCase):
    def test_correct_line(self):
        line = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        In eget dui nulla. Mauris faucibus posuere ante ut gravida.
        Mauris faucibus volutpat dictum."""
        self.assertEqual(number_of_words(line), 22)

    def test_correct_line_with_tab(self):
        line = """Lorem ipsum dolor sit amet, 
        consectetur                 adipiscing elit."""
        self.assertEqual(number_of_words(line), 8)

    def test_incorrect_line(self):
        line = 5
        with self.assertRaises(Exception):
            number_of_words(line)


if __name__ == "__main__":
    unittest.main()
