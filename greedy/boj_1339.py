import sys

input = sys.stdin.readline
n = int(input())
s = []

for i in range(n): 
    s.append(list(input().strip()))

a = [0 for i in range(26)]

for i in s:
    li = len(i)
    for j in range(li):
        a[ord(i[j]) - 65] += 10 ** (li - j - 1)

a.sort(reverse=True)
res = 0
cnt = 9

for i in a:
    res += cnt * i
    cnt -= 1

print(res)