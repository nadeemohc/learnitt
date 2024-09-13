a = input("Enter the string: ")

def check(a):
    b = a[::-1]
    if b == a:
        print('Palindrome')
    print('Not Palindrome')


check(a)