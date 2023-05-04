# boj 25372 성택이의 은밀한 비밀번호
import sys

input = sys.stdin.readline
n = int(input())

for i in range(n) :
    s = input().strip()
    if (len(s) <= 9) & (len(s) >= 6) :
        print("yes")
    else :
        print("no")