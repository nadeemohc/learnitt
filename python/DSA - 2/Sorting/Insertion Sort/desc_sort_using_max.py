x = [1,2,1,3,5,3,7,5,9]

for i in range(len(x)):
    max_val = max(x[i:])
    max_index = x.index(max_val, i)
    x[i], x[max_index] = x[max_index], x[i]

print(x)    