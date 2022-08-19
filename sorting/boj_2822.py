score = []
res = []
total = 0
for _ in range(8) :
    score.append(int(input()))

for _ in range(5) :
    total += max(score)
    idx = score.index(max(score))
    res.append(idx+1)
    score[idx] = 0

res.sort()

print(total)
print(*res)
