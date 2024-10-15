# Rotate an Array by K Steps

#     Problem: Rotate an array to the right by k steps, where k is a non-negative integer.
#     Example: Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
#     Output: [5, 6, 7, 1, 2, 3, 4]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
x = []
for i in range(k):
    x.append(nums[-1])
    nums.remove(nums[-1])

x = x[::-1]
z = x + nums
print(z)