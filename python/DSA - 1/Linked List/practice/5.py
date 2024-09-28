class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LL:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        n = self.head
        if n is None:
            print('the list is empty')
        else:
            while n is not None:
                print(n.data, '-->', end=' ')
                n = n.ref
            print()
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print('the target node is not in the linked list')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

n = LL()
n.add_begin(1)
n.add_begin(23)
n.add_after(2,23)
n.print_LL()