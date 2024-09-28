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
            print('the list is none')
        else:
            while n is not None:
                print(n.data, '-->', end=' ')
                n = n.ref
            print()
    
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print('The  linked list is empty!!')
            return

        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print('The node is not present in the linked list!!')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

n = LL()
# n.add_begin(34)
n.add_end(90)
n.add_end(40)
n.add_before(60, 90)
n.add_before(0, 40)
n.print_LL()