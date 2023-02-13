# boj 1929 소수 구하기

m, n = map(int, input().split())
chk = [False] * (n+1)
chk[1] = True

for i in range(2, n+1):
    if chk[i]: continue
    for j in range(i*2, n+1, i):
        chk[j] = True

for k in range(m, n+1):
    if not chk[k]:
        print(k)