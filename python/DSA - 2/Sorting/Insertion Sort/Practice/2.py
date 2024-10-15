# Write a function that takes a list of integers and sorts it in ascending order using the selection sort algorithm.
# Example: Input: [64, 25, 12, 22, 11] → Output: [11, 12, 22, 25, 64]

x = [64, 25, 12, 22, 11]
for i in range(len(x)):
    m = min(x[i:])
    m_ind = x.index(m, i)
    x[i], x[m_ind ] = x[m_ind], x[i]

print(x)
