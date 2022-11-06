from bisect import bisect_left
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
stack = [0]

for i in arr:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[bisect_left(stack, i)] = i

print(len(stack)-1)