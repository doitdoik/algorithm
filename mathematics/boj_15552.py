# boj 15552 빠른 A+B

import sys

input = sys.stdin.readline
t = int(input())

for i in range(t) :
    a,b = map(int, input().split())
    print(a+b)