import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    ox = input()
    res = 0
    score = 1
    for i in ox:
        if i == 'O':
            res += score
            score += 1
        else:
            score = 1
    print(res)