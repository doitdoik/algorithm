import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    l = [0] * (n + 1)
    for o in range(n):
        x, y = map(int, input().split())
        l[x]=y
    min_=100_001
    cnt = 0
    for i in range(1,len(l)):
        if  l[i] < min_: 
            min_ = l[i]
            cnt += 1
    print(cnt)