n = int(input('Enter the total number of elements: '))
x = [int(input('Enter the elements: ')) for x in range(n)]

for i in range(len(x)-1):
    for j in range(len(x)-1):
        if x[j]  > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
        
print(f'The sorted list in ascending is: {x}')