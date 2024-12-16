import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def build(self, arr):
        self.heap = arr[:]
        heapq.heapify(self.heap)

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def remove(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def display(self):
        print("MinHeap:", self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def build(self, arr):
        self.heap = [-x for x in arr]
        heapq.heapify(self.heap)

    def insert(self, val):
        heapq.heappush(self.heap, -val)

    def remove(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        return None

    def display(self):
        print("MaxHeap:", [-x for x in self.heap])


# Sample Workouts
min_heap = MinHeap()
max_heap = MaxHeap()

print("Building MinHeap and MaxHeap:")
arr = [10, 20, 15, 40, 50, 100, 25]
min_heap.build(arr)
max_heap.build(arr)
min_heap.display()
max_heap.display()

print("\nInserting into MinHeap and MaxHeap:")
min_heap.insert(5)
max_heap.insert(60)
min_heap.display()
max_heap.display()

print("\nRemoving from MinHeap and MaxHeap:")
print("Removed from MinHeap:", min_heap.remove())
print("Removed from MaxHeap:", max_heap.remove())
min_heap.display()
max_heap.display()