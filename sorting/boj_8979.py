import sys

input = sys.stdin.readline
n, k = map(int, input().split())
medals = []

for i in range(n):
    medals.append(list(map(int, input().split())))
medals.sort(key=lambda x : (-x[1], -x[2], -x[3]))

for j in range(n):
    if medals[j][0] == k:
        index = j

for l in range(n):
    if medals[index][1:] == medals[l][1:]:
        print(l+1)
        break