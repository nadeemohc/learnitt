# Write a program to insert 10 nodes at both the beginning and end of a singly linked list. After all insertions, traverse the list and count the total number of nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    def traverseit(self):
        if self.head is None:
            print('the list is empty')
        else:
            n = self.head
            while n is not None:
                print(f'-->{n.data}', end=' ')

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                n.ref = n
            n.ref = new_node


a = LinkedList()
b = int(input("Enter the max elements to enter: "))
for i in range(1, b+1):
    c =  int(input('Entere the elements: ')) 
    if i % 2 != 0:
        a.add_begin(c)
    else:
        a.add_end(c)

a.traverseit()