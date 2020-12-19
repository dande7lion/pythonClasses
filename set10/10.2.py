class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise ValueError("Stos przepełniony. Nie można dodać elementu.")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stos pusty. Nie można pobrać elementu.")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data


import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack1 = Stack()
        self.stack2 = Stack(1)
        self.stack3 = Stack (3)
        self.stack1.push(1)
        self.stack1.push(2)
        self.stack2.push(3)

    def test_is_empty(self):
        self.assertFalse(self.stack1.is_empty())
        self.assertFalse(self.stack2.is_empty())
        self.assertTrue(self.stack3.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack1.is_full())
        self.assertTrue(self.stack2.is_full())
        self.assertFalse(self.stack3.is_full())

    def test_push_and_pop(self):
        self.stack1.push(4)
        self.assertEqual(self.stack1.pop(), 4)
        self.stack1.push(5)
        self.stack1.push(6)
        self.assertEqual(self.stack1.pop(), 6)
        self.assertEqual(self.stack1.pop(), 5)

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            self.stack2.push(7)
        with self.assertRaises(ValueError):
            self.stack3.pop()

if __name__ == "__main__":
    unittest.main()
