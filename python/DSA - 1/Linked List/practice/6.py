class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LL:
    def __init__(self):
        self.head = None

    def printLL(self):
        n = self.head
        if n is None:
            print('The linked list is empty')
        else:
            while n is not None:
                print(f'{n.data}->', end=' ')
                n = n.ref
            print()
    
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def delete_last(self):
        n = self.head
        if n is None:
            print('The list is empty so no deletion possible')
        elif self.head.ref is None:
            self.head = None
        else:
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

