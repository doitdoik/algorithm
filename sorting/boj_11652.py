from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
cards = []
for _ in range(n) :
    cards.append(int(input()))

cnt = Counter(cards).most_common()
cnt.sort(key= lambda x: (-int(x[1]), int(x[0])))

print(cnt[0][0])