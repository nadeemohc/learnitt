list1 = [6,4,2,6,8, 2,4,1,90]
key = int(input('Enter the value to search: '))


def linear_search(list, key):
    a = []
    flag = False
    for i in range(len(list)):
        if key == list[i]:
            flag = True
            a.append(i)
            
    if flag is True:
        print(f'found the number {key} at')
        for i in a:
            print(i)
    else:
        print('Element missing in the list')

linear_search(list1, key)

