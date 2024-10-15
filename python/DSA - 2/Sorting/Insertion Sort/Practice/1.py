a = [4,2,3,5,43,2,1,89,0]

for i in range(len(a)):
    mi = min(a[i:])
    ind = a.index(mi, i)
    a[i], a[ind] = a[ind], a[i]
print('ascending: ',a)

for i in range(len(a)):
    ma = max(a[i:])
    ma_ind = a.index(ma, i)
    a[i], a[ma_ind] = a[ma_ind], a[i]
print('descending: ', a)