# boj 2455 지능형 기차
import sys

input = sys.stdin.readline
res = 0
max_res = 0
for i in range(4):
    a, b = map(int, input().split())
    res -= a
    res += b
    max_res = max(max_res, res)
print(max_res)