import sys
import bisect

input = sys.stdin.readline
n = int(input())
port = list(map(int, input().split()))
res = [port[0]]

for i in range(1, n):
    if port[i] > res[-1]:
        res.append(port[i])
    else:
        idx = bisect.bisect_left(res, port[i])
        res[idx] = port[i]

print(len(res))