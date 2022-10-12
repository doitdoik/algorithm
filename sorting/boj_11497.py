import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = 0

    for i in range(2, n):
        res = max(res, abs(arr[i] - arr[i-2]))
    print(res)