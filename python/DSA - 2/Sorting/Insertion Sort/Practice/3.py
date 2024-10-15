# Modify the basic selection sort function to sort a list in descending order.
# Example: Input: [4, 15, 3, 9, 12] → Output: [15, 12, 9, 4, 3]

x = [4, 15, 3, 9, 12]
for i in range(len(x)):
    m = max(x[i:])
    m_index = x.index(m, i)
    x[i], x[m_index] = x[m_index], x[i]

print(x)