import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
value = 0
arr = []
for i in range(n) : 
    s, e = map(int, input().split())
    arr.append([s,e])

arr.sort(key=lambda x : (x[1], x[0]))

for i in range(n) :
    if arr[i][0] >= value :  
        cnt += 1
        value = arr[i][1]
print(cnt)