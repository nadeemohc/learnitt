# Implement a program where you alternate between inserting at the beginning and at the end of the singly linked list. 
# Traverse the list and print the final order of elements.

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
            print('the list is empty')
        while n is not None:
            print(f'-->{n.data}', end=' ')
            n = n.ref

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
            while n.ref is not None:
                n = n.ref
            n.ref = new_node


a = LinkedList()
b = int(input('Enter the no of elements to enter: '))
x = []
for i in range(1, b+1):
    c = int(input(f'Enter the element {i}: '))
    x.append(c)
print(x)
for i in range(1, (len(x))+1):
    # print(i, x[i-1])
    if i % 2 != 0:
        a.add_begin(x[i-1])
    else:
        a.add_end(x[i-1])
a.traverseit()