class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError("Kolejka przepełniona. Nie można dodać elementu.")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError("Kolejka pusta. Brak elementów do pobrania.")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data

import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue1 = Queue()
        self.queue2 = Queue(1)
        self.queue3 = Queue (3)
        self.queue1.put(1)
        self.queue1.put(2)
        self.queue2.put(3)

    def test_is_empty(self):
        self.assertFalse(self.queue1.is_empty())
        self.assertFalse(self.queue2.is_empty())
        self.assertTrue(self.queue3.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue1.is_full())
        self.assertTrue(self.queue2.is_full())
        self.assertFalse(self.queue3.is_full())

    def test_put_and_get(self):
        self.queue1.put(4)
        self.assertEqual(self.queue1.get(), 1)
        self.queue1.put(5)
        self.queue1.put(6)
        self.assertEqual(self.queue1.get(), 2)
        self.assertEqual(self.queue1.get(), 4)

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            self.queue2.put(7)
        with self.assertRaises(ValueError):
            self.queue3.get()

if __name__ == "__main__":
    unittest.main()
