import unittest

def underscore_between_letters(word):
    if not isinstance(word, str):
        raise TypeError ("Invalid parameter")
    return "_".join(word)

class TestUnderscoreBetweenLetters(unittest.TestCase):
    def test_correct_data(self):
        self.assertEqual(underscore_between_letters("word"), "w_o_r_d")

    def test_incorrect_data(self):
        with self.assertRaises(TypeError):
            underscore_between_letters(5)

if __name__ == "__main__":
    unittest.main()
