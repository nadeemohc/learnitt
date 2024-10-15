class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DLL:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        n = self.head
        new_node = Node(data)
        if n is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def add_end(self, data):
        n = self.head
        new_node = Node(data)
        if  n is None:
            self.head = new_node
        else:
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n

    def traverseit(self):
        n = self.head
        if n is None:
            print('the list is empty')
        else:
            while n is not None:
                print(f'{n.data}->', end='')
                n = n.next
            print()

a = DLL()
a.add_begin(1)
a.add_begin(2)
a.add_begin(3)
a.add_begin(4)
a.add_end(45)
a.traverseit()