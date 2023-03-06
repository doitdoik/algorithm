# boj 11050 이항 계수 1
import math

n, k = list(map(int, input().split()))
res = 1
for i in range(k) :
    res *= n-i

res = res // math.factorial(k)

print(res)