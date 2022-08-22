import sys

input = sys.stdin.readline
n = int(input())
serial = [input().strip() for _ in range(n)]

def getNum(str):
    res = 0
    for i in str:
        if i.isdigit():
            res += int(i)
    return res

serial.sort(key=lambda x: (len(x), getNum(x), x))

for j in serial:
    print(j)

