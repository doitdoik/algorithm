import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
res = []

for i in range(n):
    queue = deque(input().split())
    res.append(queue)

sen = deque(input().split())

while sen:
    temp = sen.popleft()
    cnt = 0
    for i in res:
        if i[0] == temp:
            i.popleft()
            if not i:
                res.remove(i)
            cnt = 1
            break
    if cnt == 0:
        print('Impossible')
        exit(0)
if res:
    print('Impossible')
else:
    print('Possible')