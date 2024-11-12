n = int(input('Enter the length: '))
x = [int(input('Enter the elements: ')) for x in range(n)]

for i in range(len(x)-1):
    for j in range(len(x)-1):
        if x[j] < x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]

print('THe list after descending bubble sort: ', x)