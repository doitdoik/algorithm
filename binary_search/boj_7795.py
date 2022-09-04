import sys

input = sys.stdin.readline
t = int(input())

def bin_search(target, data):
    start = 0
    end = len(data) - 1
    res = -1
    while start <= end:
        mid = (start+end) // 2
        if data[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid -1
    return res

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    cnt=0
    
    for i in a:
        cnt += bin_search(i, b) + 1

    print(cnt)

