import sys

input = sys.stdin.readline
n, m = map(int, input().split())
card  = list(map(int, input().split()))

for _ in range(m):
    card = sorted(card)
    cover = card[0] + card[1]
    card[0] = cover
    card[1] = cover

print(sum(card))