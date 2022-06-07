import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    C = int(input())
    res = []
    coins = [25, 10, 5, 1]
    for j in range(len(coins)):
        res.append(C // coins[j])
        C %= coins[j]

    print(*res)