class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        n = self.head
        if n is None:
            print("the list is empty!!")
        else:
            while n is not None:
                print(n.data, '-->', end=' ')
                n = n.ref
            
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        # n = self.head
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n =  self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print('The node is not present in the linked list!!')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

n = LinkedList()
n.add_begin(34)
n.add_begin(23)
n.add_after(1,23)
n.print_LL()