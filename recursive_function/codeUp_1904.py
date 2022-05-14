a, b = map(int,input().split())

def odd(a,b):
    if a%2 == 1:
        print(a, end=' ')
    if a==b:
        return

    odd(a+1,b)
odd(a,b)