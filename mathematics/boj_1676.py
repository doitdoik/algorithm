# boj 1676 팩토리얼 0의 개수
import sys

input = sys.stdin.readline
n = int(input())

cnt = 0
while n > 0:
    cnt += n // 5
    n //= 5

print(cnt)