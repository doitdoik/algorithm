n = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(arr)

res = []
for i in range(n):
    t = sort_arr.index(arr[i])
    res.append(t)
    sort_arr[t] = -1

print(*res)