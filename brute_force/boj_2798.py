n, m = map(int,input().split())
cards = list(map(int,input().split()))
res = []

for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            if cards[i] + cards[j] + cards[k] <= m :
                res.append(cards[i] + cards[j] + cards[k])

print(max(res))