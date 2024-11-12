def quick_sort(list1):
    l = len(list1)
    if l <= 1:
        return(list1)
    else:
        pivot = list1.pop()

    greater = []
    lower = []
    
    for i in list1:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)

    return quick_sort(lower) + [pivot] + quick_sort(greater)

print(quick_sort([32,4,1,657,8,90]))