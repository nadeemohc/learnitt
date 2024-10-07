class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverseit(self):
        n = self.head
        if n is None:
            print("the list is empty")
        else:
            while n is not None:
                print(f"{n.data}->", end='')
                n = n.ref
            print()
    
    def add_begin(self, data):
        n = self.head
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        n = self.head
        new_node = Node(data)
        if n is None:
            new_node.ref = self.head
            self.head = new_node
        else:
            while n.ref is not None:
                n = n.ref
            new_node.ref = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        new_node = Node(data)
        while n.ref is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print('The list is empty')
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        n = self.head
        new_node = Node(data)
        if n is None:
            print("the linked list is empty")
            return
        if x == self.head.data:
            new_node.ref = self.head
            self.head = new_node
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("The searching node doesn't exist in this list")
        else:
            new_node.ref = n.ref
            n.ref = new_node

n = LinkedList()
n.add_begin(5)
n.add_begin(4)
n.add_begin(3)
n.add_begin(2)
n.add_begin(1)
# n.add_before(34,3)
# n.add_end(1)
# n.add_end(2)
# n.add_end(3)
# n.add_end(4)
# n.add_end(5)
n.add_after(45,3)
# n.add_before(34,3)
n.traverseit()