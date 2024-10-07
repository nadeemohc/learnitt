class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverseit(self):
        n = self.head
        if n is None:
            print('the list is empty')
        else:
            while n is not None:
                print(f'{n.data}->', end='')
                n = n.ref
            print()

    def add_end(self, data):
        n = self.head
        new_node = Node(data)
        if n is None:
            new_node.ref = self.head
            self.head = new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        n = self.head
        new_node = Node(data)
        if n is None:
            print('The list is empty')
        elif n.data == x:
            new_node.ref = self.head
            self.head = new_node
        else:
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print('the searching node is not present in here')
            else:
                new_node.ref = n.ref
                n.ref = new_node

n = LinkedList()
# n.add_begin(34)
n.add_end(90)
n.add_end(40)
n.add_before(60, 90)
n.add_before(0, 40)
n.traverseit()