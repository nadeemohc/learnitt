a = [32,4,1,54,23,5,7,1]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]


print(f'The sorted list in descending order is: {a}')