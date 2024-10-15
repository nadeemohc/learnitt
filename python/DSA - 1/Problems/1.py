# Find the Second Largest Element

#     Problem: Given an array of integers, find the second largest element without sorting the array.
#     Example: Input: [10, 5, 8, 12, 15]
#     Output: 12


a = [10, 5, 8, 12, 15]
x = []
for i in range(len(a)):
    c = max(a)
    x.append(c)
    a.remove(c)

print(x[1])
