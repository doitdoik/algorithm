# boj 9085 더하기

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(arr))