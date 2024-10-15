a = [4,3, 1,6,1,5,90]
print(a)
for i in range(len(a)):
    m = max(a[i:])
    m_ind = a.index(m,i)
    a[i], a[m_ind] = a[m_ind], a[i]

print(a)