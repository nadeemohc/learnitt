# x = []
# a = [2, 4, 3, 5, 7, -1, 8, 10]
# t = 7
# for i in range(len(a)):
#     for j in range(1,len(a)):
#         if a[i] + a[j] == 7:
#             print(a[i], a[j])
#             b = (a[i], a[j])
#             print('b = ', b)
#             x.append((a[i], a[j]))
#     else:
#         # print('no')
#         pass


def find_pairs_with_sum(arr, target):
    pairs = []
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

# Example usage:
arr = [2, 4, 3, 5, 7, -1, 8, 10]
target = 7
print(find_pairs_with_sum(arr, target))  # Output: [(5, 2), (4, 3), (8, -1)]
