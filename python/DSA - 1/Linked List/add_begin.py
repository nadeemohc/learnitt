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
            print('The linked list is empty')
        else:
            while n is not None:
                # print(f'The data inside node is {n.data}')
                print(n.data, '->',end=" ")
                n = n.ref
                # print(n)

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node


node = LinkedList()
node.add_begin(20)
node.add_begin(10)
node.print_LL()