import sys
import bisect

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
res = [arr[0]]

for i in range(1, n):
    if arr[i] > res[-1]:
        res.append(arr[i])
    else:
        index = bisect.bisect_left(res, arr[i])
        res[index] = arr[i]

print(len(res))