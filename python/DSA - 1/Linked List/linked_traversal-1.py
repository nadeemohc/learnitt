class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print('the linked list is empty')
        n = self.head
        while n is not None:
            print(n.data, '->',end=" ")
            n = n.ref
    # def insert_begin(self, data):
    #     new_node = Node(data)
    #     if self.head is None:
    #         self.head = new_node
    #         return
    #     new_node.ref = self.head
    #     self.head = new_node
    # def insert_end(self, data):
    #     new_node = Node(data)
    #     if self.ref is None:
    #         self.ref = new_node
    #         return
    #     new_node.ref = None
            

ll = LinkedList()
# ll.insert_begin(10)
# ll.insert_begin(100)
# ll.insert_end(79)
ll.print_LL()