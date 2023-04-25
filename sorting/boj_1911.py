#boj 1911 흙길 보수하기
import sys
import math
input = sys.stdin.readline
n, l = map(int, input().split())
pool = []

for _ in range(n):
    pool.append(list(map(int, input().split())))
    
pool.sort(key=lambda x: (x[0], x[1]))

res = 0
plank = 0

for start, end in pool:
    start = max(start, plank)
    cnt = math.ceil((end-start) / l)
    plank = start + cnt * l
    res += cnt

print(res)    