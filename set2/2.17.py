import unittest
from enum import Enum

class SortingType(Enum):
    Alphabetical = 1
    Length = 2

def sort_line(line, sortingType):
    if not isinstance (line, str):
        raise TypeError("Invalid parameter!")
    line = line.split()
    if sortingType == SortingType.Alphabetical:
        line = sorted(line, key=str.lower)
    elif sortingType == SortingType.Length:
        line = sorted(line, key=len)
    else:
        raise Exception("Invalid sorting type")
    return " ".join(line)

class TestSorting(unittest.TestCase):
    def test_alphabetical_sorting(self):
        self.assertEqual(sort_line("Lorem ipsum dolor sit amet", SortingType.Alphabetical), "amet dolor ipsum Lorem sit")
        self.assertEqual(sort_line("LOREM IPSUM DOLOR SIT AMET",SortingType.Alphabetical), "AMET DOLOR IPSUM LOREM SIT")

    def test_length_sorting(self):
        self.assertEqual(sort_line("Lorem ipsum dolor sit amet", SortingType.Length), "sit amet Lorem ipsum dolor")
        line = "Suspendisse ut massa sed nulla faucibus vehicula"
        self.assertEqual(sort_line(line, SortingType.Length), "ut sed massa nulla faucibus vehicula Suspendisse")

    def test_incorrect_data(self):
        with self.assertRaises(TypeError):
            sort_line(54, SortingType.Alphabetical)
        with self.assertRaises(TypeError):
            sort_line(87, SortingType.Length)
        with self.assertRaises(Exception):
            sort_line("Lorem ipsum", "some invalid sorting type")

if __name__ == "__main__":
    unittest.main()