from bisect import bisect_left

n = int(input())
arr = [0] + list(map(int,input().split()))
d = [0] * (n+1) 
cmp = [-1000000001] 
tmp = 0

for i in range(1, n+1):
    if cmp[-1] < arr[i]: 
        cmp.append(arr[i])
        d[i] = len(cmp) - 1
        tmp = d[i]
    else:
        d[i] = bisect_left(cmp, arr[i]) 
        cmp[d[i]] = arr[i] 
print(tmp) 

res = []

for i in range(n, 0, -1):
    if d[i] == tmp:
        res.append(arr[i])
        tmp -= 1
res.reverse()
print(*res)