a = 'ab'
count = 0
x = set(a)
words = ["a","b","c","ab","ac","bc","abc"]
for i in words:
    for j in i:
        if j not in x:
            count += 1
            print(i)
            break

print(len(words)-count)