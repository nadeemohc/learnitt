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

dll = DLL()
dll.add_end(1)
dll.add_end(2)
dll.add_end(3)
dll.add_end(4)
print("Original list:")
dll.traverseit()  # Output: 1-> 2-> 3-> 4->

dll.reverseit()
print("Reversed list:")
dll.traverseit()  # Output: 4-> 3-> 2-> 1->
