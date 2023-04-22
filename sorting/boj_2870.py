# boj 2870 수학숙제
import re

res = list()
for i in range(int(input())):
    s = input()
    for v in re.split('[a-z]', s):
        if v:
            res.append(int(v))
res.sort()
for j in res: print(j)
