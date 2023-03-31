# boj 6603 로또
import itertools

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    s = list(itertools.combinations(s, 6))
    for i in s:
        for j in i:
            print(j, end=' ')
        print()
    print()