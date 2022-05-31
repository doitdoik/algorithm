N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = 0

A.sort()
for i in range(N):
    # res에 가장작은 A, 가장 큰 B를 곱
    res += A[i] * max(B)
    B.remove(max(B))

print(res)