class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        n = self.head
        if n is None:
            print('The list is empty')
        else:
            while n is not None:
                print(f'{n.data}->', end=" ")
                n = n.next
            print()

    def add_end(self, data):
        n = self.head
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n

    def reverse(self):
        current = self.head
        previous = None
        if current is None:
            print("The list is empty")
            return
        # Traverse and swap next and prev pointers
        while current is not None:
            # Swap pointers
            current.next, current.prev = current.prev, current.next
            previous = current  # Move previous to current
            current = current.prev  # Move to the next node in the original list
            
        # Set head to the new first node (which was previous at the end)
        self.head = previous

# Example usage:
dll = DoublyLinkedList()
dll.add_end(1)
dll.add_end(2)
dll.add_end(3)
dll.add_end(4)
print("Original list:")
dll.traverse()  # Output: 1-> 2-> 3-> 4->

dll.reverse()
print("Reversed list:")
dll.traverse()  # Output: 4-> 3-> 2-> 1->
