class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

def count_leafs(top):
    if top is None:
        return
    stack = list()
    leafs_count = 0
    stack.append(top)
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        if not node.left and not node.right:
            leafs_count += 1
    return leafs_count

def count_total(top):
    if top is None:
        return
    total_count = 0
    stack = list()
    stack.append(top)
    while stack:
        node = stack.pop()
        total_count += node.data
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return total_count


if __name__ == "__main__":  
    root = Node(1)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(15)
    root.right.right = Node(7)
    root.left.left.left = Node(48)
    print(count_total(root))    # 77
    print(count_leafs(root))    # 2
