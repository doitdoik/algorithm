import sys

input = sys.stdin.readline
arr = [int(input()) for _ in range(9)]

for i in range(8):
    for j in range(i + 1, 9):
        res = 0

        for k in range(9):
            if k == i or k == j:
                continue
            res += arr[k]
            
        if res == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(arr[k])
            exit()