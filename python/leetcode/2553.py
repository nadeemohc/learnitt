### Separate the Digits in an Array ###

nums = [13,25,83,77]
# b = ','.split(nums)
# print(b)
b =''
for i in nums:
    b += str(i)

print(type(b),b)
d = []
for i in b:
    d.append(int(i))
print(type(d),d)