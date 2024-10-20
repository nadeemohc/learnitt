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
            print("The linked list is empty")
        else:
            while n is not None:
                print(f'{n.data}-->', end=' ')
                n = n.ref
            print()
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_before(self, data, x):
        n = self.head
        new_node = Node(data)
        if n is None:
            print('The list is empty')
            return
        if self.head.data == x:
            new_node.ref = self.head
            self.head = new_node
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("The searching element is not present")
        else:
            new_node.ref = n.ref
            n.ref = new_node


    def delete_last(self):
        n = self.head
        if n is None:
            print("The list is empty so deletion is not possible")
        elif self.head.ref is None:
            self.head = None
        else:
            while n.ref.ref is not None:
                n = n.ref            
            n.ref = None

n = LL()
n.add_begin(23)
n.add_begin(12)
n.add_before(340, 12)
n.add_begin(456)
n.add_begin(443)
# n.delete_last()
n.printLL()