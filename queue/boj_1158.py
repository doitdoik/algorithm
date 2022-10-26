import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
res = []
queue = deque(range(1, n+1))

for i in range(1, n+1):
    queue.rotate(-k+1)
    res.append(str(queue.popleft()))

print("<",", ".join(res)[:], ">", sep='')