import unittest

def find_intersection(sequence1, sequence2) -> list:
    sequence1.sort()
    sequence2.sort()
    result_sequence = []
    for element1 in sequence1:
        for element2 in sequence2:
            if element1 < element2:
                break
            elif element1 == element2:
                if element1 not in result_sequence:
                    result_sequence.append(element1)
    return result_sequence

def find_sum(sequence1, sequence2) -> list:
    sequence1 = list(dict.fromkeys(sequence1))      # remove duplicates
    for element2 in sequence2:
        if element2 not in sequence1:
            sequence1.append(element2)
    return sequence1

class TestIntersectionAndSum(unittest.TestCase):
    def test_intersection(self):
        self.assertEqual(find_intersection(["a","b","c"],["b", "b", "d"]), ["b"])
        self.assertEqual(find_intersection(["ab", "cd","ef"],["ef", "cd", "gh"]), ["cd", "ef"])

    def test_sum(self):
        self.assertEqual(find_sum(["a","b","c"],["b", "b", "d"]), ["a", "b", "c", "d"])
        self.assertEqual(find_sum(["ab", "cd","ef"],["ef", "cd", "gh"]), ["ab", "cd", "ef", "gh"])

if __name__ == "__main__":
    unittest.main()