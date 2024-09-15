# Write a program to insert 5 nodes at the beginning of a singly linked list and then traverse the list to print the data in each node.

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
            print('empty list')
        else:
            while n is not None:
                print(f'-->{n.data}', end=' ')
                n = n.ref
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

a = LinkedList()
x = int(input('Enter the No of total elements to insert: '))
for i in range(1, x+1):
    v = int(input(f"Enter the element no {i}: "))
    a.add_begin(v)
a.print_LL()