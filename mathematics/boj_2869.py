# boj 2869 달팽이는 올라가고 싶다
import sys

input = sys.stdin.readline
a, b, v = map(int, input().split())
res = (v - a) // (a - b)

if (v - a) % (a - b) == 0:
    print(res + 1)
else:
    print(res + 2)