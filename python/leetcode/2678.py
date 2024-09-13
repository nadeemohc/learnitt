det = ["7868190130M7522","5303914400F9211","9273338290F4010"]
x = 0
y = 60
for i in det:
    a = int(i[11:13])
    if a > y:
        x += 1
print(type(x),x)