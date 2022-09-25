import sys

input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    stack.append(int(input()))

last = stack[-1]
cnt = 1

for i in reversed(range(n)):
    if stack[i] > last:
        cnt += 1
        last = stack[i]

print(cnt)