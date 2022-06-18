import sys
input = sys.stdin.readline

n = int(input())
res = 0

for i in range(1, n+1) :
    n_list = list(map(int, str(i)))
    n_sum = i + sum(n_list)
    if n_sum == n :
        res = i
        break

print(res)