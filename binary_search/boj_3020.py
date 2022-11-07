import sys
import bisect

input = sys.stdin.readline
n, h = map(int, input().split())
top = []
bot = []

for i in range(n):
    if i % 2 == 0:
        bot.append(int(input()))
    else:
        top.append(h-int(input()))
top.sort()
bot.sort()
res = n
cnt = 0

for i in range(h):
    top_idx = bisect.bisect_right(top, i)
    bot_idx = bisect.bisect_right(bot, i)
    cur = top_idx + len(bot) - bot_idx
    if res == cur:
        cnt += 1
    elif res > cur:
        res = cur
        cnt = 1

print(res, cnt)