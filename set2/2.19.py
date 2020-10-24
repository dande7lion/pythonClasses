import unittest

def prepare_three_blocks_word(list_of_numbers):
    list_of_numbers = [str(number).zfill(3) for number in list_of_numbers]
    return " ".join(list_of_numbers)
    

class TestPrepareThreeBlocksWord(unittest.TestCase):
    def test_prepare_word(self):
        L = [87, 2, 25, 786, 48]
        self.assertEqual(prepare_three_blocks_word(L), "087 002 025 786 048")
        L = [1, 20, 300, 4, 50, 600]
        self.assertEqual(prepare_three_blocks_word(L), "001 020 300 004 050 600")

if __name__ == "__main__":
    unittest.main()