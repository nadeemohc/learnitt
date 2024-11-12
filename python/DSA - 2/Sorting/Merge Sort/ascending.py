def merge_sort(x):
    if len(x) <= 1:
        return x
    
    mid = len(x) // 2
    left_half = x[:mid]
    right_half = x[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return mergeit(left_sorted, right_sorted)

def mergeit(left, right):
    sorted_array = []
    while left and right:
        if left[0] < right[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))

    sorted_array.extend(left)
    sorted_array.extend(right)

    return sorted_array


n = int(input('Enter the limit: '))
x = [int(input('Enter the elements: ')) for _ in range(n)]
print(f'sorted array is: {merge_sort(x)}')