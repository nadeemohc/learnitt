#  Write a Quick Sort function that uses:

#     The first element as the pivot.
#     A randomly selected element as the pivot.

n = int(input("Enter the length: "))
x = [int(input("Enter the element: ")) for x in range(n)]

def quick(x):
    l = len(x)
    if l <= 1:
        print(x)
    p = int(input('Enter the desired pivot values index:'))
    pivot = x[p]
    
    greater = []
    lower = []
    for i in x:
        if i < pivot:
            lower.append(i)
        else:
            greater.append(i)

    print(quick(lower) + [pivot] + quick(greater))

print(quick(x))