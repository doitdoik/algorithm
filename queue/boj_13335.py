from collections import deque
import sys

input = sys.stdin.readline
n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
queue = deque([0] * w)
cnt = 0
weight = 0

while queue:
  cnt += 1

  if trucks:
    weight -= queue.popleft()
    if weight + trucks[0] <= L:
      weight += trucks[0]
      queue.append(trucks.popleft())

    else:
      queue.append(0)

  else:
    queue.popleft()

print(cnt)