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
        if  n is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_before(self, data, x):
        n = self.head
        new_node = Node(data)
        
        if n is None:
            print('The list is empty; insertion not possible')
            return
        elif self.head.data == x:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            
            if n is None:
                print('The searching element is not present; insertion not possible')
            else:
                new_node.next = n  # Set new_node's next to n
                new_node.prev = n.prev  # Set new_node's prev to n's prev
                
                if n.prev is not None:  # If n is not the head
                    n.prev.next = new_node  # Update the previous node's next
                n.prev = new_node  # Update n's previous pointer to new_node

    def traverseit(self):
        n = self.head
        if n is None:
            print('The list is empty')
        else:
            while n is not None:
                print(f'{n.data}->', end='')
                n = n.next
            print()

a = DLL()
a.add_begin(1)
a.add_begin(2)
a.add_begin(3)
a.add_begin(4)
a.add_before(56,3)
a.traverseit()