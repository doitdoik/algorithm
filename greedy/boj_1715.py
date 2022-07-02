import heapq
import sys

input = sys.stdin.readline
n = int(input())
card = []

for _ in range(n):
    num = int(input())
    heapq.heappush(card, num)

res = 0

while len(card)>1:
    n1 = heapq.heappop(card)
    n2 = heapq.heappop(card)
    res += n1 + n2
    heapq.heappush(card, n1+n2)

print(res)