a = ['1','2','3','4','5','6','7',]

def sumof(a):
    b = 0
    for i in a:
        if int(i)%2 ==0:
            b+=int(i)
        pass
    print(b)      

sumof(a)