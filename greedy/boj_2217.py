import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for i in range(n)]
res = []

arr.sort(reverse=True)

for i in range(n) :
    res.append(arr[i]*(i+1))

print(max(res))