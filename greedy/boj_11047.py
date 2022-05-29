
n, k = map(int, input().split())
coins = []
cnt = 0
for i in range(n) :
    coins.append(int(input()))

coins.sort(reverse=True)

for i in range(n) :
    cnt += k // coins[i]
    k %= coins[i]
    if k == 0 :
        break

print(cnt)

