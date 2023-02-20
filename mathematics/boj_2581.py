# boj 2581 소수

m = int(input())
n = int(input())
arr =[]

for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        arr.append(i)
        
if len(arr) == 0: print(-1)
else:
    print(sum(arr))
    print(arr[0])