n = int(input('Enter the total length to enter: '))
x = [int(input('Enter the elements: ')) for x in range(n)]
# for i in range(len(x)):
#     m_ind = i
#     for j in range(i+1, len(x)):
#         if x[j] < x[m_ind]:
#             m_ind = j
#     if x[i] != x[m_ind]:
#         x[i], x[m_ind] = x[m_ind], x[i]
# print(x)


for i in range(len(x)):
    m = min(x[i:])
    m_ind = x.index(m, i)
    if x[i] != x[m_ind]:
        x[i], x[m_ind] = x[m_ind], x[i]

print(x)