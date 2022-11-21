import sys

input = sys.stdin.readline
x , y = map(int, input().rstrip().split())
z = (y * 100) // x
res = 0

if z >= 99:
    print(-1)
else:
    res = 0
    start = 1
    end = 1000000000

    while start <= end:
        mid = (start + end)//2
        if (y + mid) * 100 // (x + mid) > z:
            res = mid
            end = mid-1
        else:
            start = mid+1
    print(res)