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
            print('the list is empty')
        else:
            while n is not None:
                print(n.data, '->', end='')
                n = n.ref
            print()
        
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def delete_random(self, x):
        n = self.head
        if self.head is None:
            print('the list is empty so deletion is not possible')
        elif x == self.head.data:
            self.head = self.head.ref
        else:
            n = self.head
            while n.ref is not None:
                if x == n.ref.data:
                    break
                n = n.ref
            if n is None:
                print('the given node is not present in the list')
            else:
                n.ref = n.ref.ref

n = LL()
n.add_begin(7)
n.add_begin(6)
n.add_begin(5)
n.add_begin(4)
n.add_begin(3)
n.add_begin(2)
n.add_begin(1)
n.delete_random(3)
n.printLL()