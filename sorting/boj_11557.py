import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = []

    for _ in range(n):
        uni, drinks = input().rstrip().split()
        arr.append((uni, int(drinks)))

    arr.sort(key=lambda x:x[1])
    print(arr[-1][0])