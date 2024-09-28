class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linked_List:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        n = self.head
        if n is None:
            print('The list is empty')
        else:
            while n is not None:
                print(n.data, '-->', end=' ')
                n = n.ref
            print()

    def add_empty(self, data):
        n = self.head
        if n is not None:
            print('The list is not empty')
        else:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node

n = Linked_List()
n.add_empty(10)
n.add_empty(1)
n.print_LL()