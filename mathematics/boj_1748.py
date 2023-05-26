# boj 1748 수 이어 쓰기 1

n = input()
comp = len(n) - 1
res = 0

for i in range(comp):
    res += 9 * (10 ** i) * (i + 1)
    i += 1
res += ((int(n) - (10 ** comp)) + 1) * (comp + 1)

print(res)