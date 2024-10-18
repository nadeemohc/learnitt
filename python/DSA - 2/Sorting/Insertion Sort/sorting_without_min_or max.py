list1 = [21,3,1,5,4,6,8,5]
print(f'The unsorted list is: {list1}')
for i in range(len(list1)):
    min_val = i
    for j in range(i+1, len(list1)):
        if list1[j] < list1[min_val]:
            min_val = j
    if list1[i] != list1[min_val]:
        list1[i], list1[min_val] = list1[min_val], list1[i]

print(f'The sorted list is: {list1}')