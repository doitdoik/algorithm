# boj 2953 나는 요리사다
idx = 0
res = 0
for i in range(5):
    sum = 0
    a = map(int, input().split())
    a = list(a)
    for j in range(4):
        sum += a[j]
    if(res < sum):
        res = sum
        idx = i+1

print(idx, res)