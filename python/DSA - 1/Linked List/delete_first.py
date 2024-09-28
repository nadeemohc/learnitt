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
                print(f'{n.data}-->',end='')
                n = n.ref
            print()
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def delete_first(self):
        if self.head is None:
            print('list is empty so no deletion possible')
        else:
            self.head = self.head.ref
            self.print_LL()

n = LL()
n.add_begin(5)
n.add_begin(4)
n.add_begin(3)
n.add_begin(2)
n.add_begin(1)
n.delete_first()