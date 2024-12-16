def heap_sort(arr):
    heapq.heapify(arr)
    sorted_list = []
    while arr:
        sorted_list.append(heapq.heappop(arr))
    return sorted_list

# Sample Workouts
arr = [5, 3, 8, 4, 2, 7, 6, 1]
print("Original Array:", arr)
print("Heap Sorted Array:", heap_sort(arr))