class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    def traverseit(self):
        n = self.head
        if n is None:
            print("the linked list is empty")
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

    def add_after(self, data, x):
        n = self.head
        new_node = Node(data)
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print('the searching elemment not present')
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        n = self.head
        new_node = Node(data)
        if n is None:
            print('the list is empty')
            return
        if self.head.data == x:
            new_node.ref = self.head
            self.head = new_node
        else:
            while n.ref is not None:
                if x == n.ref.data:
                    break
                n = n.ref
            if n.ref is None:
                print('The searching node is not present')
            else:
                new_node.ref = n.ref
                n.ref = new_node

    def delete_last(self):
        n = self.head
        if n is None:
            print('The list is empty')
            return
        if self.head.ref is None:
            self.head = None
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None


n = LinkedList()
n.add_begin(1)
n.add_end(3)
n.add_begin(10)
n.add_end(5)
n.add_end(4)
# n.add_before(43,4)
n.add_after(0,10)
# n.delete_last()
n.traverseit()