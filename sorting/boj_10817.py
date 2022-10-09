import sys

input = sys.stdin.readline
arr = list(map(int, input().split()))

arr.sort(reverse=True)

print(arr[1])