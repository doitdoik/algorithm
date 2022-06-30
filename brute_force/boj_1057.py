n, jm, hs = map(int, input().split())

round = 0

while (n > 1) and (jm != hs) :
    n -= n//2
    jm -= jm//2
    hs -= hs//2
    round += 1

if n == 1 and jm != hs :
    round -= 1

print(round)
