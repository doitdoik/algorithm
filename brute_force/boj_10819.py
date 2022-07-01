from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
res = []

for per in permutations(numbers, n):
    tmp = 0
    for i in range(n - 1):
        tmp += abs(per[i] - per[i + 1])
    res.append(tmp)

print(max(res))