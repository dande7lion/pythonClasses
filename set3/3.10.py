import unittest

# different way to create dictionary:
# roman_directory = {}
# roman_directory["I"] = 1
# roman_directory["V"] = 5
# roman_directory["X"] = 10
# roman_directory["L"] = 50
# roman_directory["C"] = 100
# roman_directory["D"] = 500
# roman_directory["M"] = 1000

roman_directory = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def change_roman_to_arabic(roman_number):
    result = 0
    for character in range(len(roman_number)):
        if (character > 0) and (roman_directory[roman_number[character]] > roman_directory[roman_number[character-1]]):
            result += roman_directory[roman_number[character]] - 2 * roman_directory[roman_number[character-1]]
        else:
            result += roman_directory[roman_number[character]]
    return result

class TestChangeRomanToArabic(unittest.TestCase):
    def test_change_roman_to_arabic(self):
        self.assertEqual(change_roman_to_arabic("XV"), 15)
        self.assertEqual(change_roman_to_arabic("IV"), 4)
        self.assertEqual(change_roman_to_arabic("MD"), 1500)
        self.assertEqual(change_roman_to_arabic("XII"), 12)

if __name__ == "__main__":
    unittest.main()