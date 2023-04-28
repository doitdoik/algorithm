# boj 9946 단어 퍼즐
import sys

input = sys.stdin.readline
i = 0
while True:
    i += 1
    a = input().strip()
    b = input().strip()
    if a == b == 'END':
        break 
    if sorted(a) == sorted(b):
        print(f"Case {i}: same")
    else:
        print(f"Case {i}: different")