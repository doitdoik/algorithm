import sys

def search_num(a, x):
    start = 0
    end = len(a)-1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
x = list(map(int, input().split()))

for i in range(m):
    print(search_num(a, x[i]))