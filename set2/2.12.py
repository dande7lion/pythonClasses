import unittest

def first_and_last_letters_in_line(line):
    if not isinstance(line, str):
        raise Exception ("Invalid parameter!")
    line = line.split("\n")
    word_from_first_letters = ""
    word_from_last_letters = ""
    for one_line in line:
        one_line = one_line.strip()
        word_from_first_letters += one_line[0]
        word_from_last_letters += one_line[len(word_from_last_letters)-1]

    return word_from_first_letters, word_from_last_letters

class WordsFromFirstAndLastLetters(unittest.TestCase):
    def test_correct_line(self):
        line = """Lorem ipsum dolor sit amet, consectetur adipiscing elit
        In eget dui nulla. Mauris faucibus posuere ante ut gravida
        Mauris faucibus volutpat dictum"""
        self.assertEqual(first_and_last_letters_in_line(line), "LIM", "tam")


if __name__ == "__main__":
    unittest.main()