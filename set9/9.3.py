class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DoubleList:
    """Klasa reprezentująca całą listę dwukierunkową."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node     # stary head
            self.head = node          # nowy head
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.tail:
            node.prev = self.tail
            self.tail.next = node     # stary tail
            self.tail = node          # nowy tail
        else:         # pusta lista
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        elif self.head is self.tail:   # length == 1
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.prev = None   # czyszczenie
            node.next = None   # czyszczenie
            self.length -= 1
            return node

    def remove_tail(self):   # zwraca node
        if self.is_empty():
            raise ValueError("pusta lista")
        elif self.head is self.tail:   # length == 1
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None   # czyszczenie
            node.prev = None
            self.length -= 1
            return node

            
    def find_max(self):
        # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        current_node = self.head
        max_value_node = current_node
        while current_node.next is not None:
            if max_value_node.data < current_node.next.data:
                max_value_node = current_node.next
            current_node = current_node.next
        return max_value_node
    


    def find_min(self):
        # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        current_node = self.head
        min_value_node = current_node
        while current_node.next is not None:
            if min_value_node.data > current_node.next.data:
                min_value_node = current_node.next
            current_node = current_node.next
        return min_value_node

    def remove(self, node):
        # Usuwa wskazany węzeł z listy.
        if self.is_empty():
            raise ValueError("Pusta lista!")
        if node == None:
            return ValueError("Nie ma takiego węzła!")
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            node.prev.next = None
        else:
            node.next.prev = node.prev
        

    def clear(self):     # czyszczenie listy
        if self.is_empty():
            return
        self.head = None
        self.tail = None
        self.length = 0


if __name__ == "__main__":
    double_list = DoubleList()
    node = Node(15)
    double_list.insert_head(Node(5))
    double_list.insert_head(Node(10))
    double_list.insert_head(Node(7))
    double_list.insert_head(node)
    double_list.insert_tail(Node(1))

    double_list.remove(node)

    print(double_list.find_max())   # 10
    print(double_list.find_min())   # 1

    double_list.clear()
    print(double_list.is_empty())   # True
