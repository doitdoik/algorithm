# boj 1978 소수 찾기

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    chk = 1
    for j in range(2, i):
        if i % j == 0:
            chk = 0
            break
    if chk and i != 1:
        cnt += 1

print(cnt)