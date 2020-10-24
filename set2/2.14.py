import unittest

def find_the_longest_word(line):
    if not isinstance(line, str):
        raise TypeError("Invalid parameter!")
    line=line.split()
    the_longest_word = ""
    length_of_the_longest_word = 0
    for word in line:
        length = len(word)
        if length > length_of_the_longest_word:
            length_of_the_longest_word = length
            the_longest_word = word
    return the_longest_word, length_of_the_longest_word

class TestFindTheLongestWord(unittest.TestCase):
    def test_correct_data(self):
        self.assertEqual(find_the_longest_word(""), ("", 0))
        line = """Lorem ipsum dolor 
        sit amet, consectetur adipiscing elit
        In eget dui nulla"""
        self.assertEqual(find_the_longest_word(line), ("consectetur", 11))

    def test_incorrect_data(self):
        with self.assertRaises(TypeError):
            find_the_longest_word(458)

if __name__ == "__main__":
    unittest.main()