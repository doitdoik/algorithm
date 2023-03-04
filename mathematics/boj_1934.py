# boj 1934 최소공배수
import sys

input = sys.stdin.readline
t = int(input())
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

for i in range(t):
    a, b = map(int, input().split())
    print(a*b//gcd(a, b))