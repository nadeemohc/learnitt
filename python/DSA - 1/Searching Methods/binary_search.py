def bin_search(list1, key):
    low = 0
    high = (len(list1)-1)
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found is True:
        print('Key is found')
    else:
        print('Key is not found')

list1 = [6,4,2,6,8, 2,4,1,90]
list1.sort()
key = int(input('Enter the key to search: '))

bin_search(list1, key)