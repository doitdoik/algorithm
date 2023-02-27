# boj 2475 검증수

arr = map(int, input().split())
res = 0

for n in list(arr):
    res += n**2
print(res%10)