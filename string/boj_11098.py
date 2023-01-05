import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    p = int(input())
    max = 0
    for _ in range(p):
        c,name = input().split()
        c = int(c)
        if c > max:
            max = c
            res = name
    print(res)