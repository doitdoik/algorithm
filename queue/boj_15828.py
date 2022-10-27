import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queue = deque()

while True :
    packet = input().strip()
    if packet == '-1':
        if len(queue) > 0:
            print(' '.join(queue))
        else : print('empty')
        break
    if packet == '0':
        queue.popleft()
    elif len(queue) < n :
        queue.append(packet)