import sys

input = sys.stdin.readline
n, c = map(int, input().split())
house = []

for _ in range(n):
    house.append(int(input()))

house.sort()
start = 1
end = house[-1] - house[0]
res = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    tmp = house[0]
    
    for i in range(1, n):
        if house[i] >= tmp + mid:
            cnt += 1
            tmp = house[i]

    if cnt < c:
        end = mid - 1
    else:
        start = mid + 1
        res = mid

print(res)