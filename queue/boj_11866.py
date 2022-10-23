from collections import deque

queue = deque()
res = []
n, k = map(int, input().split())

for i in range(1, n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    res.append(queue.popleft())

print("<",end='')

for i in range(len(res)-1):
    print("%d, "%res[i], end='')

print(res[-1], end='')
print(">")