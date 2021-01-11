import random
class RandomQueue:

    def __init__(self, size = 5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.number_of_elements = 0

    def insert(self, item):
        if self.is_full():
            raise ValueError("Kolejka jest pełna. Nie można dodać elementu.")
        self.items[self.number_of_elements] = item
        self.number_of_elements += 1

    def remove(self):   # zwraca losowy element
        if self.is_empty(): 
            raise ValueError("Kolejka jest pusta. Nie można pobrać elementu.")
        self.number_of_elements -= 1
        return self.items.pop(random.randrange(self.number_of_elements))
        
    def is_empty(self):
        return self.number_of_elements == 0

    def is_full(self): 
        return self.n == self.number_of_elements

    def clear(self):
        self.items[:]
        self.number_of_elements = 0

if __name__ == "__main__":
    random_queue = RandomQueue()
    random_queue.insert(3)
    random_queue.insert(4)
    random_queue.insert(5)
    random_queue.insert(6)
    print(random_queue.remove())