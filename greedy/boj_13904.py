import sys

input = sys.stdin.readline
n = int(input().rstrip())
arr = []
res = [0 for _ in range(1000)]

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(reverse= True, key = lambda x : x[1])

for i in range(n):
    for j in range(arr[i][0]-1, -1, -1):
        if res[j] == 0:
            res[j] = arr[i][1]
            break

print(sum(res))