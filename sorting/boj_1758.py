import sys

input = sys.stdin.readline
n = int(input())
tips = []
res = 0

for i in range(n):
    tips.append(int(input()))

tips.sort(reverse=True)

for i in range(n):
    if tips[i] - i>0:
        res += tips[i]-i

print(res)