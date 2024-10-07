class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DLL:
    def __init__(self):
        self.head = None
    
    def traverseit(self):
        n = self.head
        if n is None:
            print('The list is empty')
        else:
            while n is not None:
                print(f'{n.data}->', end='')
                n=n.next
            print()
    def add_begin(self, data):
        n = self.head
        new_node = Node(data)
        if n is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

x = DLL()
x.add_begin(1)
x.add_begin(1)
x.add_begin(1)
x.add_begin(1)
x.traverseit()