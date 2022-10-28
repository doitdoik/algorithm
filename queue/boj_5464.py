import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
spot = deque()
weight = deque()
wait = deque()
use = [0] * n
res = 0

for i in range(n):
    spot.append(int(input().strip()))
for i in range(m):
    weight.append(int(input().strip()))   
for i in range(m*2):
    car = int(input().strip())
    if car > 0:
        if 0 in use:
            for j in range(n):
                if use[j] == 0:
                    use[j] = car
                    break
        else:
            wait.append(car)
    else:
        a = use.index(-car)
        use[a] = 0
        res += weight[-car-1]*spot[a]
        if wait:
            use[a] = wait.popleft()

print(res)