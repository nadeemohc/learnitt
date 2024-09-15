class Node:
    def __init__(self, data):
        self.data =  data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        n = self.head
        if n is None:
            print('The linked list is empty')
        while n is not None:
            print(f'->{n.data}', end=' ')
            n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node =  Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            # new_node =  None

n = LinkedList()
n.add_end(40)
n.add_begin(50)
# n.add_end(100)
# n.add_begin(60)
n.print_LL()