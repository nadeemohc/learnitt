# Write a program to insert 5 nodes at the end of a singly linked list. After all insertions, traverse the list and print the elements in order.

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        n = self.head
        if n is None:
            print('The list is empty')
        else:
            while n is not None:
                print(f'-->{n.data}', end=' ')
                n = n.ref

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
a = LinkedList()
b = int(input('Enter the total number of elements to insert: '))
for i in range(1, b+1):
    c = int(input(f'Enter element {i}'))
    a.add_end(c)

a.traversal()