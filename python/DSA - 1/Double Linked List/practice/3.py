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
                n = n.next
            print()

    def reverseit(self):
        n = self.head
        p = None
        if n is None:
            print('The list is empty')
        else:
            while n is not None:
                n.next, n.prev = n.prev, n.next
                p = n
                n = n.prev

            self.head = p

    def add_end(self, data):
        n = self.head
        new_node = Node(data)
        if n is None:
            self.head = new_node
        else:
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n

x = DLL()
x.add_end(54)
x.add_end(64)
x.add_end(74)
print('asc')
x.traverseit()
print('dsc')
x.reverseit()
x.traverseit()