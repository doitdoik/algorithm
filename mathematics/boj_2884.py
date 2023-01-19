# boj 2884 알람시계

h, m = map(int, input().split())

if m >= 45:
    m -= 45
else:
    h -= 1
    if h == -1:
        h = 23
    m = m + 15
print (h, m)