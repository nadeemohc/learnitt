class Queue:
    def __init__(self):
        self.queue = []

    def enque(self, item):
        self.queue.append(item)
        print(f'{item} has added to the queue')

    def dequeue(self):
        if not self.queue:
            print('The queue is empty')
        else:
            item = self.queue.pop(0)
            print(f'{item} has removed from the queue')

    def display(self):
        print(f'Queue: {self.queue}')

a = Queue()
a.enque(1)
a.enque(2)
a.enque(3)
a.enque(4)
a.enque(5)
a.dequeue()
a.display()