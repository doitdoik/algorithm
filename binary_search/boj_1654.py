import sys

input = sys.stdin.readline
k, n = map(int, input().split())
cable = []

for _ in range(k):
    cable.append(int(input()))

cable.sort()
maxLength = 0

def cut_cable(target, start, end):
    global maxLength
    count = 0
    mid = (start + end) // 2
    
    if start > end:
        return None
    for i in cable:
        count += i // mid
    if count >= target:
        maxLength = max(maxLength, mid)
        return cut_cable(target, mid+1, end)
    elif count < target:
        return cut_cable(target, start, mid-1)

result = cut_cable(n, 1,max(cable))

print(maxLength)