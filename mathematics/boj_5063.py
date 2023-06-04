# boj 5063 TGN
t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    d = b - c
    if a > d:
        print("do not advertise")
    elif a < d:
        print("advertise")
    else:
        print("does not matter")