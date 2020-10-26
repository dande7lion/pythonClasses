import unittest

def first_and_last_letters_in_line(line):
    if not isinstance(line, str):
        raise TypeError ("Invalid parameter!")
    line = line.split()
    word_from_first_letters = ""
    word_from_last_letters = ""
    for word in line:
        word = word.strip()
        word_from_first_letters += word[0]
        word_from_last_letters += word[len(word)-1]

    return word_from_first_letters, word_from_last_letters

class WordsFromFirstAndLastLetters(unittest.TestCase):
    def test_correct_data(self):
        line = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
        self.assertEqual(first_and_last_letters_in_line(line), ("Lidsacae", "mmrttrgt"))

    def test_incorrect_data(self):
        with self.assertRaises(TypeError):
            first_and_last_letters_in_line(5)


if __name__ == "__main__":
    unittest.main()