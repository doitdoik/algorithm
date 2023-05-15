# boj 10156 과자

k, n, m = map(int, input().split())
total = k * n

if total - m < 0:
    print(0)
else:
    print(total - m)