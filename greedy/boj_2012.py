import sys

input = sys.stdin.readline
n = int(input())
s = []
for i in range(n):
    s.append(int(input()))

s.sort()
res = 0
for i in range(1, n + 1):
    res += abs(i - s[i - 1])
print(res)