m = int(input())
n = int(input())
res = []
i = 1

while i**2 <= n :
    if m <= i**2 <= n :
        res.append(i**2)
    i += 1

if len(res) == 0:
    print(-1)
else :
    print(sum(res))
    print(min(res))
