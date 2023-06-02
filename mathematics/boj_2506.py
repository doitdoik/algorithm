# boj 2506 점수계산
n = int(input())
sum = 0
res = 0
k = list(map(int, input().split()))

for i in range(n):
    if k[i] == 1:
        sum += 1
        res += sum
    else:
        sum = 0

print(res)