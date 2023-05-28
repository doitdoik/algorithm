# boj 2460 지능형 기차 2
res = 0
sum = 0

for _ in range(10):
    n, m = map(int, input().split())
    sum += (m-n)
    res = max(res, sum)

print(res)