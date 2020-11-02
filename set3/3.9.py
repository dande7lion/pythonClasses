import unittest

def find_sum(list):
    result_list = []
    for element in list:
        if isinstance(element, int):
            result_list.append(element)
        else:
            result = sum(element)
            result_list.append(result)
    return result_list

class TestFindSum(unittest.TestCase):
    def test_find_sum(self):
        self.assertEqual(find_sum([[1, 2, 3], [4, 5, 6]]), [6,15])
        self.assertEqual(find_sum([1, (1,2), [3,4]]), [1, 3, 7])
        self.assertEqual(find_sum([2, (2, 5, 11), 14, [23, 4], (4,8)]), [2, 18, 14, 27, 12])

if __name__ == "__main__":
    unittest.main()