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
            print('The linked list is empty')
        else:
            while n is not None:
                print(f'{n.data}, -> ', end='')
                n = n.ref
            print()

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        n = self.head
        new_node = Node(data)
        if n is None:
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
            print('the list is empty operation not possible')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        n = self.head
        new_node = Node(data)
        if n is None:
            print('the list is empty')
            return
        if n.data == x:
            new_node.ref = self.head
            self.head = new_node
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print('The searching node is not present')
        else:
            new_node.ref = n.ref
            n.ref = new_node


# a = LinkedList()
# b = int(input("Enter the max elements to enter: "))
# for i in range(1, b+1):
#     c =  int(input('Entere the elements: ')) 
#     if i % 2 != 0:
#         a.add_begin(c)
#     else:
#         a.add_end(c)

# a.traverseit()