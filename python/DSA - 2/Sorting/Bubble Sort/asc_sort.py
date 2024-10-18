a = [4,10,25,4,23,0]
for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            print(a)
        else:
            print(a) 
    print()

print(f'The sorted list in ascending order is: {a}')