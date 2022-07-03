n = int(input())
t = list(map(int,input().split()))
t.sort(reverse=True)
res = 0

for i in range(n):
    res = max(res, t[i]+i)

print(res+2)