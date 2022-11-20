l = int(input())
arr = list(map(int, input().split()))
n = int(input())
arr.insert(0, 0)  
arr.sort()

if n in arr: 
    print(0)
else:
    for i in range(l):
        if arr[i] < n < arr[i + 1]:  
            res = (n - arr[i]) * (arr[i + 1] - n) - 1
            print(res)
            break