def quick_sort(x):
    length = len(x)
    if length <= 1:
        return x
    else:
        pivot = x.pop()
        print('picot', pivot)

    greater = []
    lower = []

    for i in x:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)

    return quick_sort(lower) + [pivot] + quick_sort(greater)


print(f'the list in ascending order is: {quick_sort([21,2,43,1,54,1])}')