import unittest

def reverse_iterative(L, left, right):
    if left > right:
        raise Exception("The left index can not be greater than the right index!")
    total = left + right
    for left_elem in range(left, (total+1)//2):
        right_elem = total - left_elem
        L[left_elem], L[right_elem] = L[right_elem], L[left_elem]
    return L

def reverse_recursion(L, left, right):
    if left >= right:
        return L
    else:
        L[left], L[right] = L[right], L[left]
        return reverse_recursion(L, left+1, right-1)

class TestReverse(unittest.TestCase):
    def test_reverse_iterative(self):
        self.assertEqual(reverse_iterative([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 5), [1, 2, 6, 5, 4, 3, 7, 8, 9])
        self.assertEqual(reverse_iterative([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 4), [1, 2, 5, 4, 3, 6, 7, 8, 9])

    def test_reverse_recursion(self):
        self.assertEqual(reverse_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 4), [1, 2, 5, 4, 3, 6, 7, 8, 9])
        self.assertEqual(reverse_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 5), [1, 2, 6, 5, 4, 3, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
