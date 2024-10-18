# Sort a list in descending order by taking the input from the user

a = int(input("Enter the total numbers to enter: "))
x = [int(input('Enter the elements: ')) for x in range(a)]
print('The entered list: ',x)

for i in range(len(x)):
    m_ind = i
    for j in range(i+1, len(x)):
        if x[j] > x[m_ind]:
            m_ind = j
    
    if x[i] != x[m_ind]:
        x[i], x[m_ind] = x[m_ind], x[i]

print('The sorted list: ',x)