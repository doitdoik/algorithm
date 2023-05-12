# boj 2576 홀수
import sys
input = sys.stdin.readline
arr = []
for i in range(7):
    a = int(input())
    if a % 2 != 0: arr.append(a)
if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)