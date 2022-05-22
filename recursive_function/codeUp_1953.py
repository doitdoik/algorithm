def triangle(x):
    if x == 1:
        return print('*')
    triangle(x-1)
    return print('*'*x)

n = int(input())
triangle(n)