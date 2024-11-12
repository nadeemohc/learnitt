def selection(x):
    for i in range(len(x)-1):
        m = i
        for j in range(i+1, len(x)):
            if x[j] >= x[m]:
                m = j
        if i != m:
            x[i], x[m] = x[m], x[i]

    return x

print(selection([34,4,7,35,76]))