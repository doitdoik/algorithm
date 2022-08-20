import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    # arr은 항상 10, n은 항상 3
    arr.sort()
    print(arr[7])