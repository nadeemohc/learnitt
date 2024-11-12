class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f'{item} has added to stack')

    def pop(self):
        if not self.stack:
            print('The stack is empty')
        else:
            item = self.stack.pop()
            print(f'{item} has poped out of the stack')

    def display(self):
        print(f'Stack: {self.stack}')

a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.pop()
a.push(5)
a.push(6)
a.display()