class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
    
    def add_begin(self, data):
        n = self.head
        new_node = Node(data)
        if n is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def traverseit(self):
        n = self.head
        if n is None:
            print('The list is empty')
        else:
            while n is not None:
                print(f'{n.data}->', end='')
                n = n.next
            print()

    def add_after(self, data, x):
        n = self.head
        new_node = Node(data)
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print('The searching node is not present, insertion not possible')
        else:
            new_node.next = n.next
            new_node.prev = n
            if n.next is  not None:
                n.next.prev = new_node
            n.next = new_node


a = DLL()
a.add_begin(1)
a.add_begin(2)
a.add_begin(3)
a.add_begin(4)
a.add_after(23,2)
a.traverseit()