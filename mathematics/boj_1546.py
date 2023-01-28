# boj 1546 평균

n = int(input())
arr = list(map(int, input().split()))
avg = 0

for i in range(n):
    avg += arr[i] / max(arr) * 100
    
print(avg / n)