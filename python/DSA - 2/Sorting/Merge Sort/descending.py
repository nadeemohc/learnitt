def merge_sort(x):
    if len(x) <= 1:
        return x
    
    mid = len(x) // 2
    left = x[:mid]
    right = x[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return mergeit(left_sorted, right_sorted)

def mergeit(left, right):
    sorted_array = []
    while left and right:
        if left[0] > right[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))

    sorted_array.extend(left)
    sorted_array.extend(right)

    return sorted_array

n = int(input('enter the limit: '))
x = [int(input('Enter the elemtnt: ')) for _ in range(n)]
print(merge_sort(x))

