import sys 

input = sys.stdin.readline
arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse = True)
res = 0

for i in range(n):
    if i % 3 != 2:
        res += arr[i]

print(res)