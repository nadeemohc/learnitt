class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def trav(self):
        n = self.head
        if n is None:
            print("The list is empty")
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
            n.ref = new_node
    
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("The searching element is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

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
            print('The list is empty so no deletion possible')
        elif self.head.ref is None:
            self.head = None
        else:
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_random(self, x):
        n = self.head
        if n is None:
            print("The list is empty")
        elif self.head.data == x:
            self.head = self.head.ref
        else:
            while n.ref is not None:
                if x == n.ref.data:
                    break
                n = n.ref
            if n.ref is None:
                print('the searching node is not present')
            else:
                n.ref = n.ref.ref


x = LinkedList()
x.add_begin(1)
x.add_begin(2)
x.add_begin(3)
x.add_end(2)
x.add_before(5,2)
x.delete_last()
x.delete_random(2)
x.trav()