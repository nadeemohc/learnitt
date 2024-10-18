a = [2,3,5,4,1,2,2,3,5,6,7,66,7]

for i in range(len(a)):
    m_ind = i
    for j in range(i+1, len(a)):
        if a[j] > a[m_ind]:
            m_ind = j
        
    if a[i] != a[m_ind]:
        a[i], a[m_ind] = a[m_ind], a[i]

print(a)