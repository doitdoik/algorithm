from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
queue = deque([n-i for i in range(n)])

while len(queue) > 1:
    queue.pop()
    queue.appendleft(queue.pop())

print(queue.pop())